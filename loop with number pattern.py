'''print('increasing triangle with numbers '.center(50,"=")) 
n=5
p=0
for i in range(n):
    for j in range(i+1):
        print(p,end='')
    p+=2
    print()

print('left sided triangle in numbers '.center(50,"=")) 

n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print(p,end='')
    print()
    p+=1
    print()

print('hill pattern '.center(50,"="))
n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
    for j in range(i+1):
        print(p,end='')
    print()
    p+=1
    print()


print(' reverse hill pattern '.center(50,"="))
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print(p,end='')
    for j in range(i,n-1):
        print(p,end='')
    print()
    p+=1
    print()


print('increasing triangle pattern with number row odd and even '.center(50,"="))


n=5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print('1',end='')
        else:
            print('2',end='')
    print()


print('Diamond pattern with increasing rows '.center(50,"="))

n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(p,end='')
    for j in range(i+1):
        print(p,end='')
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print(p, end='')
    for j in range(i,n):
            print(p,end='')
    p+=1
    print()'''


print('ABCD pattern '.center(50,"="))
n=5
for i in range(n):
    p=65
    for j in range(i,n):
        print('',end='')
    for j in range(i):
        print(chr(p),end='')
        p+=1
    for j in range(i+1):
        print(chr(p),end='')
        p+=1
    print()



