Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
2+3
5
>>> 5-2
3
>>> 5*5
25
>>> 10/2
5.0
>>> 10//2
5
>>> 10%3
1
>>> 2**10
1024
>>> 2.5+2.5
5.0
>>> 2.5*2
5.0
>>> 2.5*2.8
7.0
>>> 8+2*10
28
>>> 8*2+10
26
>>> (8+2)*5
50
>>> 'navin'
'navin'
>>> "navin"
'navin'
>>> print('navin')
navin
>>> print('navin's laptop')
	  
SyntaxError: invalid syntax
>>> print("navin,"Ohhh my god"")
	  
SyntaxError: invalid syntax
>>> print("navin's book")
	  
navin's book
>>> print('navin,"Its you"')
	  
navin,"Its you"
>>> print('navin's "laptop"')
	  
SyntaxError: invalid syntax
>>> print('navin\'s "laptop"')
	  
navin's "laptop"
>>> 2 * 'navin'
	  
'navinnavin'
>>> 10 * 'navin'
	  
'navinnavinnavinnavinnavinnavinnavinnavinnavinnavin'
>>> 'navin'+'navin'
	  
'navinnavin'
>>> print(c:\docs\navin)
	  
SyntaxError: invalid syntax
>>> print('c:\docs\navin')
	  
c:\docs
avin
>>> print('c:\docs\\navin')
	  
c:\docs\navin
>>> print(r'c:\docs\navin')
	  
c:\docs\navin
>>> x=2
	  
>>> x
	  
2
>>> x=5
	  
>>> y=10
	  
>>> x+y
	  
15
>>> x=9
	  
>>> x+1
	  
10
>>> y
	  
10
>>> abc
	  
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> abc=10
	  
>>> abc
	  
10
>>> x=10
	  
>>> _+y
	  
20
>>> name='youtube'
	  
>>> name
	  
'youtube'
>>> print(name)
	  
youtube
>>> my_name='shreya'
	  
>>> my_name[2]
	  
'r'
>>> my_name[10]
	  
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    my_name[10]
IndexError: string index out of range
>>> my_name[-1]
	  
'a'
>>> my_name[-5]
	  
'h'
>>> my_name[-9]
	  
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    my_name[-9]
IndexError: string index out of range
>>> color='purple'
	  
>>> color[1:4]
	  
'urp'
>>> color[1:6]
	  
'urple'
>>> color[1:]
	  
'urple'
>>> color[:5]
	  
'purpl'
>>> color[1:10]
	  
'urple'
>>> chanel='Youtube'
	  
>>> chanel[0:3]='My'
	  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    chanel[0:3]='My'
TypeError: 'str' object does not support item assignment
>>> chanel[0]='T'
	  
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    chanel[0]='T'
TypeError: 'str' object does not support item assignment
>>> 'my'+chanel[3:]
	  
'mytube'
>>> city='VishakhaPatnam'
	  
>>> len(city)
	  
14
>>> 
list1[11,22,33,44,100]
	  
Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    list1[11,22,33,44,100]
NameError: name 'list1' is not defined
>>> list1=[10,20,30,40,50]
	  
>>> list
	  
<class 'list'>
>>> list1
	  
[10, 20, 30, 40, 50]
>>> list1[0]
	  
10
>>> list2[4]
	  
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list2[4]
NameError: name 'list2' is not defined
>>> list1[4]
	  
50
>>> list1[1:]
	  
[20, 30, 40, 50]
>>> list1[-3]
	  
30
>>> list_str=['shreya','sakshi','vishal','rahul']
	  
>>> list_str
	  
['shreya', 'sakshi', 'vishal', 'rahul']
>>> list_str[1]
	  
'sakshi'
>>> var_list=[23,'navin',4.56]
	  
>>> var_list
	  
[23, 'navin', 4.56]
>>> List=[var_list,list_str]
	  
>>> List
	  
[[23, 'navin', 4.56], ['shreya', 'sakshi', 'vishal', 'rahul']]
>>> trial_list=[23,45,78,55,10,100]
	  
>>> trial_list
	  
[23, 45, 78, 55, 10, 100]
>>> trial_list.append(23)
	  
>>> trial_list
	  
[23, 45, 78, 55, 10, 100, 23]
>>> trial_list.insert(3,200)
	  
>>> trial_list
	  
[23, 45, 78, 200, 55, 10, 100, 23]
>>> trial_list.clear()
	  
>>> trial_list
	  
[]
>>> trial_list.remove(200)
	  
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    trial_list.remove(200)
ValueError: list.remove(x): x not in list
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> value=[10,100,20,200,30,300]
	  
>>> value
	  
[10, 100, 20, 200, 30, 300]
>>> value.remove(200)
	  
>>> value
	  
[10, 100, 20, 30, 300]
>>> value.pop()
	  
300
>>> value.pop(20)
	  
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    value.pop(20)
IndexError: pop index out of range
>>> value.pop(2)
	  
20
>>> int_value=[10,11,23,34,56,78]
	  
>>> int_value
	  
[10, 11, 23, 34, 56, 78]
>>> del int_value[3:5]
	  
>>> int_value
	  
[10, 11, 23, 78]
>>> del int_value[2:]
	  
>>> int_value
	  
[10, 11]
>>> half_list=[10,20,30,40,50]
	  
>>> half_list
	  
[10, 20, 30, 40, 50]
>>> half_extend([60,70,80,90,100])
	  
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    half_extend([60,70,80,90,100])
NameError: name 'half_extend' is not defined
>>> half_list.extend([60,70,80,90,100])
	  
>>> half_list
	  
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> max(half_list)
	  
100
>>> min(half_list)
	  
10
>>> sum(half_list)
	  
550
>>> list4=[10,90,77,13,57,72]
	  
>>> list4
	  
[10, 90, 77, 13, 57, 72]
>>> sort(list)
	  
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    sort(list)
NameError: name 'sort' is not defined
>>> sort(list4)
	  
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    sort(list4)
NameError: name 'sort' is not defined
>>> list4.sort()
	  
>>> list4
	  
[10, 13, 57, 72, 77, 90]
>>> list4.count()
	  
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    list4.count()
TypeError: count() takes exactly one argument (0 given)
>>> count(list4)
	  
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    count(list4)
NameError: name 'count' is not defined
>>> tuple=(10,20,30,40)
	  
>>> typle
	  
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    typle
NameError: name 'typle' is not defined
>>> tuple
	  
(10, 20, 30, 40)
>>> max(tuple)
	  
40
>>> min(tuple)
	  
10
>>> tuple.sort()
	  
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    tuple.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> sum(sort)
	  
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    sum(sort)
NameError: name 'sort' is not defined
>>> sum(tuple)
	  
100
>>> tuple.count()
	  
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    tuple.count()
TypeError: count() takes exactly one argument (0 given)
>>> count(tuple)
	  
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    count(tuple)
NameError: name 'count' is not defined
>>> tuple[3]=60
	  
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    tuple[3]=60
TypeError: 'tuple' object does not support item assignment
>>> tuple.clear()
	  
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    tuple.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> tup=[11,11,89,89,89]
	  
>>> tup.count(11)
	  
2
>>> tup.count(89)
	  
3
>>> list=[11,23,23,45,45,45]
	  
>>> list
	  
[11, 23, 23, 45, 45, 45]
>>> list.count(45)
	  
3
>>> list.length()
	  
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    list.length()
AttributeError: 'list' object has no attribute 'length'
>>> len(list)
	  
6
>>> len(tup)
	  
5
>>>  
