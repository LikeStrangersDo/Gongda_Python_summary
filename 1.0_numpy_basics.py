#####################################################################################################
# Advatanges of Numpy:
# Numpy is useful for handling ND arrays, as we are dealing with spatial datasets (lat,lon,height,time,variable1,variable2), numpy is a good tool to mange
# Numpy is fast than for loops. Vectorized operations in Numpy are mapped to highly optimized C code, making them much faster than their standard Python counterparts.

# Numpy is a core package of Python
# You can visit its offical page for compreshensive understanding of numpy
# 1> for beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
# 2> advanced users: https://numpy.org/doc/stable/reference/

# And there is already a short and good visual guide to NumPy by Lev Maximov
# Original post: https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d?gi=2bf5aae3a590
# Chinese version: https://zhuanlan.zhihu.com/p/342356377
#####################################################################################################
# so here I just list some easy examples of numpy usages
import numpy as np

# array/matrix/sequence
a = np.array([1,2,3,4,5])
b = np.zeros(3,dtype=float) 
c = np.zeros((3,5),dtype=int)
d = np.full((3,5),'NA')
e = np.arange(0,20,2)
f = np.linspace(0,1,5)

print(a,b,c,d,e,f,sep="\n")
print(c.ndim,c.shape,c.size,c.dtype,end='')

# dtype is important
x = np.array([1,2,3,4,5])
x[0] = 3.14
print(x)

y = np.array([1,2,3,4,5],dtype = float)
y[0] = 3.14
print(y)

# make an empty N-d array
test = np.zeros((3,5))
#####################################################################################################
# application of numpy in our research



# End
#####################################################################
