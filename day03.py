#Datatypes
#Integer
n = 123
print(n)         #123
print(type(n))   #<class 'int'>
a = 123        
a = 0b1011
b = 0o761
c = 0xF109
print(a)         #value
print(type(a))   #<class 'int'>
print(b)         #value
print(type(b))   #<class 'int'>
print(c)         #value
print(type(c))   #<class 'int'>

#Float
a = 12.34
b = 12.34e2
c = 12.34e-2
print(a, type(a))  #12.35 <class 'float'>
print(b, type(b))  #1234.0 <class 'float'>
print(c, type(c))  #0.1234 <class 'float'>

#Complex
a = 3 + 4j
b = 0j
c = 7j
print(a, type(a), type(a.real), type(a.imag))  #(3+4j) <class 'complex'> <class 'float'> <class 'float'>
print(b, type(b), type(a.imag))                #0j <class 'complex'> <class 'float'> <class 'float'>
print(c)                                       #7j

#Bool
a = True
b = False
print(type(a))  #<class 'bool'>
print(type(b))  #<class 'bool'>
c = a + b 
print(c)        #1
print(type(c))  #<class 'int'>

#NoneType
a = None
print(a)        #None
print(type(a))  #<class 'NoneType'>

#List
a = []
b = list() 
c = [1,2,3,4,5]
d = list([1,2,3,4,5])
e = list((1,2,3,4,5))
f = list('srija')
g = list(range(1,6))
h = list({1,2,3,4})
i = list({1:'a', 2:'b', 3:'c'})
print(a, type(a))  #[] <class 'list'>
print(b)           #[]
print(c)           #[1, 2, 3, 4, 5]
print(d)           #[1, 2, 3, 4, 5]
print(e)           #[1, 2, 3, 4, 5]
print(f)           #['s', 'r', 'i', 'j', 'a']
print(g)           #[1, 2, 3, 4, 5]
print(h)           #[1, 2, 3, 4]
print(i)           #[1, 2, 3]

#Tuple
a = (1,2,3,4,5)
b = 1,2,3,4
c = True, 1, 3j, None
d = (5.6)
e = (1+3j)
f = (1)
g = (True)
h = (3j)
i = 1,
j = True,
k = 3j,
l = tuple() 
m = tuple([1,2,3,4,5])
n = tuple([2,3,4])
o = tuple({4,5,6})
p = tuple({1:'a', 2:'b', 3:'c'})
q = tuple(range(1,6))
r = tuple('srija')
print(a, type(a))  #(1, 2, 3, 4, 5) <class 'tuple'>
print(b, type(b))  #(1, 2, 3, 4) <class 'tuple'>
print(c, type(c))  #(True, 1, 3j, None) <class 'tuple'> 
print(d, type(d))  #5.6 <class 'float'>
print(e, type(e))  #(1+3j) <class 'complex'>
print(f, type(f))  #1 <class 'int'>
print(g, type(g))  #True <class 'bool'>
print(h, type(h))  #3j <class 'complex'>
print(i, type(i))  #(1,) <class 'tuple'>
print(j, type(j))  #(True,) <class 'tuple'>
print(k, type(k))  #(3j,) <class 'tuple'>
print(type(l))     #<class 'tuple'>
print(m)  #(1, 2, 3, 4, 5)
print(n)  #(2, 3, 4)
print(o)  #(4, 5, 6)
print(p)  #(1, 'a', 2, 'b', 3, 'c')
print(q)  #(1, 2, 3, 4, 5)
print(r)  #('s', 'r', 'i', 'j', 'a')

#Set 
a = {}
b = set() 
c = {1,2,3,4}
d = {1,1,2,2,2,3,3,3,4,4,4,4}
e = {(1,2,3), 4, True}
f = {(1,2,3), 4, True}
g = {{1:'a', 2:'b'}, 4, True}
h = {(1,2,3), 4, True} 
i = {'srija', 4, True}
j = set(1,2,2,3,3,4,4,4)
k = set([1,2,2,3,3,3])
l = set((4,4,5,5,6,6))
m = set({1:'a', 1:'b', 1:'c'})
n = set('sssrijaaa')
o = set(range(1,6))
print(a, type(a))  #{} <class 'dict'>
print(b, type(b))  #set() <class 'set'>
print(c)  #{1, 2, 3, 4}
print(d)  #{1, 2, 3, 4}
print(e)  #error
print(f)  #error
print(g)  #error
print(h)  #{(1, 2, 3), 4, True}
print(i)  #{'srija', 4, True}
print(j)  #error
print(k)  #{1, 2, 3}
print(l)  #{4, 5, 6}
print(m)  #{'a', 'b', 'c'}
print(n)  #{'s', 'r', 'i', 'j', 'a'}
print(o)  #{1, 2, 3, 4, 5}

#Dict 
a = {}
b = dict() 
c = {1,2,3,4,5}
d = {1:'a', 2:'b', 3:'c', 4:'d'}
e = {[1,2,3]:'a', 2:'b'}
f = {{1,2,3}:'a', 2:'b'}
g = {'srija':'a', 2:'b'}
h = {(1,2,3):'a', 2:'b'}
i = {1:'a', 1:'b', 1:'c', 2:'x', 2:'y'}
j = dict(1,2,3,4,5)
k = dict(1:'a', 2:'b')
l = dict({1:'a', 2:'b'})
m = dict([(1,2), [3,4], (5,6)])
n = dict( ((1,2),[3,4])) 
print(a, type(a)) #{} <class 'dict'>
print(b) #set() <class 'set'>
print(c) #{1, 2, 3, 4, 5}
print(d) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(e) #error
print(f) #error
print(g) #{'srija': 'a', 2: 'b'}
print(h) #{(1, 2, 3): 'a', 2: 'b'}
print(i) #{1: 'c', 2: 'y'}
print(j) #error
print(k) #error
print(l) #{1: 'a', 2: 'b'}
print(m) #{1: 2, 3: 4, 5: 6}
print(n) #{1: 2, 3: 4}

#String
a = 'srija'
b = "srija"
c = '''s
r
i
j
a'''
print(a)  #srija
print(type(a)) #<class 'str'>
print(b) #srija
print(type(b)) #<class 'str'>
print(c)  #s
print(type(c)) #<class 'str'>

#Range
a = range(5)
b = range(3,7)
c = range(3, 9, 2)
d = range(9,3,-1)
print(a)  #range(0, 5)
print(*a) #0 1 2 3 4
print(*b) #3 4 5 6
print(*c) #3 5 7
print(*d) #9 8 7 6 5 4

#Slicing
a = [4,1,2,3,5] 
print(a[:])  #[4, 1, 2, 3, 5]
print(a[:3]) #[4, 1, 2]
print(a[2:]) #[2, 3, 5]
print(a[::-1]) #[5, 3, 2, 1, 4]
print(a[:3:-1]) #[5]
print(a[3::-1]) #[3, 2, 1, 4]
b = {3,2,4,6}   
print(b[:3])   #error
c = {1:'a', 2:'b', 3:'c'}
print(c[:2])   #error