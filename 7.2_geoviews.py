############################################################################################################################
############################################################################################################################
# Use "GeoViews" to create interactive maps for the shipping project

# advantages:
# 1> zoom in to see the details
# 2> combine multiple plots into a single file to see the changes

# load GeoViews package
import geoviews as gv
import geoviews.feature as gf

# it is important to check your geoviews version or some commands may not work
# this script is written with version 1.9.1
print(gv.__version__)

# there are two backends for the GeoViews, although for interactive plots, we will use "bokeh" only
gv.extension('bokeh', 'matplotlib')

# load other frequently used packages for data analysis and visualisations
import os
import glob
import numpy as np
import pandas as pd
import xarray as xr
import geopandas as gpd
from cartopy import crs



############################################################################################################################
# interactive maps for xarray data

# get some xarray data from GEOS-Chem outputs
import os
import glob
import xarray as xr

# use your BTH GEOS-Chem results as the example
os.chdir("Y:/RDS/GEOSChem/MODEL_OUTPUT/BTH/PM_components")

# # open a sample GEOS-Chem output file
sample_files = sorted(glob.glob("GEOSChem.AerosolMass*nc4"))
sample_data = [xr.open_dataset(file) for file in sample_files]

# get surface layer PM2.5
#sample_PM = [data['PM25'].isel(time=0,lev=0) for data in sample_data]
sample_PM = [data['PM25'].isel(lev=0) for data in sample_data]


############################################################################################################################
# 1> make a basic interactive map

# first turn on "bokeh" backend to enable interactive map
gv.extension('bokeh')

# extract data from a sample xarray
gv_data  = gv.Dataset(sample_PM[0],['lon', 'lat'], 'PM25', crs=crs.PlateCarree())

# use the data to generate the geoviews image
gv_image = gv_data.to(gv.Image)

# decide features of the output figure
gv_image_out = gv_image.opts(cmap='jet', clim=(20,120), colorbar=True, width=800, height=500) * gf.coastline 

# save out the interactive map
os.chdir('C:/TEST/')
renderer = gv.renderer('bokeh')
renderer.save(gv_image_out, 'sample_html_1')

############################################################################################################################
# 2> add your own shape files to the map (https://geoviews.org/user_guide/Geometries.html)

# Method A: import the shapefile using holoviews

import holoviews as hv
hv.output(backend='bokeh')

os.chdir("Y:/Study/Research_Data/BTH/domain/gadm36_CHN_shp")
China_shapefile = "gadm36_CHN_1.shp"
China_shape = gv.Shape.from_shapefile(China_shapefile, crs=crs.PlateCarree(),color='none')

# plot China shape file onto the map
gv_image_out = gv_image.opts(cmap='jet', clim=(0,140), colorbar=True, width=800, height=500) * China_shape 

# save out
os.chdir('C:/TEST/')
renderer = gv.renderer('bokeh')
renderer.save(gv_image_out, 'sample_html_2')


# Method B: add shapefiles using Geopandas (but need to figure out how to remove fill color for the Polygons)

import geopandas as gpd
os.chdir("Y:/Study/Research_Data/BTH/domain/gadm36_CHN_shp")
China_provinces = gpd.read_file("gadm36_CHN_1.shp")

China_provinces = gv.Polygons(China_provinces)

gv_image_out = gv_image.opts(cmap='jet', clim=(0,140), colorbar=True, width=800, height=500) * China_provinces

# save out
os.chdir('C:/TEST/')
renderer = gv.renderer('bokeh')
renderer.save(gv_image_out, 'sample_html_3')

# Method C: check the examples


############################################################################################################################
# 3> add points and texts to the map

# provide the coordinates (lon,lat)
Beijing = (116.4,39.9)
Tianjin = (117.4,39.3)
Shijiazhuang = (114.5,38.0)

# get the coordinates for all cities
City_points = gv.Points([Beijing,Tianjin,Shijiazhuang])

# get the names for all cities
City_names1 = gv.Text(116.4,39.9,'Beijing')
City_names2 = gv.Text(117.4,39.3,'Tianjin')
City_names3 = gv.Text(114.5,38.0,'Shijiazhuang')

City_names_all = City_names1 * City_names2 * City_names3

# 
gv_image_out = gv_image.opts(cmap='jet', clim=(0,140), 
                             colorbar=True, width=800, height=500) * China_shape * City_points * City_names_all

# save out
os.chdir('C:/TEST/')
renderer = gv.renderer('bokeh')
renderer.save(gv_image_out, 'sample_html_6')


############################################################################################################################
# 4> plot data from multiple days (add time dimension to the plot)

############################################################################################################################
# interactive maps for xarray data

# get some xarray data from GEOS-Chem outputs
import os
import glob
import xarray as xr

# use your BTH GEOS-Chem results as the example
os.chdir("Y:/RDS/GEOSChem/MODEL_OUTPUT/BTH/PM_components")

# # open a sample GEOS-Chem output file
sample_files = sorted(glob.glob("GEOSChem.AerosolMass*nc4"))
sample_data = [xr.open_dataset(file) for file in sample_files]

# get surface layer PM2.5
#sample_PM = [data['PM25'].isel(time=0,lev=0) for data in sample_data]
sample_PM = [data['PM25'].isel(lev=0) for data in sample_data] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! watch this difference!


# first turn on "bokeh" backend to enable interactive map
gv.extension('bokeh')

# extract data from a sample xarray
gv_data  = gv.Dataset(sample_PM,['lon','lat','time'], 'PM25', crs=crs.PlateCarree())

# use the data to generate the geoviews image
gv_image = gv_data.to(gv.Image)

# decide features of the output figure
gv_image_out = gv_image.opts(cmap='jet', clim=(20,120), colorbar=True, width=800, height=500) * gf.coastline 

# save out the interactive map
os.chdir('C:/TEST/')
renderer = gv.renderer('bokeh')
renderer.save(gv_image_out, 'sample_html_1')
