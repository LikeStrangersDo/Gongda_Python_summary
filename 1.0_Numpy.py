#####################################################################
# Numpy

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


# End
#####################################################################
