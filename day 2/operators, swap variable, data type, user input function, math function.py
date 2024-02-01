#!/usr/bin/env python
# coding: utf-8

# # How to create environment variable

# STEPS TO SET UP EXECUTE PYTHON IN SYSTEM CMD (TO CREATE ENVIRONMENT VARIABLE)
# Open cmd # python (You will get error when you execute 1st time)
# search with environment variable - system variable:(C:\Users\kdata\AppData\Local\Microsoft\WindowsApps)
# restart the cmd & type python in cmd it will work now

# # to find help

# STEPS TO FIND HELP OPTION --> 1- help() | 2- topics | 3- search as per requirments | 4- quit if you want help on any command then help(list) || help(tuple)

# In[ ]:


help()


# ![16.png](attachment:16.png)

# In[6]:


help(list)


# In[7]:


2 + 3


# In[8]:


help(tuple)


# # introduce to ID()

# In[9]:


# variable address
num = 5
id(num)


# In[10]:


name = 'nit'
id(name) #Address will be different for both


# In[11]:


a = 10
id(a)


# In[12]:


b = a #thats why python is more memory efficient 


# In[13]:


id(b)


# In[14]:


id(10)


# In[15]:


k = 10 
id(k)


# In[16]:


a = 20  # as we change the value of a then address will change
id(a)


# In[17]:


id(b)


# what ever the variale we assigned the memory and we not assigned anywhere then we can use as garbage collection.|| VARIABLE - we can change the values || CONSTANT - we cannot change the value -can we make VARIABLE as a CONSTANT (note - in python you cannot make variable as constant)

# In[19]:


PI = 3.14  #in math this is alway constant but python we can chang
PI


# In[20]:


PI = 3.15
PI


# In[21]:


type(PI)


# # DATA TYPES & DATA STRUCTURES-->

# 1- NUMERIC || 2-LIST || 3-TUPLE || 4-SET || 5-STRING || 6-RANGE || 7-DICTIONARY

# ![1.png](attachment:1.png)

# ![2.png](attachment:2.png)

# 1- NUMERIC :- INT || FLOAT || COMPLEX || BOOL

# In[22]:


w = 2.5
type(w)


# In[23]:


(a)


# In[24]:


w2 = 2 + 3j #so hear j is represent as root of -1
type(w2)


# In[25]:


#convert flot to integer 
a = 5.6
b = int(a)


# In[26]:


b


# In[27]:


type(b)


# In[28]:


type(a)


# In[29]:


k = float(b)


# In[30]:


k


# In[31]:


print(a)
print(b)
print(k)


# In[32]:


k1 = complex(b,k)


# In[33]:


print(k1)
type(k1)


# In[34]:


b < k


# In[35]:


condition = b<k
condition


# In[36]:


type(condition)


# In[37]:


int(True)


# In[38]:


int(False)


# In[39]:


l = [1,2,3,4]
print(l)
type(l)


# In[40]:


s = {1,2,3,4}
s


# In[41]:


type(s)


# In[42]:


t = (10,20,30)
t


# In[43]:


type(t)


# In[44]:


str = 'nit' #we dont have character in python 
type(str)


# In[45]:


st = 'n'
type(st)


# range()
# 

# In[47]:


r = range(0,10)
r


# In[48]:


type(r)


# In[49]:


# if you want to print the range 
list(range(0,10))


# In[50]:


r1 = list(r)
r1


# In[51]:


#if you want to print even number
even_number = list(range(2,10,2))
even_number


# In[52]:


d= {1:'one', 2:'two', 3:'three'}
d 


# In[53]:


type(d)


# In[54]:


# print the keys 
d.keys()


# In[55]:


# how to get particular value 
d[2]


# In[56]:


# other way to get value as
d.get(2)


# # operator
# 

# 1- ARITHMETIC OPERATOR ( + , -, *, /, %, %%, **, ^) 2- ASSIGNMEN OPERATOR (=) 3- RELATIONAL OPERATOR 4- LOGICAL OPERATOR 5- UNARY OPERATOR

# # Arithmetic operator
# 

# In[57]:


x1, y1 = 10, 5


# In[58]:


#x1 ^ y1


# In[59]:


x1  + y1 


# In[60]:


x1 - y1


# In[61]:


x1 * y1


# In[62]:


x1 / y1


# In[63]:


x1 // y1


# In[64]:


x1 % y1 


# In[65]:


x1 ** y1


# In[66]:


x2 =3
y2 = 3
x2 ** y2


# # Assignment operator
# 

# In[67]:


x = 2


# In[68]:


x = x + 2 # if you want to increment by 2 


# In[69]:


x += 2
x


# In[70]:


x += 2
x


# In[71]:


x *= 2


# In[72]:


x


# In[73]:


x -= 2


# In[74]:


x


# In[75]:


x /= 2


# In[76]:


x


# In[77]:


a, b = 5,6 # you can assigned variable in one line as well


# In[78]:


a


# In[79]:


b


# # unary operator
# 

# unary means 1 || binary means 2
# Here we are applying unary minus operator(-) on the operand n; the value of m becomes -7, which indicates it as a negative value.

# In[80]:


n = 7 #negattion
n


# In[81]:


m = -(n)
m


# In[82]:


n


# In[83]:


-n


# # Relational operator
# 

# we are using this operator for comparing

# In[84]:


a = 5
b = 6


# In[85]:


a<b


# In[86]:


a>b


# In[87]:


# a = b # we cannot use = operatro that means it is assigning 


# In[88]:


a == b


# In[89]:


a != b


# In[90]:


# hear if i change b = 6
b = 5


# In[91]:


a == b


# In[92]:


b


# In[93]:


a >= b


# In[94]:


a <= b


# In[95]:


a < b


# In[96]:


a>b


# In[97]:


b = 7


# In[98]:


a != b


# # LOGICAL OPERATOR
# 

# ![3.png](attachment:3.png)

# logical operator you need to understand about true & false table
# 3 importand part of logical operator is --> AND, OR, NOT

# # lets understand the truth table:- in truth table you can represent (true-1 & false means- 0)

# ![4.png](attachment:4.png)

# ![5.png](attachment:5.png)

# ![6.png](attachment:6.png)

# In[99]:


a = 5
b = 4


# In[100]:


a < 8 and b < 5 #refer to the truth table 


# In[101]:


a < 8 and b < 2


# In[102]:


a < 8 or b < 2


# In[103]:


a>8 or b<2


# In[104]:


x = False
x


# In[105]:


not x  # you can reverse the operation


# In[106]:


x = not x
x


# In[107]:


x


# In[108]:


not x


# # Number system coverstion (bit-binary digit)
# 

# In the programing we are using binary system, octal system, decimal system & hexadecimal system
# but where do we use this in cmd - you can check your ip address & lets understand how to convert from one system to other system
# when you check ipaddress you will these format --> cmd - ipconfig

# binary : base (0-1) --> please divide 15/2 & count in reverse order ocatl : base (0-7) hexadecimal :base (0-9 & then a-f)

# ![7.png](attachment:7.png)

# In[109]:


bin(25)


# ![8.png](attachment:8.png)

# In[110]:


0b11001


# In[111]:


int(0b11001)


# In[112]:


bin(7)


# In[113]:


oct(25)


# In[114]:


0o31


# In[115]:


int(0o31)


# In[116]:


hex(25)


# In[117]:


0x19


# In[118]:


hex(16)


# In[119]:


0xa


# In[120]:


0xb


# ![9.png](attachment:9.png)

# In[121]:


hex(25)


# In[122]:


0x19


# In[123]:


0x15


# # swap 2-variable in python

# (a,b = 5,6) After swap we should get ==> (a, b = 6,5 )

# In[125]:


a = 5
b = 6


# In[126]:


a = b
b = a


# In[127]:


print(a)
print(b)


# In[128]:


# in above scenario we lost the value 5 
a1 = 7
b1 = 8


# In[129]:


temp = a1 
a1 = b1
b1 = temp


# In[130]:


print(a1)
print(b1)


# in the above code we are using third variable
# in interview they might ask can we swap better way without using 3rd variable

# ![10.png](attachment:10.png)

# In[131]:


a2 = 5
b2 = 6


# In[132]:


#swap variable formulas without using 3rd formula
a2 = a2 + b2 # 5+6 = 11
b2 = a2 - b2 # 11-6 = 5
a2 = a2 - b2 # 11-5 = 6 


# In[133]:


print(a2)
print(b2)


# In[134]:


print(0b101) # 101 is 3 bit 
print(0b110) # 110 also 3bit 


# In[135]:


print(0b110)
print(0b101)


# In[136]:


#but when we use a2 + b2 then we get 11 that means we will get 4 bit which is 1 bit extra 
print(bin(11))
print(0b1011)


# ![11.png](attachment:11.png)

# ![12.png](attachment:12.png)

# In[137]:


print(a2)
print(b2)


# In[138]:


#there is other way to work using swap variable also which is XOR because it will not waste extra bit 
a2 = a2 ^ b2
b2 = a2 ^ b2
a2 = a2 ^ b2


# In[139]:


print(a2)
print(b2)


# In[140]:


a2, b2


# In[141]:


a2 ,b2 = b2, a2 # how it work is b2 6 a2 is 5 first it goes into stack & then it reverse the 2 vlaues


# In[142]:


print(a2)
print(b2)


# # BITWISE OPERATOR

# WE HAVE 6 OPERATORS COMPLEMENT ( ~ ) || AND ( & ) || OR ( | ) || XOR ( ^ ) || LEFT SHIFT (<< ) || RIGHT SHIFT ( >> )

# In[143]:


print(bin(12))
print(bin(13))


# In[144]:


0b1101


# In[145]:


0b1100


# # complement --> you will get this key below esc character

# 12 ==> 1100 ||
# 
# first thing we need to understand what is mean by complement.
# complement means it will do reverse of the binary format i.e. - ~0 it will give you 1 ~1 it will give 0
# 12 binary format is 00001100 ( complement of ~00001100 reverse the number - 11110011 which is (-13)
# in the virtual memory we cant store -ve number & the only way to store the -ve value by using complimentory
# but the question is why we got -13
# to understand this concept ( we have concept of 2's complement
# 2's complement mean (1's complement + 1)
# in the system we can store +Ve number but how to store -ve number
# 
# lets understand binary form of 13 - 00001101 + 1

# ![13.png](attachment:13.png)

# In[146]:


# COMPLEMENT (~) (TILDE  OR TILD)
~12 # why we get -13 . first we understand what is complment means (reversr of binary format)


# In[147]:


~46


# In[148]:


~54


# In[149]:


~-6


# In[150]:


~-1


# # bit wise and operator

# AND - LOGICAL OPERATOR ||| & - BITWISE AND OPERATOR
# (we know that 1 & 1 is 1) 12 - 00001100 13 - 00001101 when we are add both then then outut we will get as 12

# ![14.png](attachment:14.png)

# In[152]:


12 & 13


# In[153]:


12 | 13


# In[154]:


1 & 0


# In[155]:


1 | 0


# ![15.png](attachment:15.png)

# In[156]:


35 & 40 #please do the homework conververt 35,40 to binary format 


# In[157]:


35 | 40


# In[158]:


# in XOR if the both number are different then we will get 1 or else we will get 0

12 ^ 13


# In[159]:


25^30


# In[160]:


bin(10)


# In[161]:


# BIT WISE LEFT SHIFT OPERATOR 
# in left shift what we need to to we need shift in left hand side & need to shift 2 bits
#bit wise left operator bydefault you will take 2 zeros ( )
#10 binary operator is 1010 | also i can say 1010
10<<2


# In[162]:


bin(20)


# In[163]:


0b101000000


# In[164]:


20<<4 #can we do this


# In[165]:


bin(10)


# In[166]:


10>>2


# In[167]:


10>>3


# In[168]:


bin(20)


# In[169]:


20>>4


# # import math function 

# In[170]:


x = sqrt(25) #sqrt is inbuild function 


# In[171]:


import math # math is module


# In[172]:


x = math.sqrt(25)
x


# In[173]:


x1 = math.sqrt(15)
x1


# In[174]:


print(math.floor(3.87)) #floor - minimum or least value 


# In[175]:


print(math.ceil(3.87)) #ceil - maximum or highest value


# In[176]:


print(math.pow(3,2))


# In[177]:


print(math.pi) #these are constant


# In[178]:


print(math.e) # e - epsilon values


# In[179]:


m.sqrt(25) 


# In[180]:


import math as m # we need to use concept aliseing, instead of math we are using as m
m.sqrt(10) #if you are lazy to type then you can use m or else you can use math 


# In[181]:


from math import sqrt,pow # math has many function if you want to import specific function then use import
print(pow(2,3))
print(math.sqrt(10))


# In[182]:


round(pow(2,3))


# In[183]:


help(math)


# # user input function in python || command line input

# how to get input from user

# In[184]:


x = input()
y = input()
z = x + y
print(z) # console is waiting for user to enter input 
# also if you work in idle


# In[187]:


type(x)


# In[186]:


x1 = input('Enter the 1st number') #whenevery you works in input function it always give you string 
y1 = input('Enter the 2nd number') # it wont understand as arithmetic operator
z1 = x1 + y1
print(z1)


# In[188]:


print(type(x1))
print(type(y1))


# In[189]:


x1 = input('Enter the 1st number') #whenevery you works in input function it always give you string 
a1 = int(x1)
y1 = input('Enter the 2nd number') # it wont understand as arithmetic operator
b1 = int(y1)
z1 = a1 + b1
print(z1)


# for the above code notice we are using many lines because fo that wasting some memory spaces as well

# In[191]:


x2 = int(input('Enter the 1st number'))
y2 = int(input('Enter the 2nd number'))
z2 = x2 + y2
z2


# lets take input from the user in char format, but we dont have char format in python

# In[192]:


ch = input('enter a char')
print(ch)
#print(type(ch))


# In[193]:


print(ch[0])


# In[194]:


print(ch[0:2])


# In[195]:


print(ch[1])


# In[196]:


print(ch[-1])


# In[197]:


ch = input('enter a char')[0]
print(ch)


# In[198]:


ch = input('enter a char')[1]
print(ch)


# In[199]:


ch = input('enter a char')[1:3]
print(ch)


# In[200]:


ch = input('enter a char')
print(ch) # if you enter as 2 + 6 -1 we get output as 2 + 6-1 only cuz 2+6-1 as expression 


# EVAL function using input

# In[201]:


result = eval(input('enter an expr'))
print(result)


# In[ ]:




