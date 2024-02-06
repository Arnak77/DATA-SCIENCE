#!/usr/bin/env python
# coding: utf-8

# # Function in Python

# In[1]:


def greet():
    print("hello")
    print("good morning ")
greet()# when we run the code we havent got any output     


# In[2]:


def greet():
    print('hello')
    print('good morning')
greet() #if you need call multiple times 


# In[3]:


def greet():
    print('hello')
    print('good morning')
greet() #if you need call multiple times 

def greet():
    print('hello')
    print('good morning')
greet() #if you need call multiple times 


# In[4]:


def greet():
    print('hello')
    print('good noon')
greet()

greet()


# In[5]:


def add(x,y):
    c=x+y
    print("add=",c)
add(12,23)    


# In[6]:


def greet():
    print('hello')
    print('good noon')
greet()

def add(x,y):
    c=x+y
    print(c)
add(5,4)
# you can create mutliple function and call them as many time as you want


# In[7]:


def greet():
    print('hello')
    print('good noon')
    
def add(x,y):
    c=x+y
    print(c)
    
greet()    
add(15,4)
# you can create mutliple function and call them as many time as you want


# In[12]:


def greet():
    print("hello")
    print("good noon")
    
def add(x,y):
    c=x+y
    return c
    
greet()
result=add(4,7)
print(result)


# as a function we have 2 choice

# #### 1- whenever we call the function . function is do the task for you greet() & add()
# 
# 
# #### 2- we have another type of function it will return you the value.

# In[13]:


def add_sub(x,y): # what if i want to return 2 values add_sub & i want to return 2 values & function can accept multiple value 
    c= x+y
    d= x-y
    return c, d

result = add_sub(4,5)
print(result)
#print(type(result))


# In[15]:


def add_sub(x,y):
    c= x+y
    d= x-y
    return c, d

result = add_sub(4,5)
print(result)
print(type(result))


# In[16]:


def add_sub(x,y):
    c= x+y
    d= x-y
    return c, d

result1,result2= add_sub(5,4)
print(result1,result2)
print(type(result1))
print(type(result2))


# In[17]:


a,b = 6


#  - function are always reuseable
# 
# - in one code you can write multiple function as well

# # Function Arguments

# - FUNCTION ARGUMENT.
#  
# - How to pass parameter to a function & what happend to the variable when you pass to a function & if you modify the value then what happen.
# 
# - every code check with debug.

# In[19]:


def update():
    x=8
    print(x)
update()    


# In[20]:


def update(): #update function take the value from the user
    x = 8
    print(x)
update(8)


# In[21]:


def update(x): #update function take the value from the user
    x = 8
    print(x)
update(8)


# In[22]:


def update(x): # user want to update the value from 8 to 10 
    x = 8
    print(x)
update(10)


# In[23]:


8
def update(x):  
    x = 8
    print(x)
    
a = 10
update(a)


# In[24]:


def update(x):  
    x = 8
    print(x) 
    
a = 5
update(a)
print(a) # this print will update 8 to 10


# function we have 2 thing

# ![1.png](attachment:1.png)

# - we have concept called as pass by value & pass by reference if you look at below code
# 
# - in other programming language

# ![image.png](attachment:image.png)

# ### in python no concept called pass by value or pass by function

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# - if you understand the code well there is no change is x value
# 
# - declaration of x is main function
# 
# - this is for other programing language & even thoug if i change x value to a still it display same result

# In[25]:


def change(a):
    a = a+ 10
    print('inside the fun a =',a)
    
x = 10
print('x before calling:', x)
change(x)
print('x after calling:', x)


# - even though i changed value x to a stil we got the same result
# - THIS CONCEPT CALLED AS (PASS BY VALUE) FOR OTHER PROGRAMING

# In[26]:


def change(a):
    a = a+ 10
    print('inside the fun a =',a)
    
a = 10
print('a before calling:', a)
change(a)
print('a after calling:', a)


# - this is concept of pass by values & in this example both a refered to same address but after change the values only address changed.
# - The main reason being in python int & strings are immutable

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[30]:


def change(a):
    print('This is original a',id(a))
    a = a+ 10
    print('This is the new a =',id(a))
    print('inside the fun a =',a)
    
a = 10
print('a before calling:', a)
print('This is main a:',id(a))
change(a)
print('a after calling:', a)


# In[29]:


def change(a):
    print('This is original a',id(a))
    
    print('This is the new a =',id(a))
    a = a+ 10
    print('inside the fun a =',a)
    
