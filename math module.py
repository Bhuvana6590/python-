'''
print(help('keywords'))
      
print(help('math'))

#importing the module
import math
print(math.sqrt(81))

'''
''''
#factorial
import math as m
n=int(input('enter the number:'))
print(f'factorial of{n}is {m.factorial(n)}')

'''
#importing the module to get all packages
from math import*
# ceil and floor
print(ceil(45.01))
print(floor(45.09))

#remainder and GCD
print('remainder value is"',remainder(45,2))
# GCD- Greatest common divisor
print('GCD is:',gcd(24,12))
'''

print('sum of values is:',fsum([10,20,30,40]))

#trignometric functions
from math import*
print('sine value is=',sin(0))
print('cosine value is=',cos(0))
print('tan value is=',tan(0))

'''
'''
#Logarithemic functions
print(log(6))
print(log(36))
print(log(1000))
'''
'''
#constant function

print('pi value is=',pi)
print('euler value is=',e)
print('tau value is=',tau)
'''
'''
# nan and infinity
print('not a number=',nan)
print('infinity=',inf)

#cmath complex mathematical- it returns the result in complex value
import cmath as c
print(c.sqrt(49))

'''
'''
#calender module----- It will display the particular mention year  calendar

import calendar
print(calendar.calendar(2025))
print(calendar.calendar(2050))
'''
'''
#calender module
import calendar as cal
year=int(input('enter the year:'))
print(cal.calendar(year))

'''
'''
import calendar as cal
year=int(input('enter the year='))
month=int(input('enter the month='))
print(cal.month(year,month))


# to check the year is leap year using calender module
import calendar as cal
y=int(input('enter the year='))
if(cal.isleap(y)):
    print(y,'is a leap year')
else:
    print(y,'is not a leap year')
'''


# import date and time
import datetime as dt
print(dt.datetime.now())

from datetime import*
d=date.today()#start with today
print(d)


# to display only time
from datetime import*
dt=datetime.now()
print('current time:',dt.strftime('%H:%M:%S'))
print('current time:',dt.strftime('%b:%b:%y'))
print('current time:',dt.strftime('%B:%A:%Y'))

d,m,y=[int(x)for x in input('enter the date=').split('/')]
dt=date(y,m,d)
print(dt.strftime('day %w of the week,this is%A'))












