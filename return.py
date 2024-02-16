# return function
def painter():
    return"i am painter"
print(painter()) 

#same above example
def valueofa():
    return 10
a=valueofa()
print(a)

# set username and passward , then get input from the user and print the return true or false
s_username="yasotha"
s_passward="1234"
  
username=input("Enter name:")
passward=input("Enter passward:")

def validate():
    if(s_username==username and s_passward== passward):
        return True
    else:
        return false
a=validate()   
print(a)

#  (a+b)*c  - get input a and b, and function called add(), which should return the sum of a and b , then mul a&b with c
def add(n1,n2):
    return n1+n2

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

added=add(a,b)
output=added*c

print(output)