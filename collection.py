# list =[],  Allow duplicates, changeable and ordered
#ex:
a=[1,2,3,4,5]
print(type(a))

# append  -  if we need to add the number in the list so we can use the 
a.append(6)
print(a)

# insert - how to insert the number in some the position, this a.insert(0,11) it mean that in "0" position change value as 11 but the value in 0 position will change as 1st position like that all the values get changed in their position
a=[1,2,3,4,5]
a.insert(0,11)
print(a) 

#to modify the values, 0 position the value was changed into 1 to 11
a=[1,2,3,4,5]
a[0]=11
print(a)

# pop - means used to remove the eliments
a=[1,2,3,4,5,6]
a.pop(5)
print(a)

# extend  - used to merge the two list , "b" list will also added to "a" list
a=[1,2,3,4,5]
b=[11,12,13,14,15]
a.extend(b)
print(a)

# Tuple =() ,  can not modify, allow duplicates , but we can change the tuple into list and then make the changes by using the list eliment after the change

a=(1,2,3,4,5)
b=list(a)
print(a)
print(b)

# set ={} - Don't allow duplicates, can't modify, 
a={1,2,3,4,5}
# if we wants to add the value in the "a", then
a.add(6)
print(a)

# remove , it will remove 4 value from the "a" eliment
a.remove(4)

# empty pop will remove any one of the number from the "a" eliment 
a.pop()

# dictionary= {}
a={
    "name":"yasotha"
    "age":"21"
    "location":"pudukkottai"
    }
# we can print 
print(a)
print(a.keys())
print(a.values())

# modification
a={
    "name":"yasotha",
    "age":"21",
    "location":"pudukkottai"
    }
a["age"]="20"
print(a)

# and also modify as, if the eliment not in the a also it will automaticaly add in the eliments
a["colour"]="white"
a.update({"age":22})

# delete
a.pop("age")
del a["age"]

# to make dictionary as empty
a.clear()

