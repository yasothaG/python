class laptop:
    def __init__(self):
        print("demo")
    def display(self):
        print("display")

hp=laptop()

# self call by construcure
class laptop:
    def __init__(self):
        self.price=""
        self.ram=""
        self.processor=""
    def display(self):
        print("display")

hp=laptop()
hp.prise="500000"
hp.ram="8gb"
hp.processor="i5"
print(hp.ram)


#
class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)

hp=laptop()

hp.ram="8gb"
hp.processor="i5"

hp.display()

# empty class
class laptop:
    pass