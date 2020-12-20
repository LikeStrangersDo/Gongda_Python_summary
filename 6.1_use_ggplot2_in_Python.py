##############################################################################################
##############################################################################################
# "ggplot2" is a very powerful R package for data visualisation.
# In Python, you can use "plotnine", which is almost a clone of "ggplot2": https://plotnine.readthedocs.io/en/stable/
# The function actually uses R codes from ggplot2, but with the Python coating.
# This is different from coding R within Python using "rpy2", as codes here are still interpreted as Python. 
# So you do not need to specify any "R cell" in the Jupyter Notebook for this. And you should be able to use this under any Python environment.
##############################################################################################
# Example: 

# read a sample data
import os 
import pandas as pd
os.chdir('C:\\Users\\geosc\\TEST')
sample_data = pd.read_csv("BTH_emissions_AW2017.csv")

# import the plotnine package
import plotnine as p9

# make a scatter plot using "geom_point" from "ggplot2"
Test_plot = (p9.ggplot(sample_data)  +
             p9.xlim(0,0.5)   +
             p9.ylim(0,0.5)   +
             p9.coord_fixed() +
             p9.geom_point(aes('OC_AW2017','BC_AW2017'),size = 20,color='red'))

# show the plot (just like in ggplot2!)
Test_plot

# save out the figure (just like in ggplot2!)
Test_plot.save('test.png',dpi=300,width = 20, height = 20)
##############################################################################################
# Remarks: "plotnine" certainly provides a straighforward way to use "ggplot2" in Python.
#           But things like "patchwork" seems to be not possible at least by now, need to consider how to combine multiple plots.

# End
##############################################################################################
