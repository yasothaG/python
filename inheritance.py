# multiple inheritance means adding more class access to the one single class 
class dad():
    def phone(self):
        print("Dads phone")

class mom():
    def sweet(self):
        print("moms sweet") 

class son(dad,mom):
    def laptop(self):
        print("sons laptop")
         
ram=son()
ram.phone() 
ram.sweet()  

# Multi level inheritance
class grandpa():
    def phone(self):
        print("grandpa phone")

class dad(grandpa):
    def money(self):
        print("dads money")

class son(dad):
    def laptop(self):
        print("sons laptop")

ram =son()
ram.laptop() 
ram.money()  

d1=dad()
d1.phone()

# hierarchy inheritance 

class dad():
    def money(self):
        print("dads money")

class son1(dad):
    def laptop(self):
        print(" his laptop")

class son2(dad):
    def mobile(self):
        print(" his mobile")

class son3(dad):
    def tab(self):
        print(" his tab")

s2=son2()
s2.money()

# hybrid inheritance  
 