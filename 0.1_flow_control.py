# for loop, if else, while loop, try except continue catch ... break ... based on the frequency




import numpy as np
import pandas as pd
import os


os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/BTH/2_results")

df = pd.read_csv("NCP_surface_AW2016_AW2017_raw_data.csv")
df.head()


import time

start = time.time()

for i in range(df.shape[0]):
    if ((df['lon'][i] > 114.5) &
        (df['lon'][i] < 115) &
        (df['lat'][i] > 35)  &
        (df['lat'][i] < 40)):
        print(df.lon[i])
        
end = time.time()
print("TIME",end - start)


import time

start = time.time()

for i in range(df.shape[0]):
    if ((df['lon'][i] > 114.5) and
        (df['lon'][i] < 115) and
        (df['lat'][i] > 35)  and
        (df['lat'][i] < 40)):
        print(df.lon[i])
        
end = time.time()
print("TIME",end - start)


# but "&" is important, and can not be excluded, see the example here:

# this works
df1 = df[(df['lon'] > 114.5) &
         (df['lon'] < 115) &
         (df['lat'] > 35)  &
         (df['lat'] < 40)]

df1

# but this does not work
df2 = df[(df['lon'] > 114.5) and
         (df['lon'] < 115) and
         (df['lat'] > 35)  and
         (df['lat'] < 40)]

df2







######################################
for var in input_list:
    var = do_sth_to(var)
    
print(input_list)


data = [1,2,3]
data_out = []

for var in data:
    data_out.append(var+1)
    
print(data_out)


a = 1
b = 2
c= 3

list1 = []

for X in [a,b,c]:
    X = X+1
    print(X)
    list1.append(X)
    
    
a,b,c=list1
    
#
print("check outputs:",a,b,c)
