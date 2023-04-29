#!/usr/bin/env python
# coding: utf-8

# In[9]:


from numpy import random 
random_number = random.randint(1,101)
print(random_number)


# In[10]:


i = 1 
while i<6:
    print(i)
    i+=1


# In[ ]:


from IPython.display import display, Math
from numpy import random 
random_number = random.randint(1,101)
def guessTheNumber():
    random_number = random.randint(1,101)
    guess_number = int(input("Guess a number between 1 and 100 :"))
    while random_number!=guess_number:
        if random_number > guess_number:
            print("guess higher!")
        elif random_number < guess_number:
            print("guess lower!")
        guess_number = int(input('Guess again :'))
    print("yes!! you guessed correctly!")
guessTheNumber()

