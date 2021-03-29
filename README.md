## Python for research in atmospheric chemistry

## My notes
My [Python](https://www.python.org/) notes focus on usages related to our research (data anlaysis + data visualisations + some small tools). They are based on my knowlege of Python, so they are not necessarily the best or only solutions to your research needs. I have introduced some Python packages here, but there are numerous usages that I do not know. For Python or any specific package, you should be able to find dedicated tutorials online.

The contents are organised as follows:
0. Python basics
1. Numerical computation
2. Pandas dataframes
3. Data visualisation
4. Handling NetCDF files
5. Advanced Python knowledge
6. Other Python usages

## Python tutorials
To learn Python for research computing, I recommend [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) and [IPython Cookbook](https://ipython-books.github.io/). For GEOS-Chem users, I strongly recommend the [Python/xarray tutorial for GEOS-Chem users](https://github.com/geoschem/GEOSChem-python-tutorial) by Jiawei Zhuang, and the [GCPy package](https://github.com/geoschem/gcpy) provided by GEOS-Chem team. 

## Suggestions for beginners
Many programming languages exist in our field. [R](https://www.r-project.org/) is good for statistics, but it is slow for large datasets. [Fortran](https://en.wikipedia.org/wiki/Fortran) is fast for processing massive data, but it is not suitable for many other tasks, like data visualisations. [Julia](https://julialang.org/) is designed for high performance scientific computing and is getting popular. But currently it is not as mature as Python. [Click here](https://github.com/geoschem/GEOSChem-python-tutorial#why-python) to see more about the comparisons between Python and other programming languages (e.g. IDL, NCL and MATLAB).

Python is widely used in our field, you should be able to resolve all your research computing problems with it. Python is particularly smart in handling NetCDF files which are freqently used in our research. Python has a very large user community in general, so that you can easily seek support. If you encounter any problems/bugs/errors, just Google them. It is very likely that you can find solutions online, particularly on [Stack Overflow](https://stackoverflow.com/). Once you have managed Python, you can also develop applications for tasks outside our research field, as it is a general-purpose programming language. 

To learn Python, I suggest you to jump to Numpy and Pandas right after knowing some Python basics. Ignore anything irrelevant, you will be able to use Python to do your research very soon! Also see suggestions from [Jiawei Zhuang](https://github.com/geoschem/GEOSChem-python-tutorial#how-to-learn-python) (author of GEOS-Chem Python). You can use [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) to help you edit and maintain your codes: [PyCharm](https://www.jetbrains.com/pycharm/), [Spyder](https://www.spyder-ide.org/), [Jupyter Notebook](https://jupyter.org/), [JupyterLab](https://jupyter.org/), and many others exist. You can also decide not to use any of them. You can use Python interactively, or you can submit complete Python jobs.
