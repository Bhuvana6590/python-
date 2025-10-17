#creation of empty set
a=set()
print(a)
print(type(a))


#add
a.add(4)
print(a)

#update
a.update({3,4,9,10,12})
print(a)
#union
b={4,10,6,"A",12,24}
print(b)
print('union value is:',a|b)
print(a.union(b))

b={4,10,6,"a",12,24}
print(b)
print('union value is:',a|b)
print(a.union(b))

#intersection
print(a&b)
print(a.intersection(b))
#difference
print(a-b)
print(a.difference(b))

#Symmetric difference
print(a^b)
print(a.symmetric_difference(b))





