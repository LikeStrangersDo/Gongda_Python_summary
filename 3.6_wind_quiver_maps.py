###########################################################################################################################
###########################################################################################################################
# Quiver plots

# Wind quiver plots are normally seen in papers investigating meterological changes, climate variablities or regional pollution episodes.
# The arrows indicate the wind directions and the length of arrows indicate wind speeds.

# There are existing solutions to these kind of plots: 
# 1> Iris: https://scitools.org.uk/iris/docs/v2.2/examples/Meteorology/wind_speed.html
# 2> Basemap: https://basemaptutorial.readthedocs.io/en/latest/plotting_data.html#quiver
# 3> Matplotlib: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html
# 4> Matplotlib: https://pythonforundergradengineers.com/quiver-plot-with-matplotlib-and-jupyter-notebooks.html
# 5> Matplotlib: https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.15-Quiver-and-Stream-Plots/
# 6> Matplotlib: https://www.dkrz.de/up/services/analysis/visualization/sw/python-matplotlib/matplotlib-sourcecode/python-matplotlib-example-vector-plot

# You can also try to create your own routine
# maybe just decide a starting point and the ending point, create a df (lat,lon,v1,v2,lat_end,lon_end), then it can plot
# the length of the arrow does not really matter as long as they are consistent in unit

# And apart from plotting wind arrows, you can also use this kind of technique to add any arrows onto your maps or figures when you need to highlight something.
# It could be as simple as "plt.arrow(x=112.500-0.5, y=39.5, dx=0.5, dy=0, width=.08, color = "purple")" 

# End
###########################################################################################################################
