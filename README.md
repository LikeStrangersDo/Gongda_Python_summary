## Python for research in atmospheric chemistry

## Contents
My notes are provided as a handy reference. They are not necessarily the best or only solutions to your reseach needs.

0. Python basics
1. Numerical computation
2. Pandas dataframes
3. Data visualisation
4. Handling NetCDF files
5. Advanced Python knowledge
6. Other Python usages

## Python tutorials
For learning Python, I recommend the tutorials below. They provide datasets with the codes, so you can run the codes and see the results from each step. For GEOS-Chem users, I particularly recommend the GEOS-Chem Python tutorial by Jiawei Zhuang. It gets you working with Python immediately.

0. Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/
1. IPython Cookbook: https://ipython-books.github.io/
2. GEOS-Chem Python: https://github.com/geoschem/GEOSChem-python-tutorial

## Core packages
 Here I list some of the Python packages frequently used in our research. For any package, instructions are always available on its homepage. You can browse the "Examples" or "Gallery" to see the main applications of a package, or find the full user guide in "Documentation".

0. Numpy: https://numpy.org/doc/stable/
1. Pandas: https://pandas.pydata.org/docs/user_guide/index.html#user-guide
2. Xarray: http://xarray.pydata.org/en/stable/index.html
3. Matplotlib: https://matplotlib.org/index.html#
4. Cartopy: https://scitools.org.uk/cartopy/docs/latest/index.html 

## Suggestions for beginners
You may wonder "Why Python"? There are a lot of discussions on the programming languages. In my view, it is worth focusing on Python, because you should be able to resolve all your problems in research computing in atmopsheric chemistry with Python. You can also develop applications in other research/non-research fields using Python, as it is a general-purpose programming language. Python is not perfect, it is faster than R, while still a lot slower than languages like C and Fortran. But languages like C and Fortran are not good for data visualsations and many other tasks in research. They are also not readable, so it is harder to maintain your codes and commmunicate your issues. Julia is a new language which combines the speed of Fortran and the readable syntax of Python. But currently Julia is not as mature as Python, while a lot of packages have been well developed in Python. Python is particularly smart in handling NetCDF files which are freqently used in our research.

After knowing some basics of Python, jump to Numpy and Pandas directly. Ignore anything irrelevant, see suggestions from [Jiawei Zhuang (author of GEOS-Chem Python)](https://github.com/geoschem/GEOSChem-python-tutorial#how-to-learn-python). You will be able to use Python in your research very soon! If you encounter any problems/bugs/errors, just Google them. It is very likely that you can find solutions online, particularly on stackoverflow: https://stackoverflow.com/.

You can use [Python IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) to help you edit and manage your codes: [PyCharm](https://www.jetbrains.com/pycharm/), [Spyder](https://www.spyder-ide.org/),[Jupyter Notebook](https://jupyter.org/), [JupyterLab](https://jupyter.org/), and many others exist. You can also decide not to use any of them.
