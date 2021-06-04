##############################################################################################
##############################################################################################
# Data visualisation with Matplotlib

# Motivation:
# Matplotlib is the traditional plotting tool in Python, it may not look as fany as modern tools like "seaborn", "plotly" and "bokeh".
# But Matplotlilb was designed for making publishable figures and has been very mature. 
# Some very useful packages used in our research are actually built upon this (e.g. "seaborn", "basemap" and "cartopy").

# Getting started:
# There are two usage patterns of "matplotlib": 
# 1> the pyplot API 
# 2> the object-oriented API

# In this basic session, I am using the "pyplot" API (version 3.1.1)
# check your matplotlib version
import matplotlib
print(matplotlib.__version__)
##############################################################################################
# There are extensive online materials about Matplotlib, for example:
# https://www.matplotlib.org.cn/tutorials/#%E5%BA%8F%E8%A8%80
# https://github.com/weidafeng/python-matplotlib-practices
# https://www.cnblogs.com/devilmaycry812839668/tag/matplotlib%28Python%29/
# https://github.com/rougier/matplotlib-tutorial#introduction
# https://github.com/matplotlib/cheatsheets
# https://github.com/jbmouret/matplotlib_for_papers

# Here I just introduce two dicussed features of Matplotlib figures
##############################################################################################
# Feature 1

# by default, Matplotlib saves out png files for the highest image quality
# but if the file sizes of your figures are getting too big
# you can build a function to convert the png figures to jpeg figures
# this will may substaintially reduce the figure size while still keeping an acceptable image qualty
# just be aware that jpeg files will degrade the image quality no matter how hard you try

def png_to_jpeg(input_filename,output_filename):
    '''Input a png filename like "test.png", save out a jpeg figure like "test.jpeg"'''
    from PIL import Image
    image = Image.open(input_filename)
    image_rgb = image.convert('RGB')
    image_rgb.save(output_filename)
##############################################################################################
# Feature 2
# Matplotlib can create interactive plots, but you can also just save out a static matplotlib figure as an interactive figure using "mpld3"

# create a simple figure
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15,7.5))
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))

# save out as an interative figure (basic version)
import mpld3

html_str = mpld3.fig_to_html(fig)
Html_file= open("sample.html","w")
Html_file.write(html_str)
Html_file.close()

# save out as an interative figure (with edited style using CSS)
import mpld3
html_fragment = mpld3.fig_to_html(fig, figid = 'fig1')

# edit your style using CSS
html_doc = f'''
<style type="text/css">
div#fig1 {{ text-align: center }}
</style>

{html_fragment}
'''

Html_file= open("sample.html","w")
Html_file.write(html_doc)
Html_file.close()

# End
##############################################################################################
