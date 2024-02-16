#1)Create a class called student ,create a variable = name and register number using constructor.
    #Create a function called display which should display the name and register number of the student
class student():
    def __init__(self):
        self.name="yasotha"
        self.regisno="12345"
    def display(self):
        print("Name:",self.name)
        print("regisno:",self.regisno)

s1=student()
print(s1.name)
print(s1.regisno)
s1.display()        

#2)Create a class called Fruit ,Create a variable called color using Init method
  #Create a object called apple "Pass the color variable as a parameter through object".
class fruit():
    def __init__(self,col):
        self.colour=col

apple=fruit("red")
print(apple.colour)

#3)Create a class called teacher , Create a variable = name and register number using constructor
    #Create a function called display which should display the name and register number of the teacher
     #Create t1 and t2 object and pass the name and reg no value through object
class Teacher():
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("Name:",self.name) 
        print("Reg:",self.regno) 

t1=Teacher("Thomas","1")
t2=Teacher("John","2")

t1.display()
t2.display()

 #4)Create a class called calculator , Create 2 variables a and b
   #Create a function called add,sub,mul,div, all functions should take 2 variables as parameter.
    #Pass the a and b value through objesti).         

class calculator():
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)
    def sub(self):
         print("sub",self.num1-self.num2)
    def mul(self):
        print("mul",self.num1*self.num2)
    def div(self):
        print("div",self.num1/self.num2)


object1=calculator(10,2)
object1.add()
object1.sub()
object1.mul()
object1.div()

# example without constructor
class calculator:
    def add(self,a,b):
        print("add",a+b)

object1=calculator()
object1.add(10,2)