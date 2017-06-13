
# coding: utf-8

# In[2]:

import numpy
import matplotlib
from matplotlib import cm
from matplotlib.pyplot import ylim, contourf, colorbar, show
from scipy.optimize import curve_fit


# In[3]:

data= numpy.loadtxt('1605a.txt', skiprows=1)
numpy.shape(data)


# In[4]:

ix=200
iy=512
x= numpy.arange(0, 200)
y=numpy.arange(0,256,0.5)
numpy.shape(y)


# In[5]:

512*200


# In[6]:

z= numpy.zeros(ix * iy).reshape(iy, ix)


# In[20]:

k=0
for j in range(ix):
    for i in range(iy):
        z[i,j]=float(data[k,2]  )
        
        k=k+1
 


# In[25]:

ylim(255.5,0)
contourf(x,y,z,256,alpha=0.7,cmap=cm.nipy_spectral)
colorbar()
show()

# In[ ]:




# In[ ]:



