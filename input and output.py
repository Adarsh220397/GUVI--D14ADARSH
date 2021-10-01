#!/usr/bin/env python
# coding: utf-8

# # Write a code to get the input in the given format and print the output in the given format.
# 
# Input Description:
# A single line contains a string.
# 
# Output Description:
# Print the characters in a string separated by line.
# 
# Sample Input :
# guvigeek
# Sample Output :
# g
# u
# v
# i
# g
# e
# e
# k
# 
# 
# 
# 
# 

# In[1]:



x= input()

for i in range(0,len(x)):

    print(x[i])


# Write a code to get the input in the given format and print the output in the given format.
# 
# Input Description:
# A single line contains three float values separated by space.
# 
# Output Description:
# Print the float value separated by line.
# 
# Sample Input :
# 2.3 4.5 7.8
# Sample Output :
# 2.3
# 4.5
# 7.8

# In[2]:


import sys

for line in sys.stdin:
    a = line.split()
    print (*a, sep="\n")
    


# Write a code to get the input in the given format and print the output in the given format
# 
# Input Description:
# A single line contains a string.
# 
# Output Description:
# Print the characters in a string separated by space.
# 
# Sample Input :
# guvi
# Sample Output :
# g u v i

# In[3]:


a = input()
b = len(a)
for i in range(0,b-1) :
    print(a[i], end = ' ')
    
print(a[b-1])


# Write a code to get the input in the given format and print the output in the given format
# 
# Input Description:
# First-line indicates two integers separated by space. Second-line indicates three integers separated by space. Third-line indicates three integers separated by space
# 
# Output Description:
# Print the input in the same format.
# 
# Sample Input :
# 2 5
# 2 5 6
# 2 4 5
# Sample Output :
# 2 5
# 2 5 6
# 2 4 5

# In[4]:


x = str(input())
y = str(input())
z = str(input())

print(x)
print(y)
print(z)


# Write a code to get the input in the given format and print the output in the given format
# 
# Input Description:
# Three integers are given in line by line.
# 
# Output Description:
# Print the integers in a single line separate by space.
# 
# Sample Input :
# 2
# 4
# 5
# Sample Output :
# 2 4 5

# In[5]:


x = int(input())
y = int(input())
z = int(input())

print(x,y,z)


# Write a code to get the input in the given format and print the output in the given format
# 
# Input Description:
# First-line indicates two integers separated by space. Second-line indicates two integers separated by space. Third-line indicates two integers separated by space.
# 
# Output Description:
# Print the input in the same format.
# 
# Sample Input :
# 2 4
# 2 4
# 2 4
# Sample Output :
# 2 4
# 2 4
# 2 4

# In[6]:


x = str(input())
y = str(input())
z = str(input())

print(x)
print(y)
print(z)


# Write a code to get the input in the given format and print the output in the given format.
# 
# Input Description:
# First-line indicates two integers which are the size of array and 'K' value. Second-line indicates an integer contains elements of an array.
# 
# Output Description:
# Print the taken input in the same format.
# 
# Sample Input :
# 5 3
# 1 2 3 4 5
# Sample Output :
# 5 3
# 1 2 3 4 5

# In[7]:


x = str(input())
y = str(input())

print(x)
print(y)


# Write a code to get the input in the given format and print the output in the given format
# 
# Input Description:
# A single line contains integers separated by space
# 
# Output Description:
# Print the integer list of integers separated by space
# 
# Sample Input :
# 2 3 4 5 6 7 8
# Sample Output :
# 2 3 4 5 6 7 8

# In[8]:


x = input()
print(x)


# In[ ]:





# In[ ]:




