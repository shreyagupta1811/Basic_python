Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
x=[11,12,13,14]
>>> x
[11, 12, 13, 14]
>>> for i in x:
	print(i)

	
11
12
13
14
>>> for i in range(10)'
SyntaxError: EOL while scanning string literal
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(0,10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(11,21,5):
	print(i)

	
11
16
>>> for i in range(21,11,-1)
SyntaxError: invalid syntax
>>> for i in range(21,11,-1):
	print(i)

	
21
20
19
18
17
16
15
14
13
12
>>> for i in range(20,25,1)
SyntaxError: invalid syntax
>>> for i in range(20,25,1):
	print(i)

	
20
21
22
23
24
>>> for i in range(11,21,3):
	print(i)

	
11
14
17
20
>>> for i in range(3,10,1):
	print(i)

	
3
4
5
6
7
8
9
>>> for i in range(1,11):
	if i%2==0:
		print(i)

		
2
4
6
8
10
>>> for i in range(1,11):
	mul=2*i
	print('2','*',i,'=',mul)

	
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
>>> for i in range(1,11):
	mul=85*i
	print('85','*',i,'=',mul)

	
85 * 1 = 85
85 * 2 = 170
85 * 3 = 255
85 * 4 = 340
85 * 5 = 425
85 * 6 = 510
85 * 7 = 595
85 * 8 = 680
85 * 9 = 765
85 * 10 = 850
>>> 
