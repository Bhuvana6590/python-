# for loop
'''
#1
x=int(input('enter number'))
for i in range(x):
print(i)

#2 
for i in range(1,11):
    print(i)
'''
'''
# odd
for i in range(1,10,2):
    print(i)
'''

'''
#3 even
for i in range(2,10,2):
    print(i)

#4 negative number

for i in range(-11,0):
    print(i)
    
#5
x=[1,2,3,4,5,6,7]
for i in x:
    if i%2==0:
        print(i)


x=[34,45,6,7,6]
for i in x:
    print(i)
    

n=int(input('Enter the number'))
for i in range(1,11):
    c=n*i
    print(n,"*",i,"=",c)'''

#even numbers
x=[1,2,3,4,5,6,7]
for i in x:
    if i%2==0:
        print('the even number=',i)

x=[1,2,3,4,5,6,7]
for i in x:
    if i%2==1:
        print('the odd number=',i)

#vowels and not vowels
x=input('the enter the string:')
for x in (a,e,i,o,u):
    print('the vowels from the entered string')



a=int(input('enter number:',))
b=1
for i in range(1,a+1):
    b*=i
    print(i)
    print('the factorial of:',b)

 

    





