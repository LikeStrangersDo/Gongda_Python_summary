#####################################################################################################
# Advatanges of Numpy:
# Numpy is useful for handling ND arrays, as we are dealing with spatial datasets (lat,lon,height,time,variable1,variable2), numpy is a good tool to mange
# Numpy is fast than for loops. Vectorized operations in Numpy are mapped to highly optimized C code, making them much faster than their standard Python counterparts.

# Numpy is a core package of Python
# You can visit its offical page for compreshensive understanding of numpy
# 1> for beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
# 2> advanced users: https://numpy.org/doc/stable/reference/

# And there is already a short and good visual guide to NumPy by Lev Maximov
# Original post: https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d?gi=2bf5aae3a590
# Chinese version: https://zhuanlan.zhihu.com/p/342356377
#####################################################################################################
# so here I just list some easy examples of numpy usages
import numpy as np

# array/matrix/sequence
a = np.array([1,2,3,4,5])
b = np.zeros(3,dtype=float) 
c = np.zeros((3,5),dtype=int)
d = np.full((3,5),'NA')
e = np.arange(0,20,2)
f = np.linspace(0,1,5)

print(a,b,c,d,e,f,sep="\n")
print(c.ndim,c.shape,c.size,c.dtype,end='')

# dtype is important
x = np.array([1,2,3,4,5])
x[0] = 3.14
print(x)

y = np.array([1,2,3,4,5],dtype = float)
y[0] = 3.14
print(y)

# make an empty N-d array
test = np.zeros((3,5))
#####################################################################################################
# An example application of NumPy in our research
# For some spatial analysis, we can use NumPy to generate some masks (e.g. scale factors for GEOS-Chem emissions)

# Use North China Plain (NCP) as the example
# first list lons and lats for GEOS-Chem grid centres over NCP, not the domain boundaries
import numpy as np

NCP_lon = np.arange(107.5,120+5/16,5/8) # use (start,end+resolution/2,resolution) to keep the maximum value
NCP_lat = np.arange(32,43+1/4,1/2)
time = np.array(['2020-01-01T00:00:00.000000000'], dtype='datetime64[ns]')
print("Your lon:",NCP_lon,"#"*50,"Your lat:",NCP_lat,"#"*50,sep="\n")

# Example 1 > apply a single scale factor of 1.5 to nitric oxide emissions
NO_mask = np.full((1,len(NCP_lat),len(NCP_lon)), 1.5)

# convert the NumPy array to Xarray so that you can save out the results as a NetCDF file
import xarray as xr

NO_mask = xr.DataArray(NO_mask, coords=[('time',time),('lat', NCP_lat),('lon', NCP_lon)])
NO_mask.name = "MASK"
NO_mask['lon'].attrs = {'long_name':'longitude','units':'degrees_east','axis':'X'}
NO_mask['lat'].attrs = {'long_name':'Latitude','units':'degrees_north','axis':'Y'}
NO_mask.attrs = {'long_name':'NO emission mask for North China Plain','units':'unitless'}
NO_mask.to_netcdf("NCP_NO_mask.nc")

# Example 2 > apply spatially varying factors for sulfur dioxide emissions

# set base = 1, then apply factors only for some target grids only
SO2_mask = np.ones((1,len(NCP_lat),len(NCP_lon)),dtype = float)

# assign different factors [time,lat,lon]
SO2_mask[0,8,6] = 6
SO2_mask[0,8,9] = 3
SO2_mask[0,11,8] = 3 
SO2_mask[0,12,8] = 2 
SO2_mask[0,12,10] = 2 
SO2_mask[0,13,8] = 3 
SO2_mask[0,15,8] = 3 

# End
#####################################################################
