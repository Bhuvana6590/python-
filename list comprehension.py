'''
# normal way of declaration using loop
string= 'hello'
mylist=[]
for letter in string:
    mylist.append(letter)
print(mylist)

'''
'''
#list comprehension
string= 'hello'
mylist=[letter for letter in string]
print(mylist)
'''

'''

fruits=['mango','cucumber','apple','mint','banana','gauva','musk melon']
new=[]
for i in fruits:
    if 'm' in i:
        new.append(i)
print(new)


#syntax- element for element in iterable object
mylist=[x for x in 'ameen']
print(mylist)


#square of a number using for loop
lis=[]
for i in range (0,11):
    lis.append(i**2)
print(lis)


#square of a number using list comprehension
lis=[num**2 for num in range(0,11)]
print(lis)


l=(2,4,5,6)
l.append(9)
print(l)  # error will come because the data given in tuple

#adding if statement
lis1=[x for x in range(0,11) if x%2==0]
print(lis1)


#farenheit formula  --- (9/5)*var+32
celcius=[0,22,34,56,7,45]
farenheit=[((9/5)*temp+32) for temp in celcius]
print(farenheit)


#debugging previous code
celcius=[0,22,34,56,7,45]
farenheit=[]
for temp in celcius:
    farenheit.append(((9/5)*temp+32))
print(farenheit)


#if else statement in list comprehension(odd)
mylist=[x if x%2==0 else 'odd'for x in range(0,11)]
print(mylist)


#if else statement in list comprehension(even)
mylist=[x if x%2==1 else 'even' for x in range(0,11)]
print(mylist)

mylist=[]
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
    print(mylist)
    

#in list comprehension
l=[x*y for x in [2,4,6] for y in [1,10,100]]
print(l)


li='c,c++,java,python'
print(li.split(','))


# a python prigram to accept a group of strings sepereated by commas and displays
#list comprehension

lis=[x for x in input('enter the strings:').split(',')]
print('list element is:',lis)

# evaluate the expression
x=eval(input('enter the expression:'))
print('result:',x)

#while program

x=input('enter the string')
y=0
while y<len(x):
    if x[y]in('a','e','i','o','u','A','E','I','O','U'):
        print(x[y],end='')
    y+=1
    
#evaluate expression in list
x=eval(input('enter the expression:'))
print('result:',list(x))

#evaluate expression using string formatting
x=eval(input('enter the expression'))
print('result:%f'%x)
print('result is:',x)





mylist=[]
y=1
for x in [3,4,5,6,7,8,9]:
    mylist.append(x+y)
print(mylist)
y+=1

'''

li=[3,4,5,6,7,8,9]
new_result=[x+10 for x in li]
print(new_result)

li=[3,4,5,6,7,8,9]
new_result=[x-1 for x in li]
print(new_result)

li=[3,4,5,6,7,8,9]
new_result=[x*100 for x in li]
print(new_result)

li=[3,4,5,6,7,8,9]
new_result=[x%2 for x in li]
print(new_result)

