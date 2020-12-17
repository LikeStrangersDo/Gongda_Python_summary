##############################################################################################
##############################################################################################
# Sometimes you may want to conduct only a small part of your job using R programming, for example:
# 1> download air quality data in the UK, using "importKCL" function from the "openair" R package
# 2> use R as a sanity check for results from a certain step in Python

# Here I provide a way of using R in Python, but only under the Jupyter Notebook on your own PC
# This means that you have the admin permission to install any R packages needed while proceeding the codes
##############################################################################################
# When I first tried this, I found the solution on: https://anderfernandez.com/en/blog/how-to-program-with-python-and-r-in-the-same-jupyter-notebook/
# But following this alone may not be enough, I did have to Goolge some errors during my installation process.

# Major steps:
# Step 1: install R on Jupyter Notebook: conda install -c r r-essentials
# Step 2: install the "rpy2" Python package: pip install rpy2 (you may or may not have to check the version)
# Step 3: create the environment variables: R_HOME, R_USER and R_LIBS_USER (you can modify these in the system settings on your PC or you can use codes to do this everytime)

# When you are done with installing "rpy2"
# load the rpy2 module
%load_ext rpy2.ipython

# Then you will be able to enable an R cell in the Python Jupyter Notebook
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
# you need to output this to the Python environmental as well, using:
# %%R -o sample_data
# now you should be able to access "sample_data" in both R and Python cells
##############################################################################################
# Remarks: Some bugs may occur when you "library()" a package, you can just install it again within the Jupyter Notebook.
#          This may be doable on university HPC, the key is the admin permission. If the user is allowed to create his/her own micro environment, it should be fine.  
# End
##############################################################################################
