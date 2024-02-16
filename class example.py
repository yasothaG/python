#1)Create a class called student ,create a variable = name and register number using constructor.
    #Create a function called display which should display the name and register number of the student
class student:
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
class fruit:
    def __init__(self):
        self.colour="black" 
apple=fruit()
         
         