#Array

#syntax
#variable name=array.array('Data Type',sequence)
'''
import array
x=array.array('i',[12,7,5,34,65])
print('Array value is:',x)
print(type(x))

import array as ar
res=ar.array('d',(23,4,6,8,13))
print('Result is:',res)

import array as ar
res=ar.array('I',(5,7,9,12,14))
print('result is:',res)

#string-unicode character - collection of characters or numbers enclosed
#within a single ,double or triple quotation
res=ar.array('u',('12345'))
print('result is :',res)


res=ar.array('u',('C,C++,java,Python'))
print('Result is:',res)
'''
#array operations
import array as ar
a=ar.array('I',(5,7,9,12,14))
print('Result is:',a)
a.append(12)
print('after appending:',a)

a.extend([13,45,60,90])
print(a)

a.insert (3,10)
print(a)
print(max(a))
print(min(a))
print(sum(a))

a.reverse()
print(a)


print(a[-1])



