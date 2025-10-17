
vechile=('car', 'bike','cycle','scooty')
print(vechile)
#Adding values to the tuple
(nano,*scooty,honda)=vechile   
print(nano, scooty, honda)
print(honda)
print(scooty)


#tuple( convert tuple into list and then again into tuple)
book=tuple(("tamil","science","maths","bhuvi"))
print(book)
print(type(book))
x=list(book)
print(type(x))
x.append('songs')
print(x)
x.remove('bhuvi')
print(x)
y=tuple(x)
print(y)
print(type(y))





