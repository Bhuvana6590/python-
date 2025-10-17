'''
#first x value not working

def total():
    s=int(input('enter number'))
    p=int(input('enter the number'))
    print(s+p)

total()
'''
'''
def addition():
    print(a+b)
def subtraction ():
    print(a-b)
def multiplication():
    print(a*b)
def division ():
    print(a/b)

a=int(input('enter number'))
b=int(input('enter number'))
addition()
subtraction()
multiplication()
division()




#def by position
def total(x,y):
    z=x+y
    print(x)
    print(y)
    print(z)
    
total(10,20)

#def by keyword
def total(x,y):
    z=x+y
    print('value of x is',x)
    print('value of y is',y)
    print(z)
total(y=10,x=20)

#define
def total(x,y=45):
    z=x+y
    print('value of x is',x)
    print('value of y is',y)
    print(z)
total(56)

#variable
def total(x,y,*c):
    print('value of x',x)
    print('value of y',y)
    print('value of c',c)
total(10,20,30,40,50)
'''

'''
#addition program
def addition (x,f):
    for i in x:
        f+=i
    print('sum of x is',f)
x=[4,6,7,8,3,4]
f=0
addition(x,f)
'''
'''
#return method
def addition(x,y):
    for i in x:
        y+=i
    return y
x=[3,4,5,6]
y=0
print('sum of y is',addition(x,y))

'''
'''
#factorial
def factorial (x,y):
    for i in range(1,x+1):
        y*=i
    return(y)
x=5
y=1
print ('factorial number:',factorial(x,y))        

'''
def fibonacci (x,a,b):
    for i in range(2,x+1):
        c=a+b
        a=b
        b=c
    return('fibonacci',c)
x=6
a=0
b=1
print (fibonacci(x,a,b))

#Example program on list
#sum
def list():
    print(sum(x))

def listadd(x,f):
    for i in x:
        f+=1
    print('sum of x is',f)

def listmultiplication(x,f):
    for i in x:
        f*=1
    print('mul of x is',f)
































































x=[1,2,3,4,5]

list()

x=[4,5,6]
f=0
listadd(x,f)

x=[3,4,5]
f=1
listmultiplication(x,f)


#example
x=[1,2,3,4,5]
f=0
for i in x:
    f+=1
    print(f)
    









    
               
