#variable in pyton
name="bhuvan"
print (" my name is",name)
'''

#creation of empty list
li=[]
print(li)
print(type(li))

#append we can add only one element at the time

li.append(25)
print(li)

#extend
li.extend([12,25.54,54,45,12])
print(li)
print(len(li))

#creation of empty list
li=[12,25,45,50.5,90,12]
print(li.count(12))


li=[12,25,45,50.5,90,12]
print(li.count(45))

#replacing thr list element
li[3]=1000
print(li)


#list
lis=li.copy()
li.append(60)
print(li)
print(lis)

#insert
print(li.insert(3,35))
print (li)


#slicing[start value:End value]

print(li[1:5])
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
print(li.remove(90))
print(li)
li.clear()
print(li)
'''


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









      

