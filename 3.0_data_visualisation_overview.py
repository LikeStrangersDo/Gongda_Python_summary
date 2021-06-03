#####################################################################################################
# Here I just briefly introduce a few Python packages for data visualisations

#####################################################################################################
# Figures in research publications

# 1> Matplotlib: https://matplotlib.org/
# Python's default plotting package, foundation for many other Python visualisation packages. You should be able to do all kinds of plots with Matplotlib.
# Full user guide: https://matplotlib.org/stable/contents.html
# Quick tutorials: https://matplotlib.org/stable/tutorials/index.html
# Gallery: https://matplotlib.org/stable/gallery/index.html

# 2> Basemap: https://matplotlib.org/basemap/
# Built on Matplotlib, designed for plotting geospatial data
# But it is old and being replaced by Cartopy

# 3> Cartopy: https://scitools.org.uk/cartopy/docs/latest/
# My current default plotting package for geospatial data

# 4> Geopandas: https://geopandas.org/
# A powerful tool for handling shapefiles (read, merge, plot)
# It can always used together with Cartopy or other plotting packages

# 5> Seaborn: https://seaborn.pydata.org/
# Built on Matplotlib, Seabron is good at making beatiful statistical data visualisation

# More about Matplotlib:
# Matplotlib has two APIs: pyplot API (what is normally used) and object-oriented API (more controls of the figure).
# Matplotlib can create interactive plots as well.
# In the full user guide of Matplotlib, there are some more packages that are built upon Matplotlib.  
#####################################################################################################
# Interactive figures

# 1> Plotly: https://plotly.com/python/
# Plotly is quite big and available in a few languages, it is designed for data visualisations for machine learning, data science, engineering, and the sciences. 
# We can just jump to its Python plotting page: https://plotly.com/python/
# The plots are interactive, so they can better show multiple dimensional datasets and help with gaining insights from data
# It is also a good tool for long term timeseires plots, as you can look into details of any short periods

# 2> Bokeh: https://docs.bokeh.org/en/latest/index.html
# Bokeh is another package for interactive plots, somehow simliar to Plotly.
# Bokeh provides a way to interact with Google Maps, which can be useful for research over a domain: https://docs.bokeh.org/en/latest/docs/user_guide/geo.html

# 3> GeoViews: https://geoviews.org/
# GeoViews is built on Bokeh, the advantage is that it can plot xarray data arrays on maps. This means you can have interactive data maps of things like model outputs.

# some other packages also exist: Altair, HoloViews
#####################################################################################################
# ggplot2 in Python
# ggplot2 is a strong R tool for data visualisations. But you can still use it in Python.

# 1> Plotnine: https://plotnine.readthedocs.io/en/stable/
# This is almost a Python clone of ggplot2 in R, although some functions may not be readily available. The syntax is alsmot identical to ggplot2 in R.

# 2> You can call R within Python, using packages like "rpy2" (a bit complicated)

# End
#####################################################################################################
