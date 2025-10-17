'''import re
s='Hello World'
res=re.findall(r'^He',s)
print(res)

import re
s='Hello World'
res=re.findall(r'^he',s)
print(res)


#A python progfram to create a regular expression to search
#whether a given string is starting with "he' or not
import re
s='Hello World'
res=re.findall(r'^He',s)
if res:
    print("the string starts with 'He'")
else:
    print("the string dindnt start with 'He'")
    

#$ String ends with or not
import re
s='Hello World'
res=re.findall(r'd$',s)
if res:
    print("the string end with 'd'")
else:
    print("the string didnt ends with 'd'")


#A python program to create a regular expression to search
#whether a given String is ending with 'world' or not
import re
s='Hello World'
res=re.search(r'World',s)
if res:
    print(res,"\n'the particular string is not available")
else:
    print("the particular String is not Available")
    

import re
s='Python program'
result=re.search(r'program$',s,re.IGNORECASE)
if result:
    print(result,"\nString ends with 'program'")
else:
    Print("String does not ends with program'")
    

#python program to create a regular expression to retrive
    #marks and names from a given string
import re
s='Suba got 80.4 Marks,Parthi got 755 Marks, whereas Faizal got 88'
marks=re.findall('\d{3}',s)
print(marks)
names=re.findall('[A-Z][a-z]*',s)
print(names)

import re
s='Suba got 80.4 Marks,Parthi got 755 Marks, whereas Faizal got 88'
marks=re.findall(r'\d+\.\d+',s)
print(marks)
names=re.findall('[A-Z][a-z]*',s)
print(names)

#puthon program to create a regex that reads
#email ids from a text file
import re
s='kumbhmela will be conducted at Ahmedabad in India'
res=re.sub(r'Ahmedabad','Allahabad',s)
print (res)
'''
import re
print(re.search("flower","picking flowers in the flower fields"))
print(re.match("flower","flower field"))
print(re.findall("flower","picking flowers in the flower field"))
for match in re.finditer("flower","Picking flowers in the flower field"):
   print(match)
    
