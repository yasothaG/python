#create class,set variabe-price, processor, ram, create object- HP, Lenovo, Dell
class laptop:
    price=""
    processor=""
    ram=""
    
Hp=laptop()        
Lanovo=laptop()
Dell=laptop()

Hp.price="50000"
Hp.processor="i5"
Hp.ram="240"

Lanovo.price="40000"
Lanovo.processor="i7"
Lanovo.ram="120"

Dell.price="65000"
Dellprocessor="i6"
Dell.ram="280"

print(Hp)
print("Hp price:",Hp.price)
print("Hp processor:",Hp.processor)
print("Hp Ram:",Hp.ram)

print("Lanovo price:",Lanovo.price)
print("Lanovo processor:",Lanovo.processor)
print("Lanovo Ram:",Lanovo.ram)

print("Dell price:",Dell.price)
print("Dell processor:",Dell.processor)
print("Dell Ram:",Dell.ram)



