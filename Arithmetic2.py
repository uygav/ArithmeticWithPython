#!/usr/bin/env python
# coding: utf-8

# In[6]:


3**2


# In[7]:


3^2


# In[8]:


x = 6
3**x


# In[9]:


print(3**3)
print(3*3*3)


# In[11]:


print(3**3 * 3**4)
print(3**(3+4))


# In[13]:


x = 9**(1/2)
y = 9**1/2
print(x)
print(y)


# In[19]:


from IPython.display import display,Math
ans = 3**3
display(Math('3^3 = 27'))
display(Math('3^3 \\times 3^4 = 3^{2+4}'))


# In[25]:


x = 5
y = 5.1
ans = (x**(3/4)) * (4**y)
display(Math('x^{3/4} \\times 4^y = %g' %ans ))


# In[35]:


ans = 3**3 / x**y
display(Math('\\frac {3^3} {x^y} = %g' %ans))


# In[37]:


ans = 10**(x-4)
display(Math('10^{x-4} = %g' %ans))


# In[ ]:




