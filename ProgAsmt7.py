#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to find sum of array?

# In[2]:


arr=[11,10,18,3,96,99]
sum=0
for i in range(0,len(arr)):
    sum=sum+arr[i]
print("Sum of the array is "+str(sum))


# 2. Write a Python Program to find largest element in an array

# In[4]:


arr=[11,10,18,3,96,99]
max=arr[0]
for i in range(0,len(arr)):
    if(arr[i]>max):
        max=arr[i]
print(max)


# 3. Write a Python Program for array rotation?

# In[6]:


arr = [1, 2, 3, 4, 5];     
n = 3;    
         
print("Original array: ");    
for i in range(0, len(arr)):    
    print(arr[i]),     
    
for i in range(0, n):    
        
    first = arr[0];    
        
    for j in range(0, len(arr)-1):    
        arr[j] = arr[j+1];    
            
        
    arr[len(arr)-1] = first;    
     
print();    
     
print("Array after rotation: ");    
for i in range(0, len(arr)):    
    print(arr[i]),    


# 4. Write a Python Program to Split the array and add the first part to the end?

# In[10]:


def SplitArray(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

        arr[n-1] = x
arr = [11,10,18,3,96,99]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')


# 5. Write a Python Program to check if given array is Monotonic?

# In[8]:


def ismonotone(a):
    n=len(a) 
    if n==1:
        return True
    else:
        
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False

a= [6, 5, 4, 2]
print(ismonotone(A))


# In[ ]:




