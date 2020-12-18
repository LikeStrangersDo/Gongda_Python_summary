##############################################################################################
##############################################################################################
# plotnine: A Grammar of Graphics for Python (https://plotnine.readthedocs.io/en/stable/)

# plotnine is almost a Python clone of "ggplot2" (a very powerful R package for data visualisation)
# So the usages here are actually R codes from ggplot2, but with the Python coating
# But this is totally different from coding R within Python using modules like "rpy2", everything here is still interpreted as Python. 
# You do not need to specify any "R cell" in the Jupyter Notebook for using this. You should be albe to use this in any Python environment.
##############################################################################################
# Example 1: make a scatter plot using "geom_point" from "ggplot2"

# read a sample data
import os 
import pandas as pd
os.chdir('C:\\Users\\geosc\\TEST')
sample_data = pd.read_csv("BTH_emissions_AW2017.csv")

# import the plotnine package
import plotnine as p9

# start plotting
Test_plot = (p9.ggplot(test)  +
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
