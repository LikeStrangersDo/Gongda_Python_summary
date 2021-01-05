## Python for research in atmospheric chemistry

## Contents
My notes are provided as a handy reference and focus on Python usages related to our research (data anlaysis + publishable plots + research presentations + some small tools). These are based on my knowlege of Python, so they are not necessarily the best or only solutions to your reseach needs. 

0. Python basics
1. Numerical computation
2. Pandas dataframes
3. Data visualisation
4. Handling NetCDF files
5. Advanced Python knowledge
6. Other Python usages

## Core packages
I have introduced some packages that are useful to our research. But there are numerous usages that I do not know. For any package, you should be able to find dedicated tutorials online for free (webpages, pdf documents or youtube videos). The homepage of each Python package also provides valuable support. You can browse the "Examples" or "Gallery" to see the main applications of a package, or find the full user guide in "Documentation". Here are some examples:

0. Numpy: https://numpy.org/doc/stable/
1. Pandas: https://pandas.pydata.org/docs/user_guide/index.html#user-guide
2. Xarray: http://xarray.pydata.org/en/stable/index.html
3. Matplotlib: https://matplotlib.org/index.html#
4. Cartopy: https://scitools.org.uk/cartopy/docs/latest/index.html 

## Python tutorials
For learning Python, I recommend the tutorials below. For GEOS-Chem users, I particularly recommend the GEOS-Chem Python tutorial by Jiawei Zhuang. You may be able to use Python to process GEOS-Chem model outputs in 1 or 2 days.

0. Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/
1. IPython Cookbook: https://ipython-books.github.io/
2. GEOS-Chem Python: https://github.com/geoschem/GEOSChem-python-tutorial

## Suggestions for beginners
Many programming languages exist in our field. [R](https://www.r-project.org/) is good for statistics, but it gets slow when the dataset is large. [Fortran](https://en.wikipedia.org/wiki/Fortran) is fast, but is not suitable for many other tasks in research, like data visualisations. [Julia](https://julialang.org/) is designed for high performance in research computing and is getting popular. But currently it is not as mature as Python. You can see more about the comparison between Python and other programming languages like IDL, NCL and MATLAB [here](https://github.com/geoschem/GEOSChem-python-tutorial#why-python). 

[Python](https://www.python.org/) is widely used in our field, you should be able to resolve all your research computing problems with Python. Python is particularly smart in handling NetCDF files which are freqently used in our research. Python has a very large user community in general, so that you can easily seek support. If you encounter any problems/bugs/errors, just Google them. It is very likely that you can find solutions online, particularly on [Stack Overflow](https://stackoverflow.com/). Once you have managed Python, you can also develop applications for tasks outside our field, as it is a general-purpose programming language. 

After knowing some basics of Python, jump to Numpy and Pandas directly. Ignore anything irrelevant, see suggestions from [Jiawei Zhuang](https://github.com/geoschem/GEOSChem-python-tutorial#how-to-learn-python) (author of GEOS-Chem Python). You will be able to use Python in your research very soon! You can use [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) to help you edit and maintain your codes: [PyCharm](https://www.jetbrains.com/pycharm/), [Spyder](https://www.spyder-ide.org/),[Jupyter Notebook](https://jupyter.org/), [JupyterLab](https://jupyter.org/), and many others exist. You can also decide not to use any of them.
