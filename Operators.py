Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 a=10
 
SyntaxError: unexpected indent
>>> a=10
>>> a
10
>>> b=20
>>> b
20
>>> c=a+b
>>> c
30
>>> c=a-b
>>> c
-10
>>> c=a*b
>>> c
200
>>> c=a/b
>>> c
0.5
>>> a=20
>>> b=4
>>> c=a/b
>>> c
5.0
>>> c=a//b
>>> c
5
>>> c=a%b
>>> c
0
>>> a=a+2
>>> a
22
>>> b=5
>>> b+=2
>>> b
7
>>> m=2
>>> n=4
>>> z*=2
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    z*=2
NameError: name 'z' is not defined
>>> b=5
>>> b=b*2
>>> b
10
>>> b*=2
>>> b
20
>>> i=7
>>> i
7
>>> -i=-7
SyntaxError: can't assign to operator
>>> j=5
>>> -j=5
SyntaxError: can't assign to operator
>>> a=50
>>> a
50
>>> -a
-50
>>> a=-a
>>> a
-50
>>> a=10
>>> b=20
>>> a>b
False
>>> b>a
True
>>> a==b
False
>>> a!=b
True
>>> a=9
>>> b=9
>>> a<=b
True
>>> a>=b
True
>>> a,b=5,9
>>> a
5
>>> b
9
>>> a<6 and b<10
True
>>> a<6 and b>10
False
>>> a>6 and b>10
False
>>> a<6 or b>10
True
>>> a>6 or b<10
True
>>> a=True
>>> a
True
>>>  not a
SyntaxError: unexpected indent
>>> not a
False
>>> b=False
>>> not b
True
>>> 
