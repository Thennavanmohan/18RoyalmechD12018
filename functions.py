
Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> l=[1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> l.append([5])
>>> l
[1, 2, 3, 4, [5]]
>>> a=['a','b','c','d']
>>> a
['a', 'b', 'c', 'd']
>>> a.index('a')
0
>>> a.index('b')
1
>>> a.index('c')
2
>>> a.index('d')
3
>>> a
['a', 'b', 'c', 'd']
>>> a.remove('d')
>>> a
['a', 'b', 'c']
>>> a.insert(3,'e')
>>> a
['a', 'b', 'c', 'e']
>>> a.insert(4,a)
>>> a.insert(4,'a')
>>> a
['a', 'b', 'c', 'e', 'a', [...]]
>>> a.count('a')
2
>>> len(a)
6
>>> a+=['f','g']
>>> a
['a', 'b', 'c', 'e', 'a', [...], 'f', 'g']
>>> b=[6,7]
>>> b*=2
>>> b
[6, 7, 6, 7]
>>> print(len(b))
4
>>> len(b)
4
>>> dict={1:'thennavan',2:'Roy',3:'chakravarthy'}
>>> dict
{1: 'thennavan', 2: 'Roy', 3: 'Chakravarthy'}
>>> dict[1]
'thennavan'
>>> dict[2]
'Roy'
>>> dict[3]
'chakravarthy'
>>> m={'a':10,'b':20,'c':30}
>>> m
{'a': 10, 'b': 20, 'c': 30}
>>> m['a']
10
>>> m['b']
20
>>> m['c']
30

