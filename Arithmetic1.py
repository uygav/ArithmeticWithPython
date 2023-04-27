#!/usr/bin/env python
# coding: utf-8

# In[12]:


from IPython.display import display, Math
display('4+3=7')
display('4+3 =' + str(4+3))
display(Math('4+3=7'))


# In[25]:


x=4
y=3
display(Math(str(4+3==4+3)))
display(Math(str(4+3)))
display(Math(str(4)+str(3)))
display(Math(str(4)+ " + " + str(3) + " = " + str(4+3)))


# In[26]:


display(Math('%g + %g = %g' %(x,y,x+y)))


# In[31]:


display(Math('4/5=.8'))


# In[33]:


display(Math('\\frac{4}{5} = .8'))


# In[40]:


x= 3.4
y= 17
display(Math('%g \\times %g = %g' %(x,y,x*y)))
display(Math('%g . %g = %g' %(x,y,x*y)))
display(('%g \\times %g = %g' %(x,y,x*y)))
display(Math('%g X %g = %g' %(x,y,x*y)))


# In[59]:


x = 7 
y = -2
z = 5
ans = 3*x*(4+y)
display(Math('3 \\times %g(4  %g) = %g' %(x,y,ans)))
display(Math('3x(4 + y) = %g' %ans))


# In[60]:


ans = -y-((x+3)/(z))
display(Math('-%g- \\frac{%g+3}{%g} = %g' %(y,x,z,ans)))
display(Math('-y- \\frac{x+3}{z} = %g' %ans))

