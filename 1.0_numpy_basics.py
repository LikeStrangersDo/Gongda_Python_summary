Numpy link: https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650806164&idx=4&sn=bc030176ad053d9e713305c0f63484ad&chksm=84e5d3eab3925afceb58e893993187148724d18cb9cd7e905fc168794e8a56d39895c99028a2&mpshare=1&srcid=0106Ymfy9rHsbW3Ukq7PjtXs&sharer_sharetime=1609911562958&sharer_shareid=6daf80879e907bb0c12fdedb7dc18303&from=timeline&scene=2&subscene=2&clicktime=1612370524&enterid=1612370524&ascene=2&devicetype=android-26&version=27001140&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=AXmsOwnVMzY0dbQA3tumrOk%3D&pass_ticket=LjHzAcOzyuZAdfNsLL%2FYqstIuXMBhrMt6KdrfaW61l3Z1zfeiEEzediX%2BJpMwuTZ&wx_header=1

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
