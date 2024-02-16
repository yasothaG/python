# instance method,  in this "self" is used to represent the object changes  

class laptop():
    chargertype="c-type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setprice(self,price):
        self.price=price

    def getprice(self):    
         print(self.price)
Hp=laptop()
Hp.setprice(10000)
Hp.getprice()

# class method

class laptop():
    chargertype="c-type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setprice(self,price):
        self.price=price

    def getprice(self):    
         print(self.price)

    @classmethod 
    def changechargertype(cls):
        cls.chargertype="B-type"
        print("chargertype changed to B")   

Hp=laptop()
Hp.setprice(10000)
Hp.getprice()
        
laptop.changechargertype()    

# static method - info
class laptop():
    chargertype="c-type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setprice(self,price):
        self.price=price

    def getprice(self):    
         print(self.price)

    @classmethod 
    def changechargertype(cls):
        cls.chargertype="B-type"
        print("chargertype changed to B")  

    @ staticmethod
    def  info():
        print("this is laptop class")   

Hp=laptop()
Hp.setprice(10000)
Hp.getprice()
        
laptop.changechargertype()    

Hp.info()



        



        