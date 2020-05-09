Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  
a=5
>>> a
5
>>> type(a)
<class 'int'>
>>> b=5.98
>>> b
5.98
>>> type(b)
<class 'float'>
>>> name='shreya'
>>> name
'shreya'
>>> type(name)
<class 'str'>
>>> x=int(b)
>>> x
5
>>> type(x)
<class 'int'>
>>> y=float(a)
>>> y
5.0
>>> type(y)
<class 'float'>
>>> i
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    i
NameError: name 'i' is not defined
>>> type(i)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(i)
NameError: name 'i' is not defined
>>> i=
SyntaxError: invalid syntax
>>> a=6
>>> b=3
>>> c=a+bi
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c=a+bi
NameError: name 'bi' is not defined
>>> c=6+3i
SyntaxError: invalid syntax
>>> c=6+3j
>>> c
(6+3j)
>>> type(c)
<class 'complex'>
>>> a=10
>>> k=3
>>> num=complex(a,k)
>>> num
(10+3j)
>>> z=int(num)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    z=int(num)
TypeError: can't convert complex to int
>>> a=1
>>> b=5
>>> num=a<b
>>> num
True
>>> int(num)
1
>>> int(b<a)
0
>>> p=range(10)
>>> p
range(0, 10)
>>> list[range(10)]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    list[range(10)]
TypeError: 'type' object is not subscriptable
>>> list[10,20,30,30,40]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list[10,20,30,30,40]
TypeError: 'type' object is not subscriptable
>>> list=[10,20,30,30,50]
>>> list
[10, 20, 30, 30, 50]
>>> tuple=(11,12,13,14,14)
>>> tuple
(11, 12, 13, 14, 14)
>>> set={11,12,13,13,14}
>>> set
{11, 12, 13, 14}
>>> set={23,56,56,78,34}
>>> set
{56, 34, 78, 23}
>>> dic=[1:'shreya',2:'rahul',3:'krati']
SyntaxError: invalid syntax
>>> type(list)
<class 'list'>
>>> type(tuple)
<class 'tuple'>
>>> type(set)
<class 'set'>
>>> dic={1:'shreya',2:'pragati',3:'krati'}
>>> dic
{1: 'shreya', 2: 'pragati', 3: 'krati'}
>>> type(dic)
<class 'dict'>
>>> str='kanika'
>>> str
'kanika'
>>> type(str)
<class 'str'>
>>> range(20)
range(0, 20)
>>> type(range)
<class 'type'>
>>> list(range(20))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list(range(20))
TypeError: 'list' object is not callable
>>> list=[range(10)]
>>> list
[range(0, 10)]
>>> list(range(2,10,2))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list(range(2,10,2))
TypeError: 'list' object is not callable
>>> range(10)
range(0, 10)
>>> list(range(10))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
>>> dic={'rahul':'Iphone','kiran':'samsung','kriti':'oppo','ritu':'vivo'}
>>> dic
{'rahul': 'Iphone', 'kiran': 'samsung', 'kriti': 'oppo', 'ritu': 'vivo'}
>>> dic.keys()
dict_keys(['rahul', 'kiran', 'kriti', 'ritu'])
>>> dic.values()
dict_values(['Iphone', 'samsung', 'oppo', 'vivo'])
>>> 
