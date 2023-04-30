#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sympy as sym
import numpy as np
sym.init_printing()
from IPython.display import display


# In[19]:


x,y = sym.symbols('x,y')


# In[22]:


print(x)
x


# In[23]:


print(y)
y


# In[15]:


print(z)


# In[16]:


print(x**y)
display(x**y)


# In[18]:


display(np.sqrt(2))
display(sym.sqrt(2))


# In[27]:


display(y*x**2)
display(sym.sqrt(4)*x)
display(sym.sqrt(x)*sym.sqrt(x))


# In[ ]:




