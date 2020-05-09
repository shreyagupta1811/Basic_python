Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
set={10,20,30,40,40}
>>> set
{40, 10, 20, 30}
>>> set.add(10)
>>> set
{40, 10, 20, 30}
>>> dictionary={1:'shreya',2:'sakshi',3:'jasmine',4:'janvi'}
>>> dictionary
{1: 'shreya', 2: 'sakshi', 3: 'jasmine', 4: 'janvi'}
>>> dictionary[1]
'shreya'
>>> dictionary[2]
'sakshi'
>>> dictionary.get(5)
>>> dictionary
{1: 'shreya', 2: 'sakshi', 3: 'jasmine', 4: 'janvi'}
>>> print(dictionary.get(5))
None
>>> dictionary.get(2)
'sakshi'
>>> dictionary.get(1,'Not Found')
'shreya'
>>> dictionary.get(5,'Not Found')
'Not Found'
>>> list1=['sakshi','shreya','janvi','jasmine']
>>> list2=['JAVA','PYTHON','C','C++']
>>> dic2=dic(zip(list1,list2))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dic2=dic(zip(list1,list2))
NameError: name 'dic' is not defined
>>> list1=['sakshi','shreya','janvi','jasmine']
>>> list2=['JAVA','PYTHON','C','C++']
>>> dic2=dict(zip(list1,list2))
SyntaxError: multiple statements found while compiling a single statement
>>> list1=['sakshi','shreya','janvi','jasmine']
>>> list2=['JAVA','PYTHON','C','C++']
>>> dic2=dict(zip(list1,list2))
SyntaxError: multiple statements found while compiling a single statement
>>>  zhcsz
SyntaxError: unexpected indent
>>>  list1=['sakshi','shreya','janvi','jasmine']

 
>>> list1=['sakshi','shreya','janvi','jasmine']
>>>list2=['Java','C','C++','Python']
SyntaxError: unexpected indent
>>> data1=['sakshi','shreya','shubhi']
>>> data2=['Java','Python','C++']
>>> data=dict(zip(data1,data2))
>>> data
{'sakshi': 'Java', 'shreya': 'Python', 'shubhi': 'C++'}
>>> data['pratishtha']='R'
>>> data
{'sakshi': 'Java', 'shreya': 'Python', 'shubhi': 'C++', 'pratishtha': 'R'}
>>> clear(data)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    clear(data)
NameError: name 'clear' is not defined
>>> data.clear()
>>> data
{}
>>> data1=['sakshi','shreya','shubhi']
>>> data2=['Java','Python','C++']
>>> data=dict(zip(data1,data2))
>>> data
{'sakshi': 'Java', 'shreya': 'Python', 'shubhi': 'C++'}
>>> del.data['sakshi']
SyntaxError: invalid syntax
>>> del data['sakshi']
>>> data
{'shreya': 'Python', 'shubhi': 'C++'}
>>> dd=['C':'codeblock','JAVA':[1:'ecillipe',2:'netbeans'],'python':[1:'pycham',2:'sublimetext',3:'edit++']]
SyntaxError: invalid syntax
>>> dd={'C':'codeblock','JAVA':{1:'ecillipe',2:'netbeans'},'python':{1:'pycham',2:'sublimetext',3:'edit++'}}
>>> dd
{'C': 'codeblock', 'JAVA': {1: 'ecillipe', 2: 'netbeans'}, 'python': {1: 'pycham', 2: 'sublimetext', 3: 'edit++'}}
>>> dd[C]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dd[C]
NameError: name 'C' is not defined
>>> dd[1]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dd[1]
KeyError: 1
>>> dd['C']
'codeblock'
>>> dd['JAVA']
{1: 'ecillipe', 2: 'netbeans'}
>>> dd['JAVA'][1]
'ecillipe'
>>> dd['JAVA'][2]
'netbeans'
>>> dd['python'][pycham]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    dd['python'][pycham]
NameError: name 'pycham' is not defined
>>> dd['python'][1]
'pycham'
>>> dd1={'C': 'codeblock', 'JAVA': {'E': 'ecillipe', 'N': 'netbeans'}, 'python': {'P': 'pycham', 'S': 'sublimetext', '': 'edit++'}}
>>> {'C': 'codeblock', 'JAVA': {'E': 'ecillipe', 'N': 'netbeans'}, 'python': {'P': 'pycham', 'S': 'sublimetext', 'D': 'edit++'}}
{'C': 'codeblock', 'JAVA': {'E': 'ecillipe', 'N': 'netbeans'}, 'python': {'P': 'pycham', 'S': 'sublimetext', 'D': 'edit++'}}
>>> dd2={'C': 'codeblock', 'JAVA': {'E': 'ecillipe', 'N': 'netbeans'}, 'python': {'P': 'pycham', 'S': 'sublimetext', 'D': 'edit++'}}
>>> dd2
{'C': 'codeblock', 'JAVA': {'E': 'ecillipe', 'N': 'netbeans'}, 'python': {'P': 'pycham', 'S': 'sublimetext', 'D': 'edit++'}}
>>> dd2['JAVA']['N']
'netbeans'
>>> DD2['python']['P']
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    DD2['python']['P']
NameError: name 'DD2' is not defined
>>> dd2['python']['P']
'pycham'
>>> 
