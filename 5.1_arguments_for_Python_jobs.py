#####################################################################################################################
# Apart from using Python interactively, you can submit complete Python jobs under Linux environment.
# And with "arguments", you can quickly submit different jobs without editing the Python script.

# Here I provide an example of this technique to read TROPOMI NO2 data over different domains, time periods with different quality flags using a single Python script.
# This script is used together with "5.2_submit_Python_jobs.sh" on the supercomputer at University of Birmingham.
#####################################################################################################################
#####################################################################################################################
# Read raw TROPOMI NO2 L2 products

import os
import glob
import numpy  as np
import pandas as pd
from netCDF4 import Dataset
import math
import argparse
#####################################################################################################################
# provide the NO2 VCD fill value and unit conversion factor obtained from a sample file
# values are the same for Precision
NO2_fill_value = 9.96921e+36
NO2_unit_conversion = 6.02214e+19

# initialize some parameters for later use, their values will change according to your arguments
start_date = str()  # first sampling date
end_date = str()    # last sampling date
start_hour1 = str() # the string for the starting hour of the swath file
start_hour2 = str() # the string for the starting hour of the swath file
start_hour3 = str() # the string for the starting hour of the swath file
start_hour4 = str() # the string for the starting hour of the swath file

qa_flag = float() # quality flag threshold 
lat_min = float() # lat_min for the requested domain
lat_max = float() # lat_max for the requested domain
lon_min = float() # lon_min for the requested domain
lon_max = float() # lon_max for the requested domain
#####################################################################################################################
# create a function to select files between two dates

def select_TROPOMI_NO2_files_between(start_date,end_date):
    '''Select TROPOMI files within the start date ('yyyymmdd') and end date ('yyyymmdd')'''
    # list all the dates between the start and the end
    from datetime import date, timedelta
    start_date = date(int(start_date[0:4]),int(start_date[4:6]),int(start_date[6:8]))
    end_date   = date(int(end_date[0:4]),int(end_date[4:6]),int(end_date[6:8]))
    delta = end_date - start_date 
    sampling_dates = []
    for i in range(delta.days + 1):
        sampling_dates.append((start_date + timedelta(days=i)).strftime('%Y%m%d'))
    
    # print out all the sampling dates
    print("#"*50,"All sampling dates:",*sampling_dates,sep="\n")
    
    # get files on each day, use  "*" to ingore changes in product versions (RPRO or OFFL)
    TROPOMI_files_each_day = []
    for i in range(len(sampling_dates)):
        TROPOMI_files_each_day.append(sorted(glob.glob('S5P_*_L2__NO2____'+sampling_dates[i]+'*T'+start_hour1+'*_*_*_*_*_*.nc') + \
                                             glob.glob('S5P_*_L2__NO2____'+sampling_dates[i]+'*T'+start_hour2+'*_*_*_*_*_*.nc') + \
                                             glob.glob('S5P_*_L2__NO2____'+sampling_dates[i]+'*T'+start_hour3+'*_*_*_*_*_*.nc') + \
                                             glob.glob('S5P_*_L2__NO2____'+sampling_dates[i]+'*T'+start_hour4+'*_*_*_*_*_*.nc')))
    
    # list the selected files
    import itertools
    print("Number of files:",len((list(itertools.chain.from_iterable(TROPOMI_files_each_day)))))
    print("Files processed:",*list(itertools.chain.from_iterable(TROPOMI_files_each_day)),sep = "\n") 
    
    # return the selected files
    return list(itertools.chain.from_iterable(TROPOMI_files_each_day))
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
        self.suffix = args.domain+'_NO2_'+args.qa_flag+'_'+args.month         
        # set output direcotry and name the output file
        self.outfile = '/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/project_1_Shipping/Oversample_input/Oversample_input_'+self.suffix
        self.fId = open(self.outfile, "w+") 
        # initialize line counts in the file
        self.line_count = 0
        
    def write_to_output_file(self): 
        """combine variables into a string and write strings to a single txt file"""
        # apply the ocean flags obtained from previous results
        ocean_flags = [1,2,3,4,9,11,13,15,17,25,33,41,49,51,53,55,57,59,61,63,124,126]
        
        # Loop over data, skip invalid NO2 from each data: 
        # (the if else statement here may be improved, can you skip the second condition if the first one is not met? If so, test land classification first, it will be quicker?)
        for i in range(len(self.NO2)):
            for j in range(self.NO2[i].shape[0]):   
                if ((math.isnan(self.NO2[i][j]) == False) and
                    (self.land[i][j] in ocean_flags) and
                    (self.lat[i][j] >= lat_min) and
                    (self.lat[i][j] <= lat_max) and
                    (self.lon[i][j] >= lon_min) and
                    (self.lon[i][j] <= lon_max)):
                    tstr="{:8}".format(self.line_count)+("{:15.6f}"*4).format(self.lat[i][j],self.lon[i][j],self.sza[i][j],self.cld[i][j])+("{:15.6E}"*2).format(self.NO2[i][j],self.pre[i][j])
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
#####################################################################################################################
# pass the arguments to specify all requests for this job

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", help="Provide a domain code, choose from US, EU, AS or add your custom domain in the script")
    parser.add_argument("--qa_flag",default='0.75',help="any float between 0 and 1, usually 0.75 or 0.5")
    parser.add_argument("--start_date", help="date string in 'yyyymmdd' format")
    parser.add_argument("--end_date", help="date string in 'yyyymmdd' format")
    parser.add_argument("--month", help="the month string in outputfile name in 'yyyymm' format")
    parser.add_argument("--data_directory", help="where the TROPOMI data files are")
    args = parser.parse_args()
    
    # pass arguments for the sampling period
    start_date = args.start_date
    end_date = args.end_date
    
    # pass arguments for quality flag
    # the argument that you input will be interpreted as a string
    # use "float()" to convert it to a float number
    qa_flag = float(args.qa_flag) 
    
    # pass arguments for the directory
    TROPOMI_files_directory = args.data_directory
    
    # Pass arguments for the study domain
    # Your chosen domain will decide the starting hours of the swath files to be selected
    # Leave sufficient margins, just to ensure that you include all the swaths that have data over your study area
    # You can use NASA GES DISC data subsetting tools to help you decide a domain: 
    # https://disc.gsfc.nasa.gov/datasets/S5P_L2__NO2____HiR_1/summary?keywords=TROPOMI%20NO2
    # Select a domain on the map, insert your sampling period, the NASA tool will return a list of L2 swath files which overpass your domain within your sampling period
    # Then you can check the starting hours of the files and edit the "start_hour" arguments below
    # For mid or high latitude regions (lat > 45?), the swaths are stretched
    # In this case, the NASA subsetting tool will return unwanted files
    # But you can use NASA Panoply to quickly plot the spicious files, just to see where the swaths actually are
    # Or just read all the returned data, and subset the results only based on the lat and lon boundaries (in this case, remove the "start_hour" from the script).
    if args.domain == "US":      # Central America
        lat_min = -10
        lat_max = 50
        lon_min = -130
        lon_max = -30
        start_hour1 = '0[1-9]'
        start_hour2 = '1[0-9]'
        start_hour3 = '2[0-2]'
        start_hour4 = 'None'
    elif args.domain == "EU":    # Europe + Northern Africa
        lat_min =  5
        lat_max =  65
        lon_min = -20
        lon_max =  60
        start_hour1 = '0[0-9]'
        start_hour2 = '1[0-4]'
        start_hour3 = '19'
        start_hour4 = '2[0-3]'
    elif args.domain == "AS":    # Asia
        lat_min = -10
        lat_max = 20
        lon_min = 60
        lon_max = 120
        start_hour1 = '0[3-9]'
        start_hour2 = 'None'
        start_hour3 = 'None'
        start_hour4 = 'None'
    else:
        print("Invalid domain: choose from 'US','EU', and 'AS'. Or add your custom domain.")
        
    # after passing all arguments, the job is already specified (period, quality flag, and where the files are)     
    
    # now start the job
    # move to directory where the raw files are
    os.chdir(TROPOMI_files_directory)
    
    # print the files directory in the slurm.out file
    print("The job starts from here.","#"*50,sep="\n")
    print(TROPOMI_files_directory)
    
    # import files during the sampling period
    TROPOMI_files_list = select_TROPOMI_NO2_files_between(start_date,end_date)
    
    # process each and save outputs from all files to a single txt file
    prepare_TROPOMI_for_oversampling(TROPOMI_files_list)
    
    # check if the job is what you expected
    # the print statements will appear upon job completion
    print("#"*50,"Parameters used in this job:",sep="\n")
    print("Sampling domain:",args.domain)
    print("Species:","NO2")
    print("Sampling period:",start_date,"-",end_date)
    print("output file month:",args.month)
    print("Quality flag threshold:",qa_flag)
    print("The job is done.","#"*50,sep="\n")

# End
#####################################################################################################################
