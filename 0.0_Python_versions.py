#################################################################################################################
#################################################################################################################
# Here I summarize the Python packages and the verions that I am using

# pakcages for reading research data

import numpy as np
import pandas as pd
import xarray as xr
import netCDF4 as nc4

# packages for data visualisations
import geopandas as gpd
import cartopy as cr
import matplotlib as plt
import geoviews as gv
import seaborn as sns
import plotly as px
import bokeh as bk

# GEOS-Chem python
import gcpy as gc

# now check the versions

print("numpy",np.__version__)
print("pandas",pd.__version__)
print("xarray", xr.__version__)
print("netCDF4",nc4.__version__)
print("="*20)
print("geopandas",gpd.__version__)
print("cartopy",cr.__version__ )
print("matplotlib",plt.__version__)
print("geoviews",gv.__version__)
print("seaborn",sns.__version__)
print("plotly",px.__version__)
print("bokeh",bk.__version__)
print("="*20)
print("GCPy",gc.__version__)
