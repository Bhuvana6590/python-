'''
f=open('C:\\Users\\asnat\\fileh.txt','r')
print(f.read())


#readlines-----read single line read
f=open('C:\\Users\\asnat\\fileh.txt','r')
print(f.readline()

#readlines ----print the data in paragraph by not moving into new line 
f=open('C:\\Users\\asnat\\fileh.txt','r')
print(f.readlines()


#w---write the data into the file
w=open('C:\\Users\\asnat\\bhuvifile.txt','w')
print(w.write('write the data into file'))
w.close()

w=open('C:\\Users\\asnat\\bhuvifile.txt','w')
print(w.write('remove the previous data'))
w.close()
'''
#append-- to add the data
w=open('C:\\Users\\asnat\\bhuvifile.txt','a')
print(w.write('\na-write the data into file'))
w.close()

#'r+'-- for both read and write the data
r=open('C:\\Users\\asnat\\bhuvifile.txt','r+')
print(r.read())
print(r.write('\nr+-for both read and write operations'))
r.close()

#csv---from excel file to csv
r=open('C:\\Users\\asnat\\excel file.csv','r')
print(r.read())

#assignment in module

file=open('C:\\Users\\asnat\\excel file.csv','r')
data=file.readlines()
for line in data:
    word=line.split()
    print(word)
''''
#python program to reverse the content of a file and store it in another file
#open the file in write mode
file=open('C:\\Users\\asnat\\excel handle.csv','w')
print(r.read())

f1=open('C:\\Users\\asnat\\excel handle.csv','w')
f2=open('C:\\Users\\asnat\\excel file.csv','r')
data=f2.read()
data1=data[::1]
f1.write(data1)
f1.close()


f1=open('C:\\Users\\asnat\\excel handle.csv','r')
f2=open('C:\\Users\\asnat\\excel file.csv','a')
for line in f1:
    f2.write(line)
f1.close()
f2.close()



f=open('C:\\Users\\asnat\\fileh.txt','r')
print(f.(read))


f=open('C:\\Users\\asnat\\fileh.txt','r')
print(f.(read))'''

file=open('venkat.txt','r')
print(file.read())

