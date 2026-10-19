# Class :- It is blueprint of objects.
# Blueprint :- it is plan to create objects.
# Objects :- It is instance of class
# var_name = class_name()
# ex. class Student :
#       s1 = Student()
#       s2 = Student()
# Objects know that they are of which class but class haven't any idea how any objects inside it
# Constructor :- It helps PVM (pyhton virtual machine) to initialize objects
# A constuctor is special method / function in a class.
# It initialize attributes / data members into memory.
# It autmatically invoked / called at time of object creation.
# Students class has 2 objects so constructor called twice .
# It runs once per object.
# The name of constructor is always like :
#           _ _init_ _
# The first argument of constructor is always self in python.
# A method that starts and ends with double underscrore in python it called dunder or magic method in python.
# class Student :
#   def __init__(self , r , n , c , e):     ---> constructor
#       self.roll_no = r
#       self.name = n
#       self.city = c
#       self.email = e
# s1 = Student (1,"Jay","Pune","jay@gmail.com")

class Student :
    pass
obj = Student()
print(obj)
print(type(obj))

obj2 = [1,2,3,4]
print(obj2)
print(type(obj2))

# All fundamental and collective data types are also classes but they are called as build-in classes in python
# ex. int , list , set , string , tuple 

class Stud :
    def __init__(self, r , n , c, e , m):
        print(f"Constructor is running for roll no {r}")
        self.roll_no = r 
        self.name = n
        self.city = c
        self.email = e
        self.marks = m

s1 = Stud( 14 , "Om" , "Mumbai" , "ompran@1418gmail.com" ,95)
s2 = Stud( 18 , "Pran" , "Mumbai" , "pranom@1814gmail.com" ,95)

print(s1.name)
print(s2.name)

print(s1.marks)
print(s2.marks)

s1.marks = 100
s2.marks = 99

print(s1.marks)
print(s2.marks)