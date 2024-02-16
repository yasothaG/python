def add(a,b,c):
    print(a+b+c)
add(10,5,4) 

# example

def add(a,b,c=0):
    print(a+b+c)

add(1,2)
add(1,2,3)

# over polymorphing
class animal():
    def sound(self):
        print("animal make sound")

class dog(animal):
    def sound(self):
        print("dog barks")

class bird(animal):
    def sound(self):
        print("bird sing")


b1=bird()        
b1.sound()

# example
class shape():
    def area(self):
        return 0

s1=shape()
print(s1.area())    

#over polymorphism
class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)

r1=rectangle()
r1.area()  

# super keyward 
    
class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print(self.name,self.grade) 

s1=student("yasotha","A")
s1.display()  

# example of over polymorphism
class vehicle():
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("car started")         

c=car()   
c.start() 
