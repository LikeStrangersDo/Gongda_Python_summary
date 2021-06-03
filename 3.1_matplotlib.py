##############################################################################################
##############################################################################################
# Data visualisation with "matplotlib"

# Motivation:
# "matplotlib" is the traditional plotting tool in Python, comparing to modern tools like "seaborn", "plotly" and "bokeh", you may find "matplotlitb" plots a bit boring.
# But "matplotlib" was initially designed for making publishable figures and has been very mature. 
# Some very useful packages used in our research are actually built upon this (e.g. "basemap", "cartopy").
# While mordern plotting tools focus more on interactive plots or Front-end web development.

# Getting started:
# There are two usage patterns of "matplotlib": 
# 1> the pyplot API 
# 2> the object-oriented API

# In this basic session, I am using the "pyplot" API (version 3.1.1)
# New features in later versions are not included here.

# However the user manual for Version 3.3.3 is much improved compared to that of 3.1.1.
##############################################################################################

# check your matplotlib version
import matplotlib
print(matplotlib.__version__)

#




# References (summarize cheatsheets pdf also)
https://www.matplotlib.org.cn/tutorials/#%E5%BA%8F%E8%A8%80
https://github.com/weidafeng/python-matplotlib-practices
https://www.cnblogs.com/devilmaycry812839668/tag/matplotlib%28Python%29/
https://github.com/rougier/matplotlib-tutorial#introduction
https://github.com/matplotlib/cheatsheets
https://github.com/jbmouret/matplotlib_for_papers

  
# summarize API method for Matplotlib 
  
# End
##############################################################################################
# Save out a static matplotlib figure as an interactive figure using "mpld3"

# create simple figure
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15,7.5))
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))

# create an interative figure (basic version)
import mpld3

html_str = mpld3.fig_to_html(fig)
Html_file= open("sample.html","w")
Html_file.write(html_str)
Html_file.close()

# create an interative figure (with edited style using CSS)
import mpld3
html_fragment = mpld3.fig_to_html(fig, figid = 'fig1')

html_doc = f'''
<style type="text/css">
div#fig1 {{ text-align: center }}
</style>

{html_fragment}
'''

Html_file= open("sample.html","w")
Html_file.write(html_doc)
Html_file.close()
##############################################################################################
