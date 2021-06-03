#################################################################################################################
#################################################################################################################
# A list of some freqently used Python packages in research computing in atmopsheric/envionmental sciences

# interactive with operations system (e.g. changing working directories)
import os

# more parameters about system
import sys

# use Unix style pathname pattern expansion to select multiple files
import glob

# numerical Python 
import numpy as np

# read tabular data from csv/xlsx/txt files
import pandas as pd

# read ND data arrays from NetCDF files (frequently used in atmospheric sciences and other fields)
import xarray as xr
import netCDF4 as nc4

# default data visualisation package and foundation for many other packages
import matplotlib as plt

# statistical figures
import seaborn as sns

# visualise spatial data
import geopandas as gpd
import cartopy as cr
import geoviews as gv

# interactive plots
import plotly as px
import bokeh as bk

# python tool for quick analysis of GEOS-Chem model
import gcpy as gc
#################################################################################################################
# always good to know the versions of Python and the packages that you are using
# as sometimes the syntax may change

# check python version
print(sys.version)

# check verions of packages
print("numpy",np.__version__)
print("pandas",pd.__version__)
print("xarray", xr.__version__)
print("netCDF4",nc4.__version__)
print("geopandas",gpd.__version__)
print("cartopy",cr.__version__ )
print("matplotlib",plt.__version__)
print("geoviews",gv.__version__)
print("seaborn",sns.__version__)
print("plotly",px.__version__)
print("bokeh",bk.__version__)
print("GCPy",gc.__version__)

# End
#################################################################################################################
