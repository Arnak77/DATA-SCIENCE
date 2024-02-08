#!/usr/bin/env python
# coding: utf-8

# # File Management
# 

# ### Python has several built-in modules and functions for creating,reading, updating and deleting files.
# 

# ![image-2.png](attachment:image-2.png)

# # Open File
# 

# In[115]:


fileobj = open('test1.txt') # Open file in read/text mode


# In[116]:


fileobj = open('test1.txt', 'r') # Open file in read mode


# In[117]:


fileobj = open('test1.txt', 'w') # Open file in write mode


# In[118]:


fileobj = open('test1.txt', 'a') # Open file in append mode


# # Close File
# 

# In[119]:


fileobj.close()


# # Read File
# 

# In[120]:


fileobj = open('test1.txt') 


# In[122]:


fileobj.read() #Read whole file


# In[123]:


fileobj.read() #File cursor is already at the end of the file so it won't be able


# In[124]:


fileobj.seek(0) # Bring file cursor to initial position.
fileobj.read() 


# In[125]:


fileobj.seek(7) # place file cursor at loc 7
fileobj.read()


# In[126]:


fileobj.seek(0)
fileobj.read(16) # Return the first 16 characters of the file


# In[127]:


fileobj.tell() # Get the file cursor position


# In[128]:


fileobj.seek(0)
print(fileobj.readline()) # Read first line of a file.
print(fileobj.readline()) # Read second line of a file.
print(fileobj.readline()) # Read third line of a file.


# In[129]:


fileobj.seek(0)
fileobj.readlines() # Read all lines of a file. 


# In[130]:


# Read first 5 lines of a file using readline()
fileobj.seek(0)
count = 0
for i in range(5):
    if (count < 5):
        print(fileobj.readline())
    else:
        break
    count+=1


# # Write File
# 

# In[131]:


fileobj = open('test1.txt', 'a')
fileobj.write('THIS IS THE NEW CONTENT APPENDED IN THE FILE') # Append content to
fileobj.close()
fileobj = open('test1.txt')
fileobj.read()


# In[132]:


# Open the file "test1.txt" in 'write' mode
fileobj = open("test1.txt", "w")

fileobj.write("NEW CONTENT ADDED IN THE FILE. PREVIOUS CONTENT HAS BEEN OVERWRITTEN")

fileobj.close()

fileobj = open('test1.txt')

file_contents = fileobj.read()

fileobj.close()


print(file_contents)


# In[ ]:





# In[133]:


fileobj = open("test2.txt", "w") # Create a new file
fileobj.write("First Line\n")
fileobj.write("Second Line\n")
fileobj.write("Third Line\n")
fileobj.write("Fourth Line\n")
fileobj.write("Fifth Line\n")
fileobj.close()
fileobj = open('test2.txt')
fileobj.readlines()


# # Error & Exception Handling
# 

# - Python has many built-in exceptions (ArithmeticError, ZeroDivisionError, EOFError, IndexError,
# KeyError, SyntaxError, IndentationError, FileNotFoundError etc) that are raised when your
# program encounters an error
# - When the exception occurs Python interpreter stops the current process and passes it to the
# calling process until it is handled. If exception is not handled the program will crash.
# - Exceptions in python can be handled using a try statement. The try block lets you test a block
# of code for errors.
# - The block of code which can raise an exception is placed inside the try clause. The code that
# will handle the exceptions is written in the except clause.
# - The finally code block will execute regardless of the result of the try and except blocks.
# - We can also use the else keyword to define a block of code to be executed if no exceptions
# were raised.
# - Python also allows us to create our own exceptions that can be raised from the program using
# the raise keyword and caught using the except clause. We can define what kind of error to
# raise, and the text to print to the user.

# # ![image.png](attachment:image.png)

# In[134]:


import sys  # Import the sys module

try:
    print(100/0)  # ZeroDivisionError will be encountered here
except:
    print(sys.exc_info()[1], 'Exception occurred')  # This statement will be executed
else:
    print('No exception occurred')  # This will be skipped as code block inside try raises an exception
finally:
    print('Run this block of code always')  # This will be always executed


# In[135]:


try:
    print(x) # NameError exception will be encountered as variable x is not defi
except:
    print('Variable x is not defined')


# In[136]:


try:
    os.remove("test3.txt") # FileNotFoundError will be encountered as "test3.txt"

except: # Below statement will be executed as exception occur
    print("BELOW EXCEPTION OCCURED")
    print(sys.exc_info()[1])

else:
    print('\nNo exception occurred')
finally:
    print('\nRun this block of code always')


# In[137]:


import os  # Import the os module

try:
    x = int(input('Enter first number: ')) 
    y = int(input('Enter second number: '))  
    print(x / y)  
    os.remove("test3.txt")  
except NameError:
    print('NameError exception occurred') 
except FileNotFoundError:
    print('FileNotFoundError exception occurred') 
except ZeroDivisionError:
    print('ZeroDivisionError exception occurred')  
finally:
    print('This block always executes')  
    
    


# In[138]:


# Handling specific exceptions
try:
    x = int(input('Enter first number :- '))
    y = int(input('Enter first number :- ')) # If the input entered is zero the
    print(x/y)
    os.remove("test3.txt")
except NameError:
    print('NameError exception occurred')
except FileNotFoundError:
    print('FileNotFoundError exception occurred')

except ZeroDivisionError:
    print('ZeroDivisionError exception occurred') 


# In[139]:


try:
    x = int(input('Enter first number :- '))
    if x > 50:
        raise ValueError(x) # If value of x is greater than 50 ValueError excepti
except:
    print(sys.exc_info()[0])


# # Built-in Exceptions
# 

# In[140]:


# OverflowError - This exception is raised when the result of a numeric calculati
try:
    import math
    print(math.exp(1000))
except OverflowError:
    print (sys.exc_info())
else:
    print ("Success, no error!")


# In[141]:


# ZeroDivisionError - This exception is raised when the second operator in a divi
try:
    x = int(input('Enter first number :- '))
    y = int(input('Enter first number :- '))
    print(x/y)

except ZeroDivisionError:
    print('ZeroDivisionError exception occurred')


# In[142]:


# NameError - This exception is raised when a variable does not exist
try:
    print(x1)
except NameError:
    print('NameError exception occurred')


# In[143]:


# AssertionError - This exception is raised when an assert statement fails
try:
    a = 50
    b = "Raj"
    assert a == b
except AssertionError:
    print ("Assertion Exception Raised.")


# In[144]:


# ModuleNotFoundError - This exception is raised when an imported module does not
try:
    import MyModule
except ModuleNotFoundError:
    print ("ModuleNotFoundError Exception Raised.")


# In[145]:


# KeyError - This exception is raised when key does not exist in a dictionary
try:
    mydict = {1:'Asif', 2:'Basit', 3:'Michael'}
    print (mydict[4])
except KeyError:
    print ("KeyError Exception Raised.")


# In[146]:


# IndexError - This exception is raised when an index of a sequence does not exis
try:
    mylist = [1,2,3,4,5,6]
    print (mylist[10])
except IndexError:
    print ("IndexError Exception Raised.")


# In[147]:


# TypeError - This exception is raised when two different datatypes are combined
try:
    a = 50
    b = "Asif"
    c = a/b
except TypeError:
    print ("TypeError Exception Raised.")


# In[148]:


# AttributeError: - This exception is raised when attribute reference or assignme
try:
    a = 10
    b = a.upper()
    print(b)
except AttributeError:
    print ("AttributeError Exception Raised.")


# In[ ]:


try:
    x = input('Enter first number :- ')

except:
    print('ZeroDivisionError exception occurred')


# # END

# In[ ]:




