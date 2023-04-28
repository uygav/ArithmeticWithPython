#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(4*5/(7+3))


# In[3]:


print(9/(3+6)-1)


# In[7]:


b = 10 > 3*3
print(b)
print(type(b))


# In[9]:


print(4==2+2)


# In[10]:


x=2
ans = 4*x+3 < 17 - x**2
print(ans)


# In[11]:


x = 3
ans = 8*x-2 <= -3*x + 42
print(ans)


# In[13]:


x1 = 3 
x2 = 4
if x1>x2:
    print('%g is greater than %g' %(x1,x2))
elif x1<x2:
    print('%g is greater than %g' %(x2,x1))
else:
    print('%g is equal to %g' %(x1,x2))


# In[35]:


from IPython.display import display, Math
for i in range(0,4):
    for j in range (0,5):
        if i>0 and j>0:
            display(Math('%g^{-%g} = %g' %(i,j,i**-j)))
    


# In[ ]:




