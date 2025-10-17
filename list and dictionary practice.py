#variable in python
name="varahi"
print('my name is',name)
name="bhuvana"
print('my name is',name)
name="Raji"
print('my name is',name)

#implicit type conversion
x=1000
print(type(x))
f=80.45
print(type(f))

#Complex-real+imaginary no
c=80+3j
print(type(c))
com=50+3j
print(type(com))

#exicit type conversion
f=80.45
print(int(f))
print(complex(f))

#creation of empty list
li=[]
print(li)
print(type(li))

#append
li.append(25)
print(li)

#extend
li.extend([12,24,36,48])
print(li)
print (len(li))

#create of empty list
li=[12,24,36,48]
print(li)
print(li.count(48))
print('sum is',sum(li))
print('maximum is',max(li))
print('mimimum is',min(li))
print(li.index(36))

lis=li.copy()
li.append(60)
print (li)

#insert
print(li.insert(3,35))
print (li)

#slicing[start value:End value]

print(li[0:5])
print(lis)
print(li[:4])
print(li[2:])
print(li[:-1])
print(li[::-1])

#sort
li.sort()
print(li)
li.reverse()
print(li)

#how to delete thr list element
del li[0]
print (li)
li.pop()
print(li)
li.clear()
print(li)


#creation of empty dictionary
dic={}
print(type(dic))

dic['name']='kani'
print(dic)
dic.update({'degree':'M.E','native':'tenkasi'})
print(dic)


# how to access the dictionary element using key
print('my name is',dic['name'])
print('i have completed',dic.get('degree'))
print(dic.keys())
print(dic.values())
print(dic.items())
del dic['degree']
print(dic)
print(dic.pop('native'))
print(dic)
dic.clear()
print(dic)


# how to access the dictionary element using key
print('my name is',dic['name'])
print('i have completed',dic.get('degree'))
print(dic.keys())


#creation of empty dictionary
dic={}
print(type(dic))

dic['name']='kani'
print(dic)
dic.update({'degree':'M.E','native':'tenkasi'})
print(dic)



