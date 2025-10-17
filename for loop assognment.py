'''
string='hello'
mylist =[]
for letter in string:
    mylist.append(letter)
print(mylist)
'''
'''
#list comprehension
string='hello'
mylist= [letter for letter in string]
print(mylist)
'''
'''
mylist=[x for x in 'ameen']
print(mylist)
'''
'''
lis=[]
for i in range(0,11):
    lis.append(i**2)
print(lis)
'''
'''
lis=[num**2 for num in range(0,11)]
print(lis)
'''
'''
l=[2,4,5,6]
l.append(9)
print(l)
'''
'''
#adding if statement
lis1=[x for x in range(0,11)if x%2==0]
print(lis1)
'''
'''
celcius=[0,22,34,56,7,45]
farenheit=[((9/5)*temp+32)for temp in celcius]# faherheit formula-- (9/5)*var+32
print(farenheit)
'''
'''
mylist=[x if x%2==1 else 'even' for x in range(0,11)]
print(mylist)

mylist=[]
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)'''




'''
a=10
for i in range(a):
    if i%2==0:
        print('even number',i)
    else:
        print('is not a even number')'''

'''        
#vowels

x=input('enter the word=')
for i in range(len(x)):
    if x[i] in ('a','e','i','o','u'):
        print('the is vol',x[i])


x=input('enter the word=')
for i in range(len(x)):
    if x[i] not in ('a','e','i','o','u'):
        print('not a is vol',x[i])'''
li=[1,3,7,8,3]
for i in range(len(li)):
    if i>=1 in li:
        print('the greatest no ')



















        
    
            




    
    

