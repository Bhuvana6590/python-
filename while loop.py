#while condition is used when the condition true it will print thr output it its false it will not print the output

#less method

'''#1 number 1 to 10 print
i=1
while i<=10:
    print(i)
    i+=1

#2 0dd numbers
x=1
while x<=10:
    print(x,'odd number')
    x+=2

    
#3 even numbers

x=2
while x<=10:
    print(x,'even number')
    x+=2



#4 (0,-10 negative number)
y=0
while y>=-10:
    print(y)
    y-=1

#5 string name print
x=input('enter name:')
z=0
while z<len(x):
    if x[z] not in ('a','e','i','o','u','A','E','I','O','U'):
        print(x[z],end='')
        z+=1

#6list in len4 print
x=['saran','karthi','ganesh','sk']
f=0
print(len(x))
print(x[0])
while f<len(x):
    if len(x[f])<4:
           print(x[f])
    f+=1


#odd or even
x=int(input('enter the number'))
z=0
while z<=x:
    if z%2==0:
        print(z,'even number')
    else:
        print(z,'odd number')
    z+=1

#max or min
x=[1,2,6,8,9,4,3]
l=[]

i=0
while i<len(x):
    l.append(x[i])
    i+=1

l.sort()
print('the smallest no. :',l[0])

#factorial of numbers
#multiplication

x=int(input('enter the number:'))
fact=1

i=1
while i<=x:
    fact=fact*i
    i+=1
print("the factorial of",x,"is" ,fact)

#multiplication
n=int(input('Enter a value'))
i=1
while i<=10:
    #print(f'{i}x{n}={n*i}')format function
    print(i,'x',n,'=',n*1)
    i+=1
'''
#printing the name
i=1
x='bhuvana'
while i<=10:
    print(x)
    i+=1

    


    
    