a = 10
print('a before calling:', a)
print('This is main a:',id(a))
change(a)
print('a after calling:', a)


# In[31]:


def change(a):
    print('This is original a',id(a))
    a = a+ 10
    print('This is the new a =',id(a))
    print('inside the fun a =',a)
    
a = 10
print('a before calling:', a)
print('This is main a:',id(a))
change(a)
print('a after calling:', a)


# In[32]:


def change(a):
    #print('This is original a',id(a))
    a = a+ 10
    print('This is the new a =',id(a))
    print('inside the fun a =',a)
    
a = 10
print('a before calling:', a)
print('This is main a:',id(a))
change(a)
print('a after calling:', a)
print('This is original a',id(a))


# ![image.png](attachment:image.png)

# - in pass by reference lets pass the mutable e.g list & lets understand the concept

# In[33]:


def change(lst):
    lst[0] = lst[0]+10
    print('inside fun =', lst)
    
lst = [10]
print('Before calling:', lst)
change(lst)
print('After calling:',lst)


# ![image.png](attachment:image.png)

# In[34]:


def update(x):   
    x = 8
    print('x : ', x)    

a = 10
update(a)
print('a : ',a)


# In[35]:


def update(x):   
    print(id(x))
    x = 8
    #print(id(x))
    print('x', x)    

a = 10
print(id(a))
update(a)
print('a',a)


# In[36]:


def update(x):   
    #print(id(x))
    x = 8
    print(id(x))
    print('x', x)    

a = 10
print(id(a))
update(a)
print('a',a)


# ![image.png](attachment:image.png)

# - when you call a function by pass the value they will share the same memory location
# - the variabel which you pass & the variable which you accessing heear a & x refer to same obejct
# - the above concept is neither pass by value or pass by reference
# - Interview( Normally in python we dont use pass by value or pass by reference but other programing language it does & the reason is python is object oriented programing languag

# In[37]:


def update(x):   
    x = 8
    
    print(id(x)) 
    print('x', x)    

a = 10
print(id(a))

update(a)
print('a',a)

# we will understand more when we learn more


# In[38]:


def update(x):   
    print(id(x))
    x = 8
    print(id(x)) 
    print('x', x)    

a = 10
print(id(a))
update(a)
print('a',a)


# In[39]:


def update(lst):   
    print(id(lst))
    
    lst[1] = 25
    print(id(lst))
    print('x', lst)    

lst = [10,20,30] #lets pass list hear
print(id(lst))
update(lst)
print('lst',lst)


# NO concept for pass by value in python ( please refer the code below)

# In[40]:


def modify_integer(x):
    x = 10
    print("Inside function:", x)    
    
my_integer = 5
modify_integer(my_integer)
print("Outside function:", my_integer)


# In[41]:


def modify_integer(x):
    x = 10
    print("Inside function:", x)  
    print('Inside function:',id(x))
    
my_integer = 5
modify_integer(my_integer)
print("Outside function:", my_integer)
print('Outside function:',id(x))


# In[43]:


def modify_integer(x):
    print('original Inside function:',id(x))
    x = 10
    print("Inside function:", x)  
    print('Inside function:',id(x))
    
my_integer = 5
modify_integer(my_integer)
print("Outside function:", my_integer)
print('Outside function:',id(x))


# NO concept for pass by reference in python ( please refer the code below)

# In[44]:


def modify_list(my_list):
    my_list.append(4)
    print("Inside function:", my_list)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)


# In[45]:


def modify_list(my_list):
    print("original Inside function:", id(my_list))
    my_list.append(4)
    print("Inside function:", my_list)
    print("Inside function:", id(my_list))

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)
print("Outside function:", id(my_list))


# ### TYPE OF ARGUMENTS --> formal argument & actual argument 

# ![image.png](attachment:image.png)

# In[46]:


def add(a,b): # a & b called formal argument
    c = a+b
    print(c)
    
add(5,6) #5 and 6 we called as actual argument


# ![image.png](attachment:image.png)

# # positional argument

# In[48]:


def person(name,age):
    print(name)
    print(age)
    
person('nit',20)
# this is called postion argument becuase name we assigned to position name to nit & age to 28
# how it know that name - nit & age - 28 we need to take care of the position, we need to maintain the sequence but what if we dont know the sequence
# lets check we have 10 variable and we need to assign them with position but what if we forget the sequence


# In[49]:


def person(name,age):
    print(name)
    print(age)
    
person(20,'nit')

# in this case we cant assign name - 20 & age to 'nit' then we can assign them as keyword 
# as we keep incorrect position this code trhoughs an error . so how to fix them 
# i dont want assign name - 20 & age to nit & in this case we will assing keyword


# ![image.png](attachment:image.png)

# # keyword argument

# In[50]:


def person(name,age):
    print(name)
    print(age)
    
person(age = 20, name = 'nit') 

#this is called keyword arguments


# ![image.png](attachment:image.png)

# # default argument

# - while you open meta account minumu age criterial is so. by default age is 18

# In[52]:


def person(name,age): #in this code we expected to print 2 but we got bydefault 
    print(name)
    print(age)
    
person('nit') 


# In[53]:


def person(name,age = 18): 
    print(name)
    print(age)
    
person('nit') 


# In[54]:


def person(name,age = 18):  
    print(name)
    print(age)
    
person('nit', 38)  #in hear bydefault override the existing default value


# ![image.png](attachment:image.png)

# # variable length argument

# In[55]:


def sum(a, b):
    c = a+b
    print(c)
    
sum(5,6) 


# In[56]:


def sum(a, b):
    c = a+b
    print(c)
    
sum(5,6) 


# - Everytime we cant add only 2 value we can also pass more the 3 values
# - you can define the function when the number of argument are not fixed

# In[57]:


def sum(a, b):
    c = a+b
    print(c)
    
sum(5,6,7,8) 


# In[58]:


def sum(a, *b): # 1st argument is fixed but for 2nd argument
    c = a+b
    print(c)

sum(5,6,7,8) 
# we got error as int & tuple error becuase a is integer & b is tuple


# In[59]:


def sum(a, *b): # 1st argument is fixed but for 2nd argument
    #c = a+b
    print(type(a))
    print(type(b))

sum(5,6,7,8) 


# In[61]:


def sum(a, *b): # 1st argument is fixed but for 2nd argument
    #c = a+b
    print(a)
    print(b)

sum(3,5,7,8) 


# In[62]:


def sum(a, *b): # 1st argument is fixed & we fetch each value from the tuple & we can add them. 
    c = a     
    for i in b:
        c = c + i 
        print(c)
        
sum(5,6,7,8) 


# In[63]:


def sum(a, *b): 
    
    c = a 
    for i in b:
        c = c + i 
    print(c)
    
sum(5,6,7,8) 


# In[64]:


def sum(a, *b): 
    
    c = a 
    
    for i in b:
        c = c + i 
    print(c)
    
sum(5,6,7,8,4,-1,1,2,3,4,6) 


# In[65]:


def sum(a, *b): 
    
    c = 0
    for i in b:
        c = c + i 
    print(c)
    
sum(5,6,7,8) 


# - KWARGs (key worded variable length arguments)

# ![image.png](attachment:image.png)

# In[66]:


def person():
    person('ALEX', 36, 'JOHN', 987767)


# In[67]:


def person(name,*data):
    print('name')
    print(data)

person('ALEX', 36, 'JOHN', 987767)
#hear what is name - is it JOHN or ALEX thats why we assigned keywords varible arguments


# In[68]:


def person(name,*data):
    print(name)
    print(data)

person('ALEX', 36, 'JOHN', 987767)
#hear what is name - is it southcit or AAA thats why we assigned keywords varible arguments


# In[69]:


def person(name,*data):
    print('name')
    print(data)

person('ALEX', age = 36, home_place ='southcity', mob =987767)
# we got error as keyword argument thats why we add another *


# In[70]:


def person(name,**data):
    print(name)
    print(data)

person('mark', age = 36, home_place ='southcity', mob =987767)


# In[71]:


def person(name,**data):
    print(name)
    
    for i, j in data.items():
        print(i, j)
        
person('john', age = 36, home_place ='southcity', mob =987767, place = 'USA')


# # Global variable vs Local Variable

# - We discussed about variable & discussed about function
# - Sometimes we are creating variable inside the function and sometimes we are creating variable outside of the function
# - when we declare variable outside of the function that concept called as scope

# In[72]:


a = 10

print(a)


# In[73]:


a = 10  

def something():
    a = 15
    print('in function',a)    

print('out function',a)
    
    # in this code we are declaring 2 variable is this possible
    # first line of a is called outside of the function 
    # inside the function is called local variable   


# In[74]:


a = 10  

def something():
    a = 15
    
print('in function',a) 
  
print('out function',a)
    
    # in this code we are declaring 2 variable is this possible
    # first line of a is called outside of the function 
    # inside the function is called local variable 


# ![image.png](attachment:image.png)

# In[75]:


a = 10  

def something():
    a = 15  #hear a is local variable 
    b = 8
    print(a)
    
#print(b)
print(a)


# In[76]:


a = 10  

def something():
    a = 15  #hear a is local variable 
    print(a)
    
print(a)


# In[77]:


a = 10  

def something():
    a = 15
    print('in function',a)  # local variable
    
print('out function',a) #gloabl variable

# In this code we ddint call the function 


# In[78]:


a = 10  

def something():
    a = 15
    print('in function',a)  # local variable
 
something()
print('out function',a) #gloabl variable

# 1st preference is always local variable 


# In[79]:


a = 10  

def something():
    #if we remove this variable then can befault it consider as global variable
    print('in function',a)
    
something()
print('out function',a)
# if we dont assign any variabel inside the functin bydefault both considerd as local variable


# In[80]:


a = 10  

def something():
    a = 55
    print('in function',a)
something()

print('out function',a)


# In[81]:


# if i want to define global variabel inside the function 

a = 10  

def something():
    global a 
    b = 15 # 15 is converted to local when user assigned global a 
    print('in function',b)
    
something()
print('out function',a)

# now in this case we dont have local variable & all variables are global variable only
# so this is how we are assigned to local variabel & global variable


# In[84]:


a = 10  

def something():
    global a
    a = 15     # we refered local to global 
    print('in function',a)
    
    a = 9 # i want a to be local variable 
        #can we assigned loca variabel in the function answer is not cuz bydefault it will treate as global
        # can we declare local & gloabl inside th function 
something()

print('out function',a)


# In[85]:


import keyword
keyword.kwlist


# In[86]:


# if we used local & global in the same function this is not good idea thats wy introduced to GLOBALS

a = 10  
print(id(a))

def something():
    a = 9
    x = globals()['a'] #gloabls can give you all the gloabls 
    
    print(id(x))
    print('in function',a)
    
        
something()
print('out function',a)


# In[87]:


# now lets introduce special function called globals & using globals we can access global variable address

a = 10 
print(id(a))

def something():
    a = 9
    x = globals() # if i dont mention a then it will creat new memory
    
    print(id(x))
    print('in function',a)
    
    globals()['a'] = 15
    
        
something()
print('out function',a)


# # pass list to function

# Can we pass list of element in the function that function will return the count of even or odd number from the list

# In[88]:


def count(lst):
    
    even = 0
    odd = 0
    
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd +=1 
    return even,odd

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
even,odd = count(lst)         

print(even)
print(odd)


# In[89]:


def count(lst):
    
    even = 0
    odd = 0
    
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd +=1 
    return even,odd

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
even,odd = count(lst)         

print("Even Number: {} and odd Number : {}".format(even,odd)) 
#format is function belongs to string& bydefault you need to pass 2 parameter


# ![image.png](attachment:image.png)

# In[90]:


def fib(n):
    print(0)
    print(1)   
    
fib(0)

# in the above code we can get the fibonaci series but if the number is large then it takes more time


# In[91]:


def fib(n):
    print(0)
    print(1)
    print(1)
    print(2)
    print(3)
    print(5)
    
fib(0)


# ![image.png](attachment:image.png)

# In[92]:


# in progammin we need to continue these process thats why we need to use loop hear

def fib(n):
    a = 0
    b = 1
    
    print(a)
    print(b)
    
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        
        print(c)
        
fib(5)


# In[93]:


# Ignore below code
'''if user wants 5 value then above code is applicable but if user wants only 1 value then if you write 
#fib(1) then you will get 2 vales thats why we need to write the condition hear.'''

def fib(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
fib(2)


# ![image.png](attachment:image.png)

# In[94]:


def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
        
    return f

x = 5
result = fact(x)
print(result)     

# please use debug the code in pycharm for more indetail explanation & breakthrouth point at f = 1


# # RECURSSION - CALLING FUNCTION FROM ITSELF IS CALLED RECURSSION

# ![image.png](attachment:image.png)

# In[95]:


def wish():
    print('hello')
wish()


# In[96]:


# i want to cal the hello multiple time
# it will execute maximum 1000 time & in below code wish is calling by itself
# bydefault we have 1000 limitation can we extend the recurssion limitation yes we can 

def wish(): #---------> 2-greeting function will executed
    print('hello') 
wish() # What if i call the function again #3---------> function calls itself is called recurssion

wish() #------------> 1-at this point we are calling wish() function 

# it will print infinity time cuz recursion its own function 


# In[97]:


def wish():
    print('hello')
    wish()
wish()


# In[98]:


import sys
print(sys.getrecursionlimit())


# In[99]:


sys.setrecursionlimit(2000)


# In[100]:


print(sys.getrecursionlimit())


# In[ ]:


'''
def wish():
    print('hello')
    wish()
wish()
'''
#kernal will dead 


# In[102]:


import sys
sys.setrecursionlimit(150)
print(sys.getrecursionlimit())

i = 0

def wish():
    global  i
    i += 1
    print('hello', i)
    wish()
wish()

# how to know how many wish it printed 
# so for best practice i would suggest for 
    


# # FACTORIAL USING RECURSSION

# recurssion is funcion calls itself

# ![image.png](attachment:image.png)

# In[103]:


def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

result = fact(5)

result


# ![image.png](attachment:image.png)

# In[104]:


def square(a):
    return a * a
result = square(5)
print(result)

# what if i dont want to call square() multiple times 


# In[105]:


#lambda expresion or lambda function
f = lambda a: a * a # hear a is an argument & operation in the argument is a * a
result = f(5)
result
# hear anonymous function is called lambda 
# remember lambda alway you need to assgin as function cuz function are object in python


# In[106]:


#lets define function which will add 2 number
# we are defining a function whcih doesnt have name
#lambda expresion or lambda function

f = lambda a, b : a + b

result = f(1,4)
result


# In[ ]:


How can we use lambda in other function like - filter, map & reduce


# ![image.png](attachment:image.png)

# In[107]:


#lets take one list & i want to find the list of even numbers
nums = [3,2,6,8,4,6,2,9]

evens = list(filter(is_even, nums)) #is_even is not an inbuild function 


# In[114]:


def is_even(n):
    return n % 2 == 0

nums = [3,2,6,8,4,6,2,9]
evens = list(filter(is_even, nums))
print(evens)    
# remember filter always takes 2 argument 1- function for the logic 2- sequence or list


# In[115]:


def is_odd(n):
    return n % 2 != 0

nums = [3,2,6,8,4,6,2,9]
odd = list(filter(is_odd, nums))
print(odd)  


# In[116]:


# lets write above function using help of lambda & lambda helps to reduce the line
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n : n%2 ==0, nums))
print(evens)


# In[117]:


nums = [3,2,6,8,4,6,2,9]
odd = list(filter(lambda n : n%2 !=0, nums))
print(odd)


# - What ever even number I have from the assigned list
# - I want to double the even number i.e 2 become 4 || 4 become 6 || 6 become 8
# - that we will do using map function
# - this largly we are using in google map reduce programme
# - we can build using user define & lambda

# In[118]:


def update(n):
    return n*2 

nums = [3,2,6,8,4,6,2,9]
evens = list(filter(is_even, nums))
double = list(map(update, evens))

print(double)  


# In[119]:


nums = [3,2,6,8,4,6,2,9]
evens = list(filter(is_even, nums))
#double = list(map(lambda n : n*2, evens))
double_ = list(map(lambda n : n-2, evens))
#print(double)  
print(double_)


# In[120]:


nums = [3,2,6,8,4,6,2,9]
evens = list(filter(is_even, nums))
double = list(map(lambda n : n*2, evens))
double_ = list(map(lambda n : n-2, evens))

print(double)  
print(double_)


# In[121]:


nums = [3,2,6,8,4,6,2,9]
evens = list(filter(is_even, nums))
double = list(map(lambda n : n*2, evens))
double_ = list(map(lambda n : n-2, evens))
double1 = list(map(lambda n : n+2, evens))

print(double)  
print(double_)
print(double1)


#  - i want to perform reduce now
# - i want reduce all the values
# - reduce you can add only 2 values
# - [4, 12, 16, 8, 12, 4] if you sum everything then you will get 56

# In[122]:


from functools import reduce

def add_all(a,b):
    return a+b

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(is_even, nums))
double = list(map(lambda n : n*2, evens))
sums = reduce(add_all, double)
sums
#print(sums)          
              


# In[123]:


from functools import reduce

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(is_even, nums))
double = list(map(lambda n : n*2, evens))
sums = (reduce(lambda a,b : a + b, double))

print(evens)
print(double)     
print(sums) 


# ![image.png](attachment:image.png)

# # ![image.png](attachment:image.png)

# In[124]:


__name__


# In[125]:


print(__name__)


# In[ ]:




