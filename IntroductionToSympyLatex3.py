#!/usr/bin/env python
# coding: utf-8

# In[28]:


import sympy as sym
from IPython.display import Math,display
sym.init_printing()


# In[32]:


x = sym.symbols('x')
mu,alpha,sigma = sym.symbols('mu,alpha,sigma')
# mu,alpha,sigma = sym.exp('mu,alpha,sigma')
expr = sym.exp((mu-alpha)**2 / (2*sigma**2)) # exp = exponential
print(expr)
display(expr)


# In[31]:


hello = sym.symbols('hello')
hello
hello / 3
print(hello / 3)
display(hello / 3)


# In[41]:


x = sym.symbols('x')
expr = x + 4
print(expr)
display(expr)
print(expr.subs(x,6))
display(expr.subs(x,6))


# In[49]:


x,y = sym.symbols('x,y')
expr = x + 4 + 2*y
expr.subs(x,-4)


# In[50]:


expr.subs({x:-4,y:3})


# In[ ]:




