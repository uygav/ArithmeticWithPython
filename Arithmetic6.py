#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = 10 
b = 3
print(a/b)
print(int(a/b))
print(a%b) # remainder


# In[6]:


a = 10 
b = 3 
division = int(a/b)
remainder = a%b
print('%g goes into %g , %g times with a remainder of %g' %(b,a,division,remainder)
)


# In[15]:


for i in range(-5,6):
    space = " "
    if i<0:
        space = ""
    
    if i%2==0:
        print('%s%g is an even number' %(space,i))
    else:
        print('%s%g is an  odd number' %(space,i))


# In[ ]:




