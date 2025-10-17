'''#lambda function
A lambda function is  also known as an anonymous function
it is small unnamed function defined using lambda keyword
it is often used for short,simpleoperations and can take multiple arguements,but can have only one expressions

Example
  lambda Arguments:expression
  
#lamba function
#sum
f=lambda x,y:x+y

print('sum of two in number',f(3,7))

#sub
a=lambda x,y:x-y
print('sub',a(53,6))

#mul
a=lambda x,y:x*y
print('mul',a(7,6))

#divi
a=lambda x,y:x/y
print('divi',a(5,8))

#mul
a=lambda x:x*x
print('mul',a(7))



def myfunc(n):
    return lambda a:a*n

mytripler=myfunc(3)

print(mytripler(11))

print(3*11)




def add(x,y):
    print(f'the value of{x} and {y} is {x+y}')
add(80,25)
add(100,25) 


# sum of numbers using lambda function

addition=lambda x,y:x+y
print(addition(10,20))


#types of lambda function
filter
map
reduce

#filter syntax
filter(lambda arguement:expression)

x=[10,23,45,78,56,91]
odd=tuple(filter(lambda x1:x1%2!=0,x))
print(odd)

x=[10,23,45,78,56,91]
even=tuple(filter(lambda x1:x1%2==0,x))
print(even)


x=[10,23,75,60,80,45,67]
odd=set(filter(lambda x1:x1%2!=0,x))
print(odd)
'''
#map

li=list(range(10))
square=list(map(lambda x2:x2**2,li))
print(square)










  













