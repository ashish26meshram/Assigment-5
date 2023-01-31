#!/usr/bin/env python
# coding: utf-8

# # Challenge 1

# In[1]:


class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return ((self.x*self.x)+(self.y*self.y)+(self.z*self.z))
    
a=Point(1,3,5)
a.sqSum()


# # Challenge 2

# In[2]:


class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return (self.num1+self.num2)
    
    def subtract(self):
        return (self.num2-self.num1)
    
    def multiply(self):
         return (self.num1*self.num2)
        
    def divide(self):
        return (self.num2/self.num1)
    
obj=Calculator(10, 94)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())


# # Challenge 3

# In[3]:


class Student:
    __name=None
    __RollNumber=None

    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setRollNumber(self,RollNumber):
        self.__RollNumber = RollNumber
    
    def getRollNumber(self):
        return self.__RollNumber
    
x=Student()
x.setName("amit")
x.setRollNumber(45)
print("student name is",x.getName())
print("student RollNumber is",x.getRollNumber())


# # Challenge 4:

# In[4]:


class Account: 
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
        
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


obj1 = SavingsAccount("Ashish", 5000)
print("Initial Balance:", obj1.getBalance())

obj2 = SavingsAccount("Ashish", 5000, 5)
print("Interest on current balance:", obj2.interestAmount())


# # Challenge 5

# In[5]:


class Account: 
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def getBalance(self):
        return self.balance


obj1 = SavingsAccount("Ashish", 2000, 5)
print("Initial Balance:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())


# In[6]:


def withdrawal(self, amount):
     self.balance = self.balance - amount
     
obj1 = SavingsAccount("Ashish", 2000, 5)
print("Initial Balance:", obj1.getBalance())
obj1.withdrawal(500)
print("Balance after withdrawal:", obj1.getBalance())


# In[7]:


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate / 100)
    
obj1 = SavingsAccount("Ashish", 2000, 5)    
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())

