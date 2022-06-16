#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to convert kilometers to miles?

# In[2]:


a=int(input("Enter a value in kilometers"))
b=a*1000
print(b)


# 2. Write a Python program to convert Celsius to Fahrenheit?

# In[3]:


a=int(input("Enter temperature in celsius"))
b=(a*1.8)+32
print(b)


# 3. Write a Python program to display calendar?

# In[5]:


import calendar
y=int(input("Enter year"))
m=int(input("Enter month"))

print(calendar.month(y,m))


# 4. Write a Python program to solve quadratic equation?

# In[6]:


import cmath

a = 1
b = 5
c = 6


d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# 5. Write a Python program to swap two variables without temp variable?

# In[ ]:


a=int(input("Enter a value"))
b=int(input("Enter a value"))
a=a+b
b=a-b
a=a-b
print("After swapping " )
print(a)
print(b)


# In[ ]:




