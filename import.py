Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=math.sqrt(25)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x=math.sqrt(25)
NameError: name 'math' is not defined
>>> import math
>>> x=math.sqrt(25)
>>> x
5.0
>>> x=math.pow(2,5)
>>> x
32.0
>>> print(math.floor(2.9))
2
>>> print(math.ceil(6.2))
7
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> import math as m
>>> m.sqrt(36)
6.0
>>> m.pow(5,2)
25.0
>>> print(m.ceil(34.6))
35
>>> print(m.floor(78.2))
78
>>> m.fact(5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    m.fact(5)
AttributeError: module 'math' has no attribute 'fact'
>>> m.fac(5)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    m.fac(5)
AttributeError: module 'math' has no attribute 'fac'
>>>  from math import sqrt()
SyntaxError: unexpected indent
>>> from math import sqrt
>>> x=math.sqrt(49)
>>> x
7.0
>>> 
