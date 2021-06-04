###########################################################################################################################
###########################################################################################################################
# NetCDF (Network Common Data Form) is a set of software libraries and self-describing, machine-independent data formats 
# that support the creation, access, and sharing of array-oriented scientific data. 
# NetCDF4 files are frequently used in fields of atmospheric sciences, environmental sciences and earth sciences.

# Xarray is a powerful Python package designed for processing ND arrays. It is pretty smart at handling NetCDF4 files. 
# I think Xarray is very well developed (just like Pandas), I would strongly recommend it.
# You can find many useful functions on its homepage: http://xarray.pydata.org/en/stable/
# There is already a very nice tutorial of Xarray written by Jiawei Zhuang: https://github.com/geoschem/GEOSChem-python-tutorial

# Based on Xarray, there is a also a Rioxarray: https://corteva.github.io/rioxarray/stable/index.html
# But currently this is just something to be aware of.

# Here I just show how to use xarray to process GEOS-Chem model outputs.
###########################################################################################################################
# load packages

import os
import glob
import numpy  as np
import pandas as pd
import xarray as xr
###########################################################################################################################
# first pick a model scenario

# AW2016 
#os.chdir("/rds/projects/2018/maraisea-glu-01/RDS/GEOSChem/MODEL_OUTPUT/BTH/BTH_AW2016_default")
#os.chdir("/rds/projects/2018/maraisea-glu-01/RDS/GEOSChem/MODEL_OUTPUT/BTH/BTH_AW2016_scaled_NO_SO2_CO")
#os.chdir("/rds/projects/2018/maraisea-glu-01/RDS/GEOSChem/MODEL_OUTPUT/BTH/BTH_AW2016_scaled_NO_SO2_CO_VOC_1.5")
###########################################################################################################################
# check the chosen scenario
print(os.getcwd())

# now read model outputs from the chosen scenario
Species  = sorted(glob.glob("GEOSChem.SpeciesConc*.nc4"))
StateMet = sorted(glob.glob("GEOSChem.StateMet*.nc4"))
Aerosols = sorted(glob.glob("GEOSChem.AerosolMass*nc4"))

# get files from the time periods of interest
Species  = Species[2:8] 
StateMet = StateMet[2:8]
Aerosols = Aerosols[2:8]

# check the selected files
print(*Species,*StateMet,*Aerosols, sep = "\n")

# extract data fields from GC output files
Species  = [xr.open_dataset(file) for file in Species]
StateMet = [xr.open_dataset(file) for file in StateMet]
Aerosols = [xr.open_dataset(file) for file in Aerosols]

# surface layer data
surface_NO2 = [data['SpeciesConc_NO2'].isel(time=0,lev=0) for data in Species]
surface_SO2 = [data['SpeciesConc_SO2'].isel(time=0,lev=0) for data in Species]
surface_CO  = [data['SpeciesConc_CO'].isel(time=0,lev=0)  for data in Species]
surface_NH3 = [data['SpeciesConc_NH3'].isel(time=0,lev=0) for data in Species]
surface_O3  = [data['SpeciesConc_O3'].isel(time=0,lev=0)  for data in Species]
surface_PM  = [data['PM25'].isel(time=0,lev=0) for data in Aerosols]
surface_TotalOA = [data['TotalOA'].isel(time=0,lev=0) for data in Aerosols]
surface_TotalOC = [data['TotalOC'].isel(time=0,lev=0) for data in Aerosols]
surface_SO4 = [data['AerMassSO4'].isel(time=0,lev=0) for data in Aerosols]
surface_NIT = [data['AerMassNIT'].isel(time=0,lev=0) for data in Aerosols]
surface_NH4 = [data['AerMassNH4'].isel(time=0,lev=0) for data in Aerosols]
surface_BC  = [data['AerMassBC'].isel(time=0,lev=0)  for data in Aerosols]

