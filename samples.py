class phone:
    chargertype="c-type"
    def __init__(self, brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Chargertype:",self.chargertype)

phone.chargertype="B-type" 
       
samsung=phone("samsung","10000")
samsung.display()

Redmi=phone("Redmi","20000")
Redmi.display()

        



        