#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Find the Factorial of a Number?

# In[6]:


num=int(input("enter any number to find factorial"))
fact=1
if num<0:
    print("Sorry factorial can't be found for a number less than 0")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of" ,num, "is " , fact)


# 2. Write a Python Program to Display the multiplication Table?

# In[12]:


num=int(input("Enter any number for it's table"))

if num<=0:
    print("Sorry! Please enter a positive number")
else:
    for i in range(1,11):
        print(num, 'x', i, '=', num*i)


# 3. Write a Python Program to Print the Fibonacci sequence?

# In[16]:


nterms = int(input("How many terms? "))


n1, n2 = 0, 1
count = 0


if nterms <= 0:
       print("Please enter a positive integer")

elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
    
else:
    print("Fibonacci sequence:")
    while count < nterms:
           print(n1)
           last = n1 + n2
           n1=n2
           n2 = last
           count += 1


# 4. Write a Python Program to Check Armstrong Number?

# In[19]:


num= int(input("Enter any number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print("The number is armstrong number")
else:
    print("The number is not an armstrong number")


# 5. Write a Python Program to Find Armstrong Number in an Interval?

# In[1]:


lower=int(input("Enter the lower value"))
upper=int(input("Enter the upper value"))

for num in range(lower,upper+1):
     order=len(str(num))
     #print(order)
     sum=0
     temp=num
     while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
     if num==sum:
        print(num)


# 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[4]:



num = int(input("Sum of natural numbers up to "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
  
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[ ]:




