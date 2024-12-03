#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def addtwonumbersr(n1,n2):
    sum1n2=n1+n2
    return(sum1n2)

num1=int(input("Enter number"))
num2=int(input("Enter number"))

result =addtwonumbersr(num1,num2)

print(f"the sum of num{num1} and num{num2} is {result}")
print(f"the square of the sum is {result **2}")

addtwonumbersr(num1,num2)


# In[ ]:


def calcnameandage():
    name = str(input("Enter Name"))
    age = int(input("Enter your age"))
    print("Your name is ",name,"and your age is ", age)
calcnameandage()


# In[ ]:


def show_employee(names=[],salary=900):
    name=str(input("Enter Name"))
    salary=int(input("Enter salary".format(salary)))

    print(name)
    print(salary)
show_employee()


# In[2]:


def show_employee(names=[], salary=900):
    name = input("Enter Name: ")
    if not name:
        name = "Unknown"
    salary_input = input("Enter salary (press Enter for default value {}): ".format(salary))
    if salary_input:
        salary = int(salary_input)
    print("Name:", name)
    print("Salary:", salary)

show_employee()


# In[ ]:




