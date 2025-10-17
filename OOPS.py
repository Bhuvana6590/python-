'''#Empty class creation
class car():
    pass
ob=car()
ob.carname='Duster'
ob.model=2021
ob.color='red'
print('My car name is',ob.carname)
print(ob.__dict__)

#creation of class with variable
class student:
    name='Mari'
    degree='BE'
    role='Developer'
stu=student()
print('My name is:',stu.name)
print('My name is:',stu.degree)
print('My name is:',stu.role)

#find the sum of two number using class
class cal:
    #method declaration
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #method declaration for display the result
    def show(self):
        return self.x+self.y
n=int(input("enter the NO:"))
m=int(input("enter the NO:"))
s=cal(n,m) #creation of object
print("the sum of value is:",s.show())

class student:
    def __init__(self,Name,Age):
        self.n=Name
        self.a=Age
    def display(self):
        print(f"My name is {self.n} and my age is {self.a}")
s=student('abdul',24)
s.display()

#single inheritance
class parent:#Parent,super or base class
    def __init__(self,Name,Age):
        self.n=Name
        self.a=Age
    def display(self):
        print("My Father name is {} and age of my father is{}".format(self.n,self.a))
class child(parent):#child, sub or derived role
    def __init__(self,Name,Age,Degree,Role):
        self.n=Name
        self.a=Age
        self.d=Degree
        self.r=Role
    def dis(self):
        print("My father name is {} and age of my father {}".format(self.n,self.a))
        print('im studying {} and working as a{}'.format(self.d,self.r))
c=child('venkat',55,'BE',"Developer")
c.display()
c.dis()


#Multiple inheritance
class cal1:#parent class1
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
class cal2:#parent class2
    def sub(self):
        return self.a-self.b
class cal3(cal1,cal2):
    def mul(self):
        return self.a*self.b
ob=cal3(90,45)
print("value of child class:",ob.mul())
print("value of parent class2:",ob.sub())
print("value of parent class1:",ob.add())


#multilevel inheritance
class employee(): #super class
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
class childemployee1(employee):#first child
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
class childemployee2(childemployee1):#second child class
     def __init__(self,name,age,salary):
         self.name=name
         self.age=age
         self.salary=salary
emp1=employee('venkat',22,1000)
emp2=childemployee1('arjun',23,2000)
print(emp1.age)
print(emp2.age)

#hierarchical inheritance
class employee(): 
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
class childemployee1(employee):
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
class childemployee2(employee):#second child class
     def __init__(self,name,age,salary):
         self.name=name
         self.age=age
         self.salary=salary
emp1=employee('Blessy',22,1000)
emp2=childemployee1('christy',23,2000)
print(emp1.age)
print(emp2.age)
'''
#hybrid inheritance
class school:
    def func1(self):
        print("This function is in school")
class student1(school):
    def func2(self):
        print("this function is mainly for student1 ")
class student2(school):
    def func3(self):
        print("this function is mainly for student1 ")
class student3(student1,school):
    def func4(self):
        print("this function is mainly for student1 ")
#creation of object
object=student3()
object.func1()
object.func2()


#hybrid inheritance

class get: #parent class
    def getin(self):
        self.a=int(input("enter the number:"))
        self.b=int(input("enter the number:"))
class addition(get):#child class1
    def add(self):
        self.getin()
        c=self.a+self.b
        print("Addition is:",c)
class subtraction(get):#child class2
    def
































