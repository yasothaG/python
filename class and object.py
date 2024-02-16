 #  explanation
class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoying the beach")  

ramesh=goa()   
suresh=goa()

ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print("drink:",ramesh.drink)

print(suresh.name)
print("drink:",suresh.drink)

ramesh.party()
suresh.beach()
