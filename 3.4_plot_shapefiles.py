###############################################################################################
###############################################################################################
# For research publications, normally the shapefiles are needed to make maps
# Then you can add data points or fill the grids to show your data upon the map (see "")

# In this script, I focus on how to work with shapefiles
# shapefiles source: https://gadm.org/download_country_v3.html
# I am using a "shapefile" which consists of at least four actual files (.shp, .shx, .dbf, .prj). This is an obsolete, but still commonly used format. 
# The new ".rds" format shapefiles seem to be designed only for use in R.
# For more about shapefile formats: https://gadm.org/formats.html

# move to the directory for the files
import os
os.chdir("C:\Study\Shapefile\gadm36_GBR_shp")
###############################################################################################
# Method 1 (Matplotlib + Cartopy)
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

# import the shapefile
UK_shape_file = r'gadm36_GBR_3.shp'
# get the map (geometries)
UK_map = ShapelyFeature(Reader(UK_shape_file).geometries(),ccrs.PlateCarree(), edgecolor='black',facecolor='none')
# initialize a plot
test= plt.axes(projection=ccrs.PlateCarree())
# add the shapefile for the whole UK
test.add_feature(UK_map) 
# zoom in to London
test.set_extent([-2,2,51,52], crs=ccrs.PlateCarree()) 
###############################################################################################
# Method 2 (Matplotlib + Cartopy + Geopandas)
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import geopandas as gpd

# read the UK shapefile as a "geopandas.geodataframe.GeoDataFrame"
UK_shapefile = gpd.read_file("gadm36_GBR_3.shp")
# check what UK shapefile contains
UK_shapefile
# get shapes for London, Birmingham and Edinburgh from the UK shapefile
# you can also go to a coarser/finer layer to select a bigger/smaller domain
London = UK_shapefile[UK_shapefile['NAME_2'] == "Greater London"]
Birmingham = UK_shapefile[UK_shapefile['NAME_2'] == "Birmingham"]
Edinburgh  = UK_shapefile[UK_shapefile['NAME_2'] == "Edinburgh"]

# check the geometry for each city
print(London.geometry)
print(Birmingham.geometry)
print(Edinburgh.geometry)

# create a list of your study cities and merge the shapes (geopandas.geodataframe.GeoDataFrame)
import pandas as pd
study_cities = [London,Birmingham,Edinburgh]
study_cities_shapes = gpd.GeoDataFrame(pd.concat(study_cities, ignore_index=True))

# initialize a plot
test= plt.axes(projection=ccrs.PlateCarree())
# add shapefiles to your chosen cities only
# you can change "edgecolor", "facecolor" and "linewidth" to highlight certain areas
# you can change the "zorder" to decide the layer
test.add_geometries(study_cities_shapes.geometry, crs=ccrs.PlateCarree(),edgecolor='black',facecolor='none',linewidth=2,zorder=0)

# zoom in to your study domain
test.set_extent([-5,2,51,57], crs=ccrs.PlateCarree())
###############################################################################################
# Remarks:
# 1> I prefer Method 2 as "Geopandas" allows you to have more controls of the shapefile
# 2> But it can be almost impossible to install geopandas on your PC, if you are following the instructions on its homepage.
#    I managed to install it on windows following this video: https://www.youtube.com/watch?v=LNPETGKAe0c
# 3> Since that "Geopandas" may not be always available on all platforms, Method 1 becomes somehow essential too.

# End
###############################################################################################
