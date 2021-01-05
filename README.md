## Python for research in atmospheric chemistry

## Contents
My notes are provided as a handy reference and focus on main topics related to our research field (some Python knowledge + data anlaysis + publishable plots + research presentations). They are not necessarily the best or only solutions to your reseach needs. 

0. Python basics
1. Numerical computation
2. Pandas dataframes
3. Data visualisation
4. Handling NetCDF files
5. Advanced Python knowledge
6. Other Python usages

## Core packages
I have introduced some useful packages in my notes here. But for any Python package, there are numerous advanced usages that I do not know. You can find dedicated tutorials online for free (webpages, pdf documents or youtube videos). 

The homepage of each Python package also provides valuable support. You can browse the "Examples" or "Gallery" to see the main applications of a package, or find the full user guide in "Documentation". Here are some examples:

0. Numpy: https://numpy.org/doc/stable/
1. Pandas: https://pandas.pydata.org/docs/user_guide/index.html#user-guide
2. Xarray: http://xarray.pydata.org/en/stable/index.html
3. Matplotlib: https://matplotlib.org/index.html#
4. Cartopy: https://scitools.org.uk/cartopy/docs/latest/index.html 

## Python tutorials
For learning Python, I recommend the tutorials below. They provide datasets with the codes, so you can run the codes and see the results from each step. For GEOS-Chem users, I particularly recommend the GEOS-Chem Python tutorial by Jiawei Zhuang. It gets you working with Python immediately.

0. Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/
1. IPython Cookbook: https://ipython-books.github.io/
2. GEOS-Chem Python: https://github.com/geoschem/GEOSChem-python-tutorial

## Suggestions for beginners
Many programming languages exist in our field. [R](https://www.r-project.org/) is good for statistics and has powerful data visualisation packages, but it gets slow or even dead when the dataset is large. It is also not very smart when handling NetCDF files. 

[Fortran](https://en.wikipedia.org/wiki/Fortran#:~:text=Fortran%20(%2F%CB%88f%C9%94%CB%90rt,numeric%20computation%20and%20scientific%20computing) is very fast, but is not good for data visualisations and many other tasks in research. The syntax is also not readable, making it harder to maintain your codes and commmunicate your issues. [Julia](https://julialang.org/) combines the speed of Fortran and the readable syntax of Python. But currently Julia is not as mature as Python, while a lot of Python packages have been well developed. 

Python is widely used in our field, you should be able to resolve all your research computing problems with Python. Python is particularly smart in handling NetCDF files which are freqently used in our research. Python has a very large user community in general, so that you can easily seek support. Once you have managed Python, you can also develop applications for almost any tasks outside our field, as it is a general-purpose programming language. 

After knowing some basics of Python, jump to Numpy and Pandas directly. Ignore anything irrelevant, see suggestions from [Jiawei Zhuang (author of GEOS-Chem Python)](https://github.com/geoschem/GEOSChem-python-tutorial#how-to-learn-python). You will be able to use Python in your research very soon! If you encounter any problems/bugs/errors, just Google them. It is very likely that you can find solutions online, particularly on stackoverflow: https://stackoverflow.com/.

You can use [Python IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) to help you edit and manage your codes: [PyCharm](https://www.jetbrains.com/pycharm/), [Spyder](https://www.spyder-ide.org/),[Jupyter Notebook](https://jupyter.org/), [JupyterLab](https://jupyter.org/), and many others exist. You can also decide not to use any of them.
