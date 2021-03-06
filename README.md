## Python for research computing in atmopsheric sciences
My notes are mainly based on my research codes for atmospheric chemistry modeling. I have also added links to some relevant and nice online materials. These can be applied to related fields within and beyond environmental sciences. I plan to keep updating this repository in my spare time. I hope these notes will be helpful, but these are not necessarily the best solutions to your specific research computing problems.

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
Python is widely used in our field, and it has a few [advantanges over other programming languages](https://github.com/geoschem/GEOSChem-python-tutorial#why-python). Python is particularly smart in handling NetCDF files which are freqently used in our research. Python packages have been extensively developed, and there is a very large Python user community so that you can easily seek support. Just Google your problems/bugs/errors, you will probably find existing solutions online, particularly on [Stack Overflow](https://stackoverflow.com/). You should be able to resolve all your research computing problems using Python. But there are even more benifits of learning Python. For example, it is very easy for a Python user to pick up other powerful research computing languages like [Julia](https://julialang.org/).

Regarding research computing, I suggest you to jump to Numpy and Pandas right after knowing some Python basics. Ignore anything irrelevant, then you should be able to use Python in your research very soon (Also see suggestions from [Jiawei Zhuang](https://github.com/geoschem/GEOSChem-python-tutorial#how-to-learn-python)). You can use [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) to help you edit and maintain your codes: [PyCharm](https://www.jetbrains.com/pycharm/), [Spyder](https://www.spyder-ide.org/), [Jupyter Notebook](https://jupyter.org/), [JupyterLab](https://jupyter.org/), and many others. You can also decide not to use any of them. You can use Python interactively, or you can submit Python jobs via complete scripts.
