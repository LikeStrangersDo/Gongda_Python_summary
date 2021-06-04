###########################################################################################################################
# Cartopy is a mature tool for ploting geospatial data, and it is replacing Basemap.
# In modeling studies, there is always need for plotting colored gridded maps, sometimes with surface data points.
# Here I provide two examples using data from GEOS-Chem model and TROPOMI satellite observations.
# The model outputs are already nd data arrays, it is straightforward to plot.
# The TROPOMI data is in the format of pandas data frames, I introduce a way of converting it to xarrya data arrays before ploting.
# And there are massive TROPOMI plots needed, so I show a way to quickly producing figures by creating my own plotting function.

import os
import glob
import numpy  as np
import pandas as pd
import xarray as xr
import geopandas as gpd

%matplotlib inline
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# set plotting style 
plt.style.use('seaborn-ticks')
###########################################################################################################################
###########################################################################################################################
# Example 1 - plot GEOS-Chem model outputs (already in nd array format)

# read modelled PM2.5 from AW2016
os.chdir("/rds/projects/2018/maraisea-glu-01/RDS/GEOSChem/MODEL_OUTPUT/BTH/BTH_AW2016_scaled_NO_SO2_CO")

# check the directory
print(os.getcwd())

# select GEOS-Chem files
Aerosols_AW2016 = sorted(glob.glob("GEOSChem.AerosolMass*nc4"))
Aerosols_AW2016 = Aerosols_AW2016[2:8]
print(*Aerosols_AW2016, sep = "\n")

# open GEOS-Chem files
Aerosols_AW2016 = [xr.open_dataset(file) for file in Aerosols_AW2016]

# get surface layer PM2.5
surface_PM_AW2016 = [data['PM25'].isel(time=0,lev=0) for data in Aerosols_AW2016]

# calculate season average for AW2016             
gc_PM_AW2016  = sum(surface_PM_AW2016)/len(surface_PM_AW2016)
#####################################################
# import surface data used for comparison with GEOS-Chem
os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/BTH/2_results")
surface_data = pd.read_csv("NCP_surface_AW2016_AW2017_regrid_data.csv")

# modify the colnames
surface_data.rename(columns = {'regrid_lon': 'lon', 'regrid_lat': 'lat'}, inplace = True)

# group the regridded surface data by BTH and OTH

# BTH
BTH_data = surface_data[surface_data['group'] == 'Y']
BTH_data = BTH_data.reset_index(drop=True)

# OTH
OTH_data = surface_data[surface_data['group'] == 'N']
OTH_data = OTH_data.reset_index(drop=True)
#####################################################
# read shapefiles

# China shapefiles (UC Davis GADM 3.6)
os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/BTH/domain/gadm36_CHN_shp")
China_provinces = gpd.read_file("gadm36_CHN_1.shp")
China_cities = gpd.read_file("gadm36_CHN_2.shp")

# check the city list
print(China_cities['NAME_2'])

# get the list of "2+26" cities and get the shapefile for each city
os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/BTH/domain/")
BTH_cities = pd.read_csv("2+26_cities.csv")
BTH_cities = list(BTH_cities['City'])

# extract shapefile for each city
BTH_shapes = [China_cities[China_cities['NAME_2'] == city_name] for city_name in BTH_cities]
print("Number of city shapefiles:",len(BTH_shapes))

# combine shapefiles from all cities
BTH_shapes = gpd.GeoDataFrame(pd.concat(BTH_shapes, ignore_index=True))

# set NCP domain [lon_min,lon_max,lat_min,lat_max]
NCP_domain  = [107.5-0.625/2,120+0.625/2,32-0.5/2,43+0.5/2]
#####################################################
# now start plotting

# move to directory
os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/BTH/3_figures")

# initialize a figure
fig = plt.figure(figsize=[20,20])

# set the map domain
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(NCP_domain)
ax.add_geometries(China_provinces.geometry, crs=ccrs.PlateCarree(),edgecolor='black',facecolor='none',zorder=1)
ax.add_geometries(BTH_shapes.geometry, crs=ccrs.PlateCarree(),edgecolor='purple',facecolor='none',linewidth=2,zorder=1)

# plot AW2016 PM2.5 data from model and the surface observations
gc_PM_AW2016.plot(ax=ax, cmap=WhGrYlRd,vmin = 0,vmax =160,zorder=0)
ax.scatter(x=BTH_data['lon'], y=BTH_data['lat'],marker='^',c=BTH_data['AW2016_PM'],cmap=WhGrYlRd,edgecolors='black',linewidths=3,s = 500,vmin = 0,vmax =160,zorder=2)
ax.scatter(x=OTH_data['lon'], y=OTH_data['lat'],marker='o',c=OTH_data['AW2016_PM'],cmap=WhGrYlRd,edgecolors='black',linewidths=3,s = 500,vmin = 0,vmax =160,zorder=2)

# insert title and text
ax.set_title('AW2016 PM$_\mathregular{2.5}$',fontsize=80,weight='bold', pad=20)
ax.text(107.5,42.5,'OBS: 103.1',fontsize=50,weight='bold',bbox=dict(facecolor='white', edgecolor='black'))   
ax.text(107.5,41.5,'GC: 112.3',fontsize=50,weight='bold',bbox=dict(facecolor='white', edgecolor='black'))

# set your colorbar
PCM=ax.get_children()[2]
bounds = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]
colorbar = plt.colorbar(PCM,ax=ax,label='($\mu$g m$^{-3}$)',orientation='horizontal',shrink=0.8,pad=0.05,extend = 'max',
                       boundaries=bounds)

colorbar.set_ticks([0,30,60,90,120,150])
colorbar.ax.tick_params(labelsize=50) 
colorbar.ax.xaxis.label.set_size(50)

# add lines to color bar
# check later why this one does not work: colorbar.ax.vlines([0,10,20],0,160, colors='black', linestyles='solid',linewidth=10)
for x in np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]):
    colorbar.ax.axvline(x,ymin=0, ymax=1,linewidth=2, color='black')

#set the border width globally
import matplotlib as mpl
mpl.rcParams['axes.linewidth'] = 5 

# remove the unwanted colorbar that comes by default
plt.delaxes(fig.axes[1])

# turn on this to save out without the legend
# plt.delaxes(fig.axes[-1])

# turn on this to generate the legend only
plt.delaxes(fig.axes[0])

# save out
fig.savefig('BTH_model_surface_PM.png', dpi=300,bbox_inches='tight')
###########################################################################################################################
###########################################################################################################################
# Example 2 - plot TROPOMI NO2 from pandas data frames (lat,lon,variable)

# build functions to read oversampled TROPOMI NO2 and HCHO output files as pandas dataframes
def read_oversampled_NO2(TROPOMI_oversampled_NO2_output_file):
    '''read the output file for oversampled TROPOMI NO2'''
    df = pd.read_csv(TROPOMI_oversampled_NO2_output_file,sep="\s+",header=None)
    df = df.iloc[:,2:7]
    df.columns = ['lat','lon','NO2','Count','NO2_uncertainty']
    return df

def read_oversampled_HCHO(TROPOMI_oversampled_HCHO_output_file):
    '''read the output file for oversampled TROPOMI HCHO'''
    df = pd.read_csv(TROPOMI_oversampled_HCHO_output_file,sep="\s+",header=None)
    df = df.iloc[:,2:7]
    df.columns = ['lat','lon','HCHO','Count','HCHO_uncertainty']
    return df
#####################################################
# Step 1> select the oversampled data ( you can repeat the data processing routine and save out accordingly)
os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/project_1_Shipping/Oversample_output/")

domain = "AS"
month = 202012

Oversampled_NO2_data  = "Oversample_output_"+str(domain)+"_NO2_"+str(month)+"_0.05"
Oversampled_HCHO_data  = "Oversample_output_"+str(domain)+"_HCHO_"+str(month)+"_0.05"

# provide the resolution of the oversampled data
Res = 0.05
#####################################################
# Step 2> feed the oversampled data into this data cleaning routine

# read oversampled NO2 and HCHO data
NO2_data  = read_oversampled_NO2(Oversampled_NO2_data)
HCHO_data = read_oversampled_HCHO(Oversampled_HCHO_data)

# combine these data together as we need to look at HCHO/NO2 ratio
NO2_HCHO_data = pd.merge(NO2_data,HCHO_data,on=['lat','lon'])
NO2_HCHO_data = NO2_HCHO_data.dropna()
NO2_HCHO_data['Count'] = NO2_HCHO_data['Count_x']
NO2_HCHO_data = NO2_HCHO_data.drop(['Count_x','Count_y'], 1)
NO2_HCHO_data['ratio'] = NO2_HCHO_data['HCHO']/NO2_HCHO_data['NO2']

# get the domain dimension of the cmobined data
lat_min = NO2_HCHO_data['lat'].min()
lat_max = NO2_HCHO_data['lat'].max()
lon_min = NO2_HCHO_data['lon'].min()
lon_max = NO2_HCHO_data['lon'].max()

# set the domain map based on the resolution

# first list all the lats and lons - use (min,max+1/2 resolutions, resolution) to keep the max value in Python
domain_lat = np.arange(lat_min,lat_max+Res/2,Res,dtype=None)
domain_lon = np.arange(lon_min,lon_max+Res/2,Res,dtype=None) 

# just round the floats created by Python to be safe
# actually this is so very important North Python always hNorth issues with precisions of floats
# for the following "pd.merge" step, it requires the values of "keys" to be excatly the same
domain_lat = np.round(domain_lat,3)
domain_lon = np.round(domain_lon,3)

# build a function to create a "full grid" by listing the full combinations of lats and lons in the domain
def expand_grid(lat,lon):
    '''list all combinations of lats and lons using expand_grid(lat,lon)'''
    test = [(A,B) for A in lat for B in lon]
    test = np.array(test)
    test_lat = test[:,0]
    test_lon = test[:,1]
    full_grid = pd.DataFrame({'lat': test_lat, 'lon': test_lon})
    return full_grid

# get the "full grid"
domain_grid = expand_grid(domain_lat,domain_lon)

# combine the data with the full domain grids
NO2_HCHO_data = pd.merge(domain_grid,NO2_HCHO_data,how='left', on=['lat','lon'])
NO2_HCHO_data = NO2_HCHO_data.sort_values(by=['lat','lon'], ascending=[True, True])

# reshape the variables from 1D in the dataframe to the map dimension
NO2 = NO2_HCHO_data['NO2'].values.reshape(len(domain_lat),len(domain_lon))
NO2_uncertainty = NO2_HCHO_data['NO2_uncertainty'].values.reshape(len(domain_lat),len(domain_lon))
HCHO = NO2_HCHO_data['HCHO'].values.reshape(len(domain_lat),len(domain_lon))
HCHO_uncertainty = NO2_HCHO_data['HCHO_uncertainty'].values.reshape(len(domain_lat),len(domain_lon))
Ratio = NO2_HCHO_data['ratio'].values.reshape(len(domain_lat),len(domain_lon))
Count = NO2_HCHO_data['Count'].values.reshape(len(domain_lat),len(domain_lon))

# convert to xarray for plotting
NO2_xarray = xr.DataArray(NO2, coords=[('lat', domain_lat),('lon', domain_lon)])
NO2_uncertainty_xarray = xr.DataArray(NO2_uncertainty, coords=[('lat', domain_lat),('lon', domain_lon)])
HCHO_xarray = xr.DataArray(HCHO, coords=[('lat', domain_lat),('lon', domain_lon)])
HCHO_uncertainty_xarray = xr.DataArray(HCHO_uncertainty, coords=[('lat', domain_lat),('lon', domain_lon)])
Ratio_xarray = xr.DataArray(Ratio, coords=[('lat', domain_lat),('lon', domain_lon)])
Count_xarray = xr.DataArray(Count, coords=[('lat', domain_lat),('lon', domain_lon)]) 

# check again the data used
print(Oversampled_NO2_data,Oversampled_HCHO_data,sep = "\n")

# use one month as an example
NO2_xarray_1901 = NO2_xarray.copy()
HCHO_xarray_1901 = HCHO_xarray.copy()
Ratio_xarray_1901 = Ratio_xarray.copy()
#####################################################
# Step 3> prepare for making plots 

# avoid setting "%matplotlib inline" as it is time consuming when we need to produce many figures
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import geopandas as gpd

# read shape file (Global high resolution shoreline database from NOAA: https://www.ngdc.noaa.gov/mgg/shorelines/)
# use "full reolution" here
os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/shapefiles/gshhg-shp-2.3.7/GSHHS_shp/f")
world_shore = gpd.read_file("GSHHS_f_L1.shp")
#####################################################
# build a function for quick plotting without plot tile (you can also decide to add plot tile)

def quick_plot(input_xr,plot_domain,label,var_min,var_max,output_figure_name):
  '''provide input information in order, and generate a corresponding figure'''
    fig = plt.figure(figsize=[20,10])
    cbar_keys = {'shrink': 0.5, 'pad' : 0.05,'orientation':'horizontal','label':label} 
    # set the map projection: https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html#cartopy-projection
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent(plot_domain)
    # plotthe value on map
    im = input_xr.plot(ax=ax,cmap='jet',cbar_kwargs=cbar_keys,vmin=var_min,vmax=var_max)
    # set color bar label size
    plt.rcParams.update({'font.size':12})
    ax.xaxis.label.set_size(12)
    # add shapefile
    ax.add_geometries(world_shore.geometry, crs=ccrs.PlateCarree(),edgecolor='black',facecolor='none')
    # save out
    fig.savefig(output_figure_name, dpi=100,bbox_inches='tight')
#####################################################
# now plot
os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/project_1_Shipping/Figures/New/AS/")

# set domain [lon_min,lon_max,lat_min,lat_max]
AS_domain = [60,130,-10,25]
EA_domain = [110,150,15,45]
YRD_domain = [117.5,129,23,34]
CKJ_domain = [115,144,32,42]

EU_domain = [-20,60,5,65]
US_domain = [-130,-30,-10,50]

# plot over domain
domain = "AS"
month = "1901"

quick_plot(NO2_xarray_1901,AS_domain,'NO$_2$ tropospheric column [$10^{15}$ molec. cm$^{-2}$]',0,2,str(domain)+"_NO2_"+str(month))
quick_plot(HCHO_xarray_1901,AS_domain,'HCHO tropospheric column [$10^{15}$ molec. cm$^{-2}$]',0,5,str(domain)+"_HCHO_"+str(month))
quick_plot(Ratio_xarray_1901,AS_domain,'HCHO/NO$_2$ ratio [unitless]',0,15,str(domain)+"_HCHO_NO2_Ratio_"+str(month))
###########################################################################################################################
###########################################################################################################################
# additional notes:
# if the file sizes of TROPOMI figures are too big
# you can build a function to convert the png figures to jpeg figure
# this will reduce the figure size while degrades the quality

def png_to_jpeg(input_filename,output_filename):
    '''Input a png filename like "test.png", save out a jpeg figure like "test.jpeg"'''
    from PIL import Image
    image = Image.open(input_filename)
    image_rgb = image.convert('RGB')
    image_rgb.save(output_filename)
    
# End
###########################################################################################################################
