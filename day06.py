# #append()
l = ['a', 'b', 'c']
l.append(34) 
l.append(34.3)
l.append(4+3j)
l.append(True)
l.append(None)
l.append([0,1,2])
l.append((3,4,5))
l.append({6,7,8})
l.append({9:'a', 10:'b', 11:'c'})
l.append('rakesh')
l.append(range(12,15))
print(l) #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3, 4, 5), {8, 6,7}, {9: 'a', 10: 'b', 11: 'c'}, 'rakesh', range(12, 15)]

# extend() 
l = ['a', 'b', 'c']
l.extend(34)
l.extend(34.3)
l.extend(4+3j)
l.extend(True)
l.extend(None)
l.extend([0,1,2])
l.extend((3,4,5))
l.extend({6,7,8})
l.extend({9:'a', 10:'b', 11:'c'})
l.extend('rakesh')
l.extend(range(12,15))
print(l)  #['a', 'b', 'c', 'r', 'a', 'k', 'e', 's', 'h', 12, 13, 14]


# insert() 
#positive index
l = ['a', 'b', 'c', 'd']
l.insert(2, 'hi')
print(l) #['a', 'b', 'hi', 'c', 'd']
l.insert(10, 'hi')
print(l) #['a', 'b', 'hi', 'c', 'd', 'hi']
#negative index
l = ['a', 'b', 'c', 'd', 'e']
l.insert(-2, 'hi') 
print(l) #['a', 'b', 'c', 'hi', 'd', 'e']
l.insert(-100, 'hi')
print(l) #['hi', 'a', 'b', 'c', 'hi', 'd', 'e']

#pop()
l = [1, 2, 3, 4, 5]
a = l.pop()
print(a, l) # 5 [1, 2, 3, 4]
b = l.pop(2)
print(b, l) # 3 [1, 2, 4]
#c = l.pop(7)
del l[0]
print(l) # [2, 4]

# remove()
l = [1, 2, 3, 4]
a  = l.remove(3)
print(a, l) # None [1, 2, 4]
#print(l.remove(5))

# clear()  
l = [1, 2, 3, 4, 5]
l.clear()
print(l) # []

# reverse() 
l = [1, 2, 3, 4, 5]
print(id(l)) 
a = l.reverse()
print(a, l) #None [5, 4, 3, 2, 1]
print(id(l))

# sort()  
l = [1,4,2,6,5,3]
print(id(l))
a = l.sort() 
print(a, l) #None [1, 2, 3, 4, 5, 6]
print(id(l))
l = [50,10,40,20,30]
print(l.sort(reverse=True))
print(l) #[50, 40, 30, 20, 10]


# index() 
l = [1, 2, 1, 4, 6, 1, 7]
print(l.index(1)) # 0
print(l.index(1, 3)) # 5
#print(l.index(1, 3, 5))
#print(l.index(9))

# count() 
l = [1, 2, 1, 4, 1, 6, 7, 1]
print(l.count(1)) #4
print(l.count(9)) #0


# index() 
l = (1, 2, 1, 4, 6, 1, 7)
print(l.index(1)) #0
print(l.index(1, 3)) #5
# print(l.index(1, 3, 5))
# print(l.index(9))

# count() 
l = (1, 2, 1, 4, 1, 6, 7, 1)
print(l.count(1)) #4
print(l.count(9)) #0
