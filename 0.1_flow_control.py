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
