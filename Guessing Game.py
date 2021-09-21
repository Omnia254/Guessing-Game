#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
number = random.randint(1, 10)

player_of_name = input("Hello, What's your name?")
number_of_guess = 0
print('okay! '+ player_of_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guess < 5:
    guess = int(input())
    number_of_guess += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guess) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))


# In[ ]:





# In[ ]:





# In[ ]:




