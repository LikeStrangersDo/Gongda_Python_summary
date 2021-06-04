#####################################################################################################################
# Xarray is strong, but it is not suitable for some types of NetCDF4 files. For example, it can not properly open subgroups within a data file.
# So here I introduce "netCDF4" API: https://unidata.github.io/netcdf4-python/

# Here I use TROPOMI satellite data to illustrate how to use netCDF4 to extract data
#####################################################################################################################
# load packages needed to read raw TROPOMI NO2 L2 products 

import os
import glob
import numpy  as np
from netCDF4 import Dataset
#####################################################################################################################
# find a random sample file
os.chdir('/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/sample')
files = glob.glob("*.nc")
sample_file = files[10]
sample_data = Dataset(sample_file, "r", format="NETCDF4")
sample_data

# explore some frequently used data fields
sample_NO2_VCD = sample_data.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column']
sample_NO2_VCD_fill_value = sample_NO2_VCD._FillValue
sample_NO2_VCD_unit_convert = sample_NO2_VCD.multiplication_factor_to_convert_to_molecules_percm2
sample_NO2_VCD_precision = sample_data.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision']
sample_NO2_VCD_qa_flag = sample_data.groups['PRODUCT'].variables['qa_value']
sample_NO2_lat = sample_data.groups['PRODUCT'].variables['latitude']
sample_NO2_lon = sample_data.groups['PRODUCT'].variables['longitude']
sample_NO2_lat_bounds = sample_data.groups['PRODUCT']['SUPPORT_DATA']['GEOLOCATIONS'].variables['latitude_bounds']
sample_NO2_lon_bounds = sample_data.groups['PRODUCT']['SUPPORT_DATA']['GEOLOCATIONS'].variables['longitude_bounds']
sample_NO2_wind_east = sample_data.groups['PRODUCT']['SUPPORT_DATA']['INPUT_DATA'].variables['eastward_wind']
sample_NO2_wind_north = sample_data.groups['PRODUCT']['SUPPORT_DATA']['INPUT_DATA'].variables['northward_wind']
sample_NO2_Y_axis = sample_data.groups['PRODUCT'].variables['scanline'] # along-track dimension index
sample_NO2_X_axis = sample_data.groups['PRODUCT'].variables['ground_pixel'] # across-track dimension index
sample_NO2_land_type = sample_data.groups['PRODUCT']['SUPPORT_DATA']['INPUT_DATA']['surface_classification']

# print the constants
print("NO2_VCD_fill_value:",sample_NO2_VCD_fill_value)
print("NO2_VCD_unit_conversion_factor:",sample_NO2_VCD_unit_convert)
#####################################################################################################################
# create a "class" of "object" to store data fields from a list of selected TROPOMI files

class TROPOMI_NO2:
    def __init__(self,TROPOMI_files_list):
        '''Process a list of raw TROPOMI NO2 files. This is a flexible selection of files to accommodate each specific task. 
           It can be a list of files between any dates, on certain dates, or grouped by weekdays/weekends.'''
        
        # open the raw files from this list 
        self.TROPOMI_data = [Dataset(file, "r", format="NETCDF4") for file in  TROPOMI_files_list]
            
    def extract_raw_TROPOMI(self):    
        '''Extract relevant variables from a list of raw TROPOMI NO2 files, and close all the files afterwards'''       
        self.NO2 = [np.array(data.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'][0][:][:]) for data in self.TROPOMI_data]
        self.lat = [np.array(data.groups['PRODUCT'].variables['latitude'][0][:][:]) for data in self.TROPOMI_data]
        self.lat_bounds = [np.array(data.groups['PRODUCT']['SUPPORT_DATA']['GEOLOCATIONS'].variables['latitude_bounds'][0][:][:][:]) for data in self.TROPOMI_data]
        self.lon = [np.array(data.groups['PRODUCT'].variables['longitude'][0][:][:]) for data in self.TROPOMI_data]
        self.lon_bounds = [np.array(data.groups['PRODUCT']['SUPPORT_DATA']['GEOLOCATIONS'].variables['longitude_bounds'][0][:][:][:]) for data in self.TROPOMI_data]     
        self.flag = [np.array(data.groups['PRODUCT'].variables['qa_value'][0][:][:]) for data in self.TROPOMI_data]
        self.pre  = [data.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'][0][:][:] for data in self.TROPOMI_data]
        self.sza  = [data.groups['PRODUCT']['SUPPORT_DATA']['GEOLOCATIONS']['solar_zenith_angle'][0][:][:] for data in self.TROPOMI_data]
        self.cld  = [data.groups['PRODUCT']['SUPPORT_DATA']['INPUT_DATA']['cloud_fraction_crb'][0][:][:] for data in self.TROPOMI_data]
        self.land = [np.array(data.groups['PRODUCT']['SUPPORT_DATA']['INPUT_DATA']['surface_classification'][0][:][:]) for data in self.TROPOMI_data]
        [file.close() for file in self.TROPOMI_data]
            
        # now process the data fields which have been stored by the "TROPOMI_NO2" object          
    def process_raw_TROPOMI(self):
        '''For data from each file, do some processing: remove the fill values, apply quality flags, convert units etc.'''
        for i in range(len(self.TROPOMI_data)):
            self.NO2[i] = np.where(self.flag[i] >= qa_flag,self.NO2[i],np.nan) # np.where(condition,x,y): if condition == True, yield x, otherwise y
            self.NO2[i] = self.NO2[i]*NO2_unit_conversion  # convert unit to "molecules_percm2"
            self.pre[i] = self.pre[i]*NO2_unit_conversion   
            self.NO2[i] = self.NO2[i]/1e15 # convert to "1e15 molecules_percm2"
            self.pre[i] = self.pre[i]/1e15
        
    def convert_2D_to_1D(self):
        '''For data from each file, convert the variables to 1D, so you can skip the unwanted observations later'''
        self.NO2 = [data.ravel() for data in self.NO2]
        self.lat = [data.ravel() for data in self.lat]
        self.lon = [data.ravel() for data in self.lon]
        self.pre = [data.ravel() for data in self.pre]
        self.sza = [data.ravel() for data in self.sza]
        self.cld = [data.ravel() for data in self.cld]
        self.land = [data.ravel() for data in self.land]
        
    def create_output_file(self):      
        """create a single outputfile to store the results from all selected files""" 
        # use a unique suffix to dinguish the output file from each task
        self.suffix = 'Shipping_NO2_test'   
        # set output direcotry and name the output file
        self.outfile = '/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/project_1_Shipping/NO2_oversampling_input_'+self.suffix
        self.fId = open(self.outfile, "w+") 
        # initialize line counts in the file
        self.line_count = 0
        
    def write_to_output_file(self): 
        """combine variables into a string and write strings to a single txt file"""
        
        # Loop over data, skip invalid NO2 from each data: 
        # (the if else statement here may be improved, can you skip the second condition if the first one is not met? If so, test land classification first, it will be quicker?)
        for i in range(len(self.NO2)):
            for j in range(self.NO2[i].shape[0]):   
                if (math.isnan(self.NO2[i][j]) == False):
                    tstr="{:8}".format(self.line_count)+("{:15.6f}"*4).format(self.lat[i][j],self.lon[i][j],self.sza[i][j],self.cld[i][j])+("{:15.6E}"*3).format(self.NO2[i][j],self.pre[i][j],self.land[i][j])
                    self.fId.write(tstr) # write tstr to the file 
                    self.fId.write("\n") # progresses to the next line
                    self.line_count += 1 # increment the line number
        self.fId.close # close the txt file at end of loop
#####################################################################################################################
# now wrap your processing steps so you can loop over all files together
def prepare_TROPOMI_for_oversampling(raw_TROPOMI_file_list):
    '''given a list of raw TROPOMI files, convert the list to a "TROPOMI_NO2" object,
       and save results from all files to a single text file.
    '''
    test = TROPOMI_NO2(raw_TROPOMI_file_list)
    test.extract_raw_TROPOMI() 
    test.process_raw_TROPOMI()
    test.convert_2D_to_1D()
    test.create_output_file()
    test.write_to_output_file()
    
# test if the function can save out data properly

# get a small dataset
os.chdir('/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/sample')
files = glob.glob("*.nc")
files_list = files[0:3]

# provide input values required
qa_flag = 0.75
NO2_fill_value = 9.96921e+36
NO2_unit_conversion = 6.02214e+19

# run the function
prepare_TROPOMI_for_oversampling(files_list)
#####################################################################################################################
#####################################################################################################################
