# instance variable
 # in constructor - self will work as the representation of odject , this self eliment is called as the instance variable 
class phone:
    def __init__(self, brand,price,chargertype):
        self.brand=brand
        self.price=price
        self.chargertype=chargertype
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Chargertype:",self.chargertype)

samsung=phone("samsung","10000","c-type")
samsung.display()

# class variable
  # this class variable is used as the common instructor of all the objects, this can also be changed by using the class.
class phone:
    chargertype="c type"
    def __init__(self, brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)

phone.chargertype="B-type" 

samsung=phone("samsung","10000")
samsung.display()

Redmi=phone("Redmi","20000")
Redmi.display()


        
 


        
