##############################################################################################
##############################################################################################
# Sometimes you may want to conduct only a certain step within your research using R programming, for example:
# 1> download air quality data in the UK, using "importKCL" function from the "openair" R package
# 2> use R as a sanity check for results from a certain step in Python

# Here I provide a way of using R in Python, but currently only with the Jupyter Notebook on your own PC
# This means that you have the admin permission to install any R packages needed while proceeding the codes
# This may also be achievable on university HPC, if the user can create his/her own micro environment and have full permission to it.  
##############################################################################################
# When I first tried to connect R and Python, I was following this page: https://anderfernandez.com/en/blog/how-to-program-with-python-and-r-in-the-same-jupyter-notebook/
# But this may not be enough, I remember I did have to Goolge some errors during the installation process.

# Major steps in installing "rpy2":
# Step 1: install R on Jupyter Notebook: conda install -c r r-essentials
# Step 2: install the "rpy2" Python package: pip install rpy2 (you may or may not have to check the version)
# Step 3: create the environment variables: R_HOME, R_USER and R_LIBS_USER (you can modify these in the system settings on your PC or you can use codes to do this everytime)

# load the rpy2 module after installation
# Then you will be able to enable R cells within the Python Jupyter Notebook
%load_ext rpy2.ipython
##############################################################################################
# Example 1: plot a dataframe using ggplot2

# first read a dataframe using Python
import os
import pandas as pd
os.chdir("C:\\Users\\geosc\\TEST")
test_data = pd.read_csv("BTH_emissions_AW2017.csv")

# now use R to access this dataframe and plot it using ggplot2
# tell Jupyter Notebook that you are going to use R in this cell, and for the "test_data" generated using the Python
%%R -i test_data 
library(ggplot2)

plot <- ggplot(test_data) + 
        geom_point(aes(NO_AW2017,SO2_AW2017),size = 20)
plot
ggsave('test.png')
##############################################################################################
# Example 2: download air quality data at a sample site using "importKCL" function from "openair" package

%%R
library(openair)
sample_data <- importKCL(site = "my1",
                         year = 2009,
                         pollutant = "all",
                         met = FALSE,
                         units = "mass",
                         extra = FALSE,
                         meta = FALSE,
                         to_narrow = FALSE)

# however with the codes above, the output "sample_data" can not be accessed in the Python cells
# you need to output this to the Python environmental as well, using: "%%R -o sample_data" instead of a simple "%%R"
# then you should be able to access "sample_data" in both R and Python cells

# Known issue: some bugs may occur when you "library()" a package, you can just install it again within the Jupyter Notebook.     
# End
##############################################################################################




##############################################################################################
##############################################################################################
# "ggplot2" is a very powerful R package for data visualisation.
# In Python, you can use "plotnine", which is almost a clone of "ggplot2": https://plotnine.readthedocs.io/en/stable/
# The function actually uses R codes from ggplot2, but with the Python coating.
# This is different from coding R within Python using "rpy2", as codes here are still interpreted as Python. 
# So you do not need to specify any "R cell" in the Jupyter Notebook for this. And you should be able to use this under any Python environment.


# Also
# check out sth like this: https://github.com/yhat/ggpy
# https://pypi.org/project/ggplot/
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