# convert unit for gases (dry mol/mol to ug/m3)
surface_AIRNUMDEN = [data['Met_AIRNUMDEN'].isel(time=0,lev=0) for data in StateMet]
surface_NO2_mass  = [x*y*46/(6.022*1e11) for (x,y) in zip(surface_NO2,surface_AIRNUMDEN)]
surface_SO2_mass  = [x*y*64/(6.022*1e11) for (x,y) in zip(surface_SO2,surface_AIRNUMDEN)]
surface_CO_mass   = [x*y*28/(6.022*1e14) for (x,y) in zip(surface_CO,surface_AIRNUMDEN)]
surface_NH3_mass  = [x*y*17/(6.022*1e11) for (x,y) in zip(surface_NH3,surface_AIRNUMDEN)]
surface_O3_mass   = [x*y*48/(6.022*1e11) for (x,y) in zip(surface_O3,surface_AIRNUMDEN)]

# calculate averages         
model_NO2 = sum(surface_NO2_mass)/len(surface_NO2_mass)
model_SO2 = sum(surface_SO2_mass)/len(surface_SO2_mass)
model_CO  = sum(surface_CO_mass)/len(surface_CO_mass)
model_NH3 = sum(surface_NH3_mass)/len(surface_NH3_mass)
model_O3  = sum(surface_O3_mass)/len(surface_O3_mass)
model_PM  = sum(surface_PM)/len(surface_PM)
model_TotalOA = sum(surface_TotalOA)/len(surface_TotalOA)
model_TotalOC = sum(surface_TotalOC)/len(surface_TotalOC)
model_SO4 = sum(surface_SO4)/len(surface_SO4)
model_NIT = sum(surface_NIT)/len(surface_NIT)
model_NH4 = sum(surface_NH4)/len(surface_NH4)
model_BC  = sum(surface_BC)/len(surface_BC)

# recover the names for the gaseous
model_NO2 = model_NO2.rename(surface_NO2[0].name)
model_SO2 = model_SO2.rename(surface_SO2[0].name)
model_CO  = model_CO.rename(surface_CO[0].name)
model_NH3 = model_NH3.rename(surface_NH3[0].name)
model_O3  = model_O3.rename(surface_O3[0].name)

# now re-arrange the extraced model results

# combine the variables
model_output = xr.merge([model_NO2,
                         model_SO2,
                         model_CO,
                         model_NH3,
                         model_O3,
                         model_PM,
                         model_TotalOA,
                         model_TotalOC,
                         model_SO4,
                         model_NIT,
                         model_NH4,
                         model_BC])

# subset data over NCP
model_output_NCP = model_output.sel(lat=slice(32,43),lon=slice(107.5,120))

# convert xarray data arrays to a single pandas data frame
def xr_to_df(data):
    data = data.to_dataframe()
    data.reset_index(inplace=True)
    return data

model_output_NCP_df = xr_to_df(model_output_NCP)

# drop the unwanted column
model_output_NCP_df = model_output_NCP_df.drop(['lev'], axis=1)

# fix the columnnames for easy comparison with surface data in future
model_output_NCP_df = model_output_NCP_df.rename(columns={"SpeciesConc_NO2": "GEOSChem_NO2",
                                                          "SpeciesConc_SO2": "GEOSChem_SO2",
                                                          "SpeciesConc_CO" : "GEOSChem_CO",
                                                          "SpeciesConc_NH3": "GEOSChem_NH3",
                                                          "SpeciesConc_O3" : "GEOSChem_O3",
                                                          "PM25": "GEOSChem_PM"})

# check the output
# check the "lat" and "lon"
# this is consistent with R results, but Python draws the map row by row, from bottom-left to top-right
# Python is prefered over R here
print(model_output_NCP_df)

# check the chosen scenario again before saving out
os.getcwd()

# save out the results as csv for easy use in future
os.chdir('/rds/projects/2018/maraisea-glu-01/Study/Research_Data/BTH/2_results')

# assign the output file name accroding to the chosen scenario
#model_output_NCP_df.to_csv('GEOSChem_outputs_AW2016_default.csv',index=False)
#model_output_NCP_df.to_csv('GEOSChem_outputs_AW2016_scaled_NO_SO2_CO.csv',index=False)
#model_output_NCP_df.to_csv('GEOSChem_outputs_AW2016_scaled_NO_SO2_CO_VOC_150.csv',index=False)

# End
###########################################################################################################################
###########################################################################################################################
