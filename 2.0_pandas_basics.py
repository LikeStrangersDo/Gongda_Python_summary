#####################################################################################################
# Pandas is extensively used and developed
# I found this official guide very useful: https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html
# It should solve all your issues with Pandas
# Apart from the normal usages of Pandas, there some fun but not neccesary tricks of using Pandas: https://towardsdatascience.com/30-examples-to-master-pandas-f8a2da751fa4

# Some other powerful packages are developed based on Pandas, like "Dask": https://docs.dask.org/en/latest/ 
# Pandas uses a single CPU, while A Dask DataFrame is a large parallel DataFrame composed of many smaller Pandas DataFrames, split along the index
# However, you should be able to solve all your problems using Pandas only
# If speed is a problem, you can try to use paralle programming using "map" in Python, while sticking to Pandas
#####################################################################################################
# Here I just list some Pandas basics

import os
import glob
import pandas as pd
#####################################################################################################
# Work with data files

# move to the working directory
os.chdir("/../../../your working directory/")

# import and sort csv files by filename
surface_files = sorted(glob.glob("china_sites_201610*.csv"))

# read all imported csv files using list comprehension
surface_data  = [pd.read_csv(file) for file in surface_files] 

# select rows based on conditions of a certain column
NO2  = [data[data['type'] == 'NO2'] for data in surface_data] 

# merge the list of data frames into a single dataframe by rows
NO2_total  = pd.concat(NO2) 
print(len(NO2_total))       
print(NO2_total.head())     
print(NO2_total.tail())    

# subset the dataframe using "df.iloc[rows,columns]"
NO2_test = NO2_total.iloc[0:3,0:6] 
print(NO2_test)

# merge two data frames by column
df1 = NO2_total.iloc[0:3,0:4]
df2 = NO2_total.iloc[0:3,0:6]
NO2_test  = pd.merge(df1,df2,left_on = 'date',right_on = 'date') 
print(NO2_test)

# select a column by column name
NO2_date_1 = NO2_total['date']
NO2_date_2 = NO2_total.date

# subset the dataframe by column names
Info  = ['date','hour','type']
Sites = ['1001A','1002A','1003A'] 
NO2_test = NO2_total[Info + Sites]
print(NO2_test)

# subset the dataframe by conditions
NO2_test_1 = NO2_total[(NO2_total['1001A'] < 80) & (NO2_total['1002A'] < 60)] 
NO2_test_2 = NO2_total[(NO2_total['1001A'] < 80) | (NO2_total['1002A'] < 60)] 

print(NO2_test_1)
print(NO2_test_2)

# delete columns by column names
NO2_test = NO2_total.drop(['date','hour','type'],1)
print(NO2_test.head())

# add a column
NO2_test = NO2_total.iloc[0:3,0:6] 
NO2_test['new_column'] = 'test'
print(NO2_test)

# save the pandas dataframe to csv
NO2_total.to_csv('NO2_total.csv', index=False)
#####################################################################################################
# save the pandas dataframe to netcdf files
import xarray as xr

# convert pandas data frame to xarray data format
test = xr.Dataset.from_dataframe(NO2_total)

# see the data format is already changed
test

# add attributes of variables
test['NO2'].attrs = {'unit':'ug/m3'}
test['Site_Longitude'].attrs = {'unit':'Degrees_east'}
test['Site_Latitude'].attrs={'unit':'Degrees_north'}

# save xarray data to netcdf format
test.to_netcdf('China_NO2.nc')

# check if the output is what you expected
China_NO2_nc = xr.open_dataset('China_NO2.nc')
#####################################################################################################
