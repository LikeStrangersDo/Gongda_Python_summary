#####################################################################################################
# Here I just gather some tips on using Python

# The Ipython Jupyter Notebook can be adjusted for better user experience
# for example: set the width of Jupyter Notebook
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

# some good practice while using Python:
# 1> create new environment: conda env create -f environment
# 2> address package dependencies: recursive testing
# 3> share evironment with collegues: keep record of project packages using YAML file
# 4> version control: Github, Gitlab, Bitbucket
# 5> containerize/orchestration production codes: Docker, Kubernetes
# 6> also see the workshop led by John Roberts: https://maraisresearchgroup.co.uk/Presentations/JRoberts-Anatomy-of-Python.pdf

# apart from the conventional "python your_script.py", you can use "pypy" to speed up the process
# homepage of PyPy: https://doc.pypy.org/en/latest/introduction.html
# but currently PyPy is only available for Python 3.7

# For Python users, it is easy to pick up Julia
# Julia is much faster than Python, and is built for handling large datasets in climate sciences, machine learning applications and more
# The major reason for not learning Julia right now may be that Python is currently much more mature than Julia
# Anyway, I plan to work on this and expect to have a Julia page in some time
# https://towardsdatascience.com/how-to-learn-julia-when-you-already-know-python-641ed02b3fa7
# https://sunscrapers.com/blog/the-quickest-introduction-to-julia-for-pythonistas/

# Although this sounds not very necessary, but you can call Python in R
# https://rstudio.github.io/reticulate/

# End
#####################################################################################################
