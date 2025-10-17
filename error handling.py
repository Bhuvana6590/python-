#Error handling454
#refer notes from whatsapp
''' 
x=90
y='80'
print(x+y)

import Math

tu=(2,3,4,5)
tu.append(8)

#zero division error
x=int(input('enter the number:'))
y=int(input('enter the number:'))
print(x/y)

#Example 4
try:
    x=float(input("enter the number:"))
    y=int(int('enter the number:'))
    print(f'value of {x} and {y} is {x/y}')
except:
    print('error occured')

#example 6
try:
    x=float(input("enter the number:"))
    y=int(input('enter the number:'))
    print(f'value if{x} and {y}is {x/y}')
except ZerodivisionError  as a:
    print(a)

# how to handle multiple exception
try:
    x=int(input('enter the number:'))
    y=int(input('enter the number:'))
    print(x/y)
except zerodivisionerror as a:
    print(a)
except Nameerror as n:
    print(n)

x=50
if x%2==0:
print(x,'is even')
else:
    print(x,'is odd')


try:
    x=70
    if x==0:
        print('true')
    else:
        print('false')
except:
    traceback.print_exc()
    '''
# how to handle the error in list datatype
l=[35,50.45,'aruvi',90,25]
try:
    l.append(3)
    l.extend([80,35,89])
    print(l[11])
expect 
