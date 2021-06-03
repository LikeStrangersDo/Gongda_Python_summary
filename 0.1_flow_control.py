#####################################################################################################
# Apart from "if else", there are other flow control statements like "if not", "break", "continue" and "try except catch" statements.
# for a beginner, "if else" with "for loops" can solve almost all your problems
# here we discuss a bit more about "if else" and "for loops"

#####################################################################################################
# speed up the "if else" statement

# read a sample data 
import numpy as np
import pandas as pd
import os

os.chdir("/rds/projects/2018/maraisea-glu-01/Study/Research_Data/")
df = pd.read_csv("sample_spatial_data.csv")

# print out some data based on latitudes and longitudes and calculate the time needed
import time
start = time.time()

for i in range(df.shape[0]):
    if ((df['lon'][i] > 114.5) &
        (df['lon'][i] < 115) &
        (df['lat'][i] > 35)  &
        (df['lat'][i] < 40)):
        print(df['variable'][i])

end = time.time()
print("TIME",end - start)

# replace "&" with "and", then calculate the time needed
import time
start = time.time()

for i in range(df.shape[0]):
    if ((df['lon'][i] > 114.5) and
        (df['lon'][i] < 115) and
        (df['lat'][i] > 35)  and
        (df['lat'][i] < 40)):
        print(df['variable'][i])
        
end = time.time()
print("TIME",end - start)

# conclusion: for multiple conditions, using "and" is faster than "&", because if a condition is not met, it will not evaluate the following conditions any more

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
#####################################################################################################
# sometimes "for loops" may not store the results

# you may want to do something like below:
for var in input_list:
    var = do_sth_to(var)
    
print(input_list)

# but nothing will change in the data
# here I use an example to explain this

# nothing happens
a = [1,2,3,4]

for number in a:
    number = number + 1
 
print(a)

# in this way, you will get results
b = [number + 1 for number in a]
print(b)

# The only difference is that the list compreshension provided a list to hold the results
#####################################################################################################
