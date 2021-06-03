## Python for research computing in atmopsheric/envirnomental/earth sciences
My Python notes focus on usages in research computing for atmopsheric/envirnomental/earth sciences. However, they are not necessarily the best solutions to your specific research needs, as I have my own preferences and there are many Python usages that I actually do not know.

0. Basics
1. Numpy
2. Pandas
3. Data visualisation
4. NetCDF files
5. Advanced Python
6. Small Python tools

## Python tutorials
To learn Python for research computing, I recommend [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) and [IPython Cookbook](https://ipython-books.github.io/). To get started with handling NetCDF files, I strongly recommend the [Python/xarray tutorial for GEOS-Chem users](https://github.com/geoschem/GEOSChem-python-tutorial) by Jiawei Zhuang. For GEOS-Chem users, there is also the [GCPy package](https://github.com/geoschem/gcpy) provided by GEOS-Chem team. 

## Suggestions for beginners
Python is widely used in our field, as it has a few [advantanges over other programming languages](https://github.com/geoschem/GEOSChem-python-tutorial#why-python). Python is particularly smart in handling NetCDF files which are freqently used in our research. You should be able to resolve all your research computing problems using Python. And there is a very large Python user community so that you can easily seek support. Just Google your problems/bugs/errors, you will probably find existing solutions online, particularly on [Stack Overflow](https://stackoverflow.com/). There are more benifits of managing Python, for example, it is very easy for a Python user to pick up other powerful research computing languages like [Julia](https://julialang.org/).

Regarding research computing, I suggest you to jump to Numpy and Pandas right after knowing some Python basics. Ignore anything irrelevant, then you should be able to use Python in your research very soon (Also see suggestions from [Jiawei Zhuang](https://github.com/geoschem/GEOSChem-python-tutorial#how-to-learn-python)). You can use [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) to help you edit and maintain your codes: [PyCharm](https://www.jetbrains.com/pycharm/), [Spyder](https://www.spyder-ide.org/), [Jupyter Notebook](https://jupyter.org/), [JupyterLab](https://jupyter.org/), and many others. You can also decide not to use any of them. You can use Python interactively, or you can submit Python jobs via complete scripts.
