# to check the whether the given no is odd or even
'''
no=int(input('enter the number:'))
if(no%2==0):
    print(no,'is an even number')
else:
    print(no,'is an odd number')
'''
    
'''
age=int(input('enter the age:'))
if(age>18):
    print('eligible to vote')
else:
    print('not eligible to vote')

'''

'''
#if -elif else
x=int(input('enter number'))
if x>56:
    print(' the number is positive')
elif x<0:
    print ('the number is negative')
else:
    print('no is zero')
'''

'''
# nested condition


if(x>0):
    if(x>25):
        print(' no greater than 25')
    else: 
        print('the number less than  25')
else:
    print('the number is zero')
'''
'''
# Assignment
#MAx of two numbers

x=int(input('enter number 1:'))
y=int(input('enter number 2:'))
if(x>y):
    print('no 1 is greater')
else:
    print('no 1 is greater')
    '''

'''
# given character in vowel or not

x=(input('enter the word:'))
if x in ('a','e','i','o','u'):
    print('the string has vowels')
else:
    print('the string doesnt have vowels')

'''

'''5
#check the string is upper or lower case
x=(input('enter the word:'))
if x.isupper():
    print('the string is uppercase')
else:
    print('the string is lower case')
    
'''

#Calculator function
'''
l=int(input('enter number 1:'))
m=int(input('enter number 2:'))
n=input("enter choice:'add','sub','multiply','divide':")
if n=='add':
    print("Addition :",l+m )
elif n=='sub':
    print("subtraction :",l-m )
elif n=='multiply':
    print("multiplication :",l*m )
else:
    print("division :",l/m )
'''

'''
a=int(input('enter number:'))
if a==2:
   print('its a prime number')
elif(a%2==0):
    print('its a prime')
elif(a%3==1):
    print('its not a prime')
elif(a%5==1):
    print('its not a prime')
else:
    print('not a prime ')
    
'''

# palindrome
x=(input('enter the word:'))
if(x==x[::-1]):
   print('the enter word is palindrome')
else:
   print('the enter word is not palindrome')





   
a=int(input('enter given marks:'))
if(a>=90 or a==100):
   print('the grade is distinction')
elif(a>=80 or a==90):
   print('A GRADE')
elif(a>=70 or a==60):
   print('B GRADE')
elif(a>=60 or a==40):
   print('c GRADE')
elif(a>=100 or a<=40):
   print('No grades defined') 
   
   




   


    
    
    
    
