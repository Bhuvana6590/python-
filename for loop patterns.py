'''# increasing triangle
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


print(' decreasing triangle '.center(50,"="))


#decreasing triangle
n=5
for i in range(n):
    for j in range(i,n):
        print('*', end='')
    print()
    
print(' right sided triangle '.center(50,"="))
#right sided triangle
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()

print(' left sided triangle '.center(50,"="))
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()


'''
print(' reverse hill pattern '.center(50,"="))
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print('*', end='')
    for j in range(i,n-1):
            print('*',end='')
    print()

    '''
print(' diamond '.center(50,"="))
n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*', end='')
    for j in range(i,n):
            print('*',end='')
    print()
'''

'''(' hill pattern '.center(50,"="))
n=4
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()
n=4
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()'''






  
