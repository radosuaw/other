#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


t_0 = 0.
T = 2.
x_0 = 1.
n = 10
def f(t,x):
  return -2.*(x-np.cos(t))-np.sin(t)

#real solution
def g(t):
  return np.cos(t) 


# In[9]:


def EULER(R, n, f, t_0, T, x_0):
    h = 2./n
    R[0]=[t_0,x_0]
    for i in range (1,n+1):
      R[i]=[t_0 + i*h,R[i-1][1]+h*f(R[i-1][0]+h/2,R[i-1][1]+h/2*f(R[i-1][0],R[i-1][1]))]
    
def EULER_ERROR(n, f, g, t_0, T, x_0):
    e = np.empty(n)
    for i in range(n):
        R = np.empty(shape=(5*(2**(i+1))+1,2))
        EULER(R,5*(2**(i+1)), f, t_0, T, x_0)
        e[i]=np.abs(R[5*(2**(i+1))][1]-g(T))
    return e


# In[4]:


R = np.empty(shape=(n+1,2)) # list of nods with numerical solutions in these points
EULER(R, n, f, t_0, T, x_0)
R


# In[5]:


# zipping above values to be able to plot them along with the real solution
x,y = zip(*R)
plt.figure(figsize=(10,8))
plt.plot(x, y, label='numerical')
plt.plot(x, g(x), label='real')
plt.legend()


# In[13]:


E = EULER_ERROR(n, f, g, t_0, T, x_0)
E


# In[14]:


def HEUN(R, n, f, t_0, T, x_0):
    h = 2./n
    R[0]=[t_0,x_0]
    for i in range (1,n+1):
      R[i]=[t_0 + i*h,R[i-1][1]+0.5*h*f(R[i-1][0],R[i-1][1])+0.5*h*f(R[i-1][0]+h,R[i-1][1]+h*f(R[i-1][0],R[i-1][1]))]
    
def HEUN_ERROR(n, f, g, t_0, T, x_0):
    e = np.empty(n)
    for i in range(n):
        R = np.empty(shape=(5*(2**(i+1))+1,2))
        HEUN(R,5*(2**(i+1)), f, t_0, T, x_0)
        e[i]=np.abs(R[5*(2**(i+1))][1]-g(T))
    return e


# In[15]:


P = np.empty(shape=(n+1,2))
HEUN(P, n, f, t_0, T, x_0)
P


# In[16]:


x,y = zip(*P)
plt.figure(figsize=(10,8))
plt.plot(x, y, label='numerical')
plt.plot(x, g(x), label='real')
plt.legend()


# In[18]:


H = HEUN_ERROR(n, f, g, t_0, T, x_0)
H


# In[ ]:




