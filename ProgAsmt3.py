#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[3]:


a=int(input("Enter any number"))
if a<0:
    print("The number is negative")
elif a>0:
    print("The number is positive")
else:
    print("The number is 0")


# 2. Write a Python Program to Check if a Number is Odd or Even?

# In[4]:


a=int(input("Enter any number"))
if a/2==0:
    print("The number is even")
else:
    print("The numbmer is odd")


# 3. Write a Python Program to Check Leap Year?

# In[7]:


a=int(input("Enter any year"))
if a/4==0 or a/100:
    print("The year is a leap year")
else:
    print("The year is not a leap year")


# 4. Write a Python Program to Check Prime Number?

# In[13]:


num = 12
  
if num > 1:
  

    for i in range(2, int(num/2)+1):
  
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[17]:


lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




