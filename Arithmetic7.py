#!/usr/bin/env python
# coding: utf-8

# In[1]:


def firstfunc():
    print("hello")
firstfunc()


# In[2]:


def secondFunc(name):
    print("hello %s" %name)
secondFunc("uygar")


# In[3]:


a = input("input a number : ")
print(a)
print(type(a))
b = int(input("input a number : "))
print(type(b))


# In[4]:


def cumputeremainder(x,y):
    divis = int(x/y)
    remainder = x%y
    print('%g goin into %g, %g times with a remainder of %g' %(y,x,divis,remainder))
cumputeremainder(200,5)


# In[5]:


def divisionWithInput():
    x = int(input('input the numerator :'))
    y = int(input('input the denominator :'))
    divis = int(x/y)
    remainder = x%y
    print('%g goes into %g , %g times with a remainder of %g' %(y,x,divis,remainder))
divisionWithInput()    


# In[6]:


from IPython.display import display, Math
def challange1():
    space = " "
    display(Math('press 1 to compute 2^4 or 2 to compute \\frac{2}{4}'))
    x = int(input('input your choise :'))
    if x == 1:
        display(Math('2^4 = 16'))
    elif x == 2:
        display(Math('\\frac{2}{4} = 0.5'))
    else:
        print("invalid selection")
challange1()


# In[7]:


def challange2():
    space = " "
    display(Math('press \: 1 \: to \: compute \: 3^5 \: or \: 2 \: to \: compute \: \\frac{3}{5}'))
    x = int(input('input your choise :'))
    if x == 1:
        display(Math('3^5 = 243'))
    elif x == 2:
        display(Math('\\frac{3}{5} = 0.6'))
    else:
        print("invalid selection")
challange2()


# In[11]:


def powers(x,y):
    display(Math('%g^{%g} = %g' %(x,y,x**y)))
def division(x,y):
    display(Math('\\frac{%g}{%g} = %g' %(x,y,x/y)))
def mainfunction():
    x = float(input('Input X:'))
    y = float(input('Input Y:'))
    
    display(Math('\\text{Press "1" to compute }%g^{%g}\\text{or press "2" to compute }\\frac{%g}{%g}' %(x,y,x,y)))
    switch = input(' ')
    
    if switch =='1':
        powers(x,y)
    elif switch =='2':
        division(x,y)
    else:
        print('Invalid selection !')
mainfunction()


# In[ ]:




