#!/usr/bin/env python
# coding: utf-8

# In[14]:


a = -4 
b = abs(a)
print(a,b)


# In[18]:


display(Math('|-4| = 4'))


# In[20]:


x = -4.3
display(Math('|%g| = %g' %(x,abs(x))))


# In[34]:


numbers = [-4,6,-1,43,-18,2,0]

for i in numbers:
    if i <= -5 or i>2:
        print('absolute number of %g is %g' %(i,abs(i)))
    else:
        print(str(i)+' was no tested')


# In[ ]:




