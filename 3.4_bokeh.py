##############################################################################################
##############################################################################################
# Good examples of Bokeh can be found at: https://docs.bokeh.org/en/latest/index.html

# Here I introduce a way to make use of Google Maps interactively to communicate research (developed in Jupyter Notebook)
# You can also output static Google Maps for presentations

# Preparation: you need a Google Maps API Key before you can access Google Maps
# Get your API: https://developers.google.com/maps/documentation/javascript/get-api-key
# Free to enable, pricing depends on number of requests, $200 credit for free every month

# input your api_key here
api_key = 'xxxxxxxxxxxxxxxxxxx'

# Google Maps from a developer's view: https://developers.google.com/maps/documentation/javascript/overview

# load bokeh with settings
from bokeh.io import output_notebook
output_notebook()

# load tools for interactive Google Maps in the Jupyter notebook
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions

# A webdriver is also required, firefox driver was easy to install "conda install -c conda-forge firefox geckodriver"
##############################################################################################
# create a basic function to show an interactive Google Map
# example usage: show_Google_map("China",40,110,map_type='satellite')

def show_Google_map(map_title,lat,lon,zoom=5,fig_width=500,fig_height=500,map_type='roadmap',input_toolbar_location="below"):
    '''Input a map title, centre coordinates (lat,lon), specify zoom in level, figure dimension, and map_type. 
       Return an interactive Google Map in the Jupyter Notebook.
       If no values are provided for the optional arguments, the default values will be used.
       Available "map_types": roadmap, satellite, hybrid,terrain.
       Available "input_toolbar_location":above,below,left,right and None.
    '''
    # input map info
    gmap_options = GMapOptions(lat=lat, lng=lon,map_type=map_type, zoom=zoom)
    # create the plot with the map info + figure settings
    Map = gmap(api_key, gmap_options, title=map_title, width=fig_width, height=fig_height,
               toolbar_location=input_toolbar_location)
    show(Map)
    return Map
##############################################################################################  
# update the function to plot data on the Google Map
# for examples, plot colored circles to indicate locations of 28 cities in Northern China

# read the coordinates of the cities
import os
import pandas as pd
os.chdir("Y:\Study\Research_Data\BTH\domain")
BTH_cities = pd.read_csv("28_cities.csv")

def show_Google_map(map_title,lat,lon,zoom=5,fig_width=500,fig_height=500,map_type='roadmap',input_toolbar_location="below",input_df):
    '''Input a map title, centre coordinates (lat,lon), specify zoom in level, figure dimension, and map_type. 
       Return an interactive Google Map in the Jupyter Notebook.
       If no values are provided for the optional arguments, the default values will be used.
       Available "map_types": roadmap, satellite, hybrid,terrain.
       Available "input_toolbar_location":above,below,left,right and None.
    '''
    from bokeh.models import ColumnDataSource
    # input map info
    gmap_options = GMapOptions(lat=lat, lng=lon,map_type=map_type, zoom=zoom)
    # create the plot with the map info + figure settings
    Map = gmap(api_key, gmap_options, title=map_title, width=fig_width, height=fig_height,
               toolbar_location=input_toolbar_location)
    
    source = ColumnDataSource(input_df)
    # see how we specify the x and y columns as strings, 
    # and how to declare as a source the ColumnDataSource:
    center = Map.circle('lon', 'lat', size=50, alpha=0.2, 
                      color='data', source=source)    
    show(Map)
    return Map
