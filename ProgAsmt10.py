#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to find sum of elements in list?

# In[13]:


l=[11,18,3,10,99,96]
suml=0

for i in range(0,len(l)):
    suml=suml+l[i]
print(suml)


# 2. Write a Python program to Multiply all numbers in the list?

# In[17]:


l=[11,18,3,10,99,96]
mul=1

for i in range(0,len(l)):
    mul=mul*l[i]
print(mul)


# 3. Write a Python program to find smallest number in a list?

# In[20]:


l=[11,18,3,10,99,96]
smallest=l[0]
for i in range(0,len(l)):
    if (smallest>l[i]):
        smallest=l[i]
        i=i+1
print(smallest)


# 4. Write a Python program to find largest number in a list?

# In[22]:


l=[11,18,3,10,99,96]
largest=l[0]
for i in range(0,len(l)):
    if (largest<l[i]):
        largest=l[i]
        i=i+1
print(largest)


# 5. Write a Python program to find second largest number in a list?

# In[27]:


l=[11,18,3,10,99,96]

l.sort()
print(l[-2])
    


# 6. Write a Python program to find N largest elements from a list?

# In[30]:


num=int(input("Enter the number of largest elements to be printed"))
l=[2343,65,76,324,76,34,632,54,65,2,3,643,635,3,546,45235314,665,5]
l.sort()
print(l[len(l)-num:])


# 7. Write a Python program to print even numbers in a list?

# In[39]:


l=[11,18,3,10,99,96]
for i in range(0,len(l)):
    if ((l[i]%2)==0):
        print(l[i])


# 8. Write a Python program to print odd numbers in a List?

# In[40]:


l=[11,18,3,10,99,96]
for i in range(0,len(l)):
    if ((l[i]%2)!=0):
        print(l[i])


# 9. Write a Python program to Remove empty List from List?

# In[59]:


l=[234235,5,236,2,[],546,[]]
l1=[]
for i in range(0,len(l)):
    if l[i]!=[]:
        l1.append(l[i])
        i=i+1
        
print(l1)
        


# 10. Write a Python program to Cloning or Copying a list?

# In[69]:


l=[11,18,3,10,99,96]
print("Input list ",l)
l1=[]

l1=l[:]
print("Copied list ",l1)


# In[ ]:




