#!/usr/bin/env python
# coding: utf-8

# Code to create register /login /forgetpassword 

# In[ ]:


import re

def registration():
    db = open("data1.txt",'r')
    d = []
    f = []
    
    for i in db:
        a,b =i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d,f))
    
    name      = input("create username/EmailId :")
    if name in d:                  #changed db to d
        print("Username exists in db")
        print("You are registered")
        registration()
    elif not name[0].isalpha() or'@'not in name or " " not in name or '@.' in name:
        print("Invalid username/EmailId")
        registration()
        
    password  = input("create password :")
    password1  = input("Confirm password :")
    if password != password1:
        print("Password does not match, restart")
        registration()
    elif len(password) <= 6 :
        print("password too short,restart")
        registration() 
    elif len(password) > 16 :
        print("password too long,restart")
        registration()
    elif not re.search("[A-Z]",password) or not re.search("[a-z]",password) or not re.search("[0-9]",password):
        print("Type the required keys")
    else:
        db = open("data1.txt","a")
        db.write(name +", "+ password+"\n")
        print("Success!")
        
def forget_password():
    
    db = open("data1.txt",'r')
    d = []
    f = []
    
    for i in db:
        a,b =i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d,f)) 
    name = input("create username/EmailId :")

def access():
    
    db = open("data1.txt",'r')
    name     = input("Enter your username/EmailId: ")
    password = input("Enter your password: ")
    
    if  len(name or password ) > 1 :
        d = []
        f= []
        for i in db:
            a,b = i.split(", ")
            b =b.split()
            d.append(a)
            f.append(b)
            
        data =dict(zip(d, f))
        
        try:
            if data[name]:
                try:
                    if password==data[name]:
                        print("Login successful")                        
                        print("Hello !," ,name )     
                    else:
                        print("Password or username/EmailId incorrect")
                except:
                    print("Incorrect password or username/EmailId")
            else:
                print("Username/EmailId or password doesn't exist")
        except:
            print("Username/EmailId and password doesn't exist")
    else:
        print("Please enter a value")

def home(option = None):
    option = input(" Login | Signup | Forget password ")
    if option == "Login":
        access()
    elif option == "Signup":
        registration()
    elif option == 'Forget password':
        forget_password()
    else:
        print("Please enter the option")
home()


# In[ ]:




