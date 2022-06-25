#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Find LCM?

# In[8]:


def findlcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0)and (greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm

num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
    
print("The L.C.M. is", findlcm(num1, num2))


# 2. Write a Python Program to Find HCF?

# In[10]:


def findhcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
    
print("The L.C.M. is", findhcf(num1, num2))


# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[11]:


num = int(input("Enter num"))

print("The decimal value of", num, "is:")
print(bin(num), "in binary.")
print(oct(num), "in octal.")
print(hex(num), "in hexadecimal.")


# 4. Write a Python Program To Find ASCII value of a character?

# In[12]:


c = 'd'
print("The ASCII value of '" + c + "' is", ord(c))


# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[ ]:


def sumfunc(x,y):
   
    return x+y

def difffunc(x,y):
    
    return x-y

def mulfunc(x,y):
    
    return x*y

def divfunc(x,y):
    
    return x/y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice=input("Enter your choice")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice=='1':
            print(num1,'+', num2,'=',sumfunc(num1,num2))
            #print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice=='2':
            print(difffunc(num1,num2))
            
        elif choice=='3':
            print(mulfunc(num1,num2))
            
        elif choice=='4':
            print(divfunc(num1,num2))
            
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
             break
            
    else:
            print("Enter valid choice")
            
            

    


# In[ ]:




