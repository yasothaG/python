# function

# add
def add():
    print("Addition")
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    print(a+b)
add()   

#sub
def sub():
    print("subraction")
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    print(a-b)
sub()  

# multiple
def mul():
    print("multiple")
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    print(a*b)
mul()  

# division
def div():
    print("division")
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    print(a/b)
div()  


# example 
  # get integer input , and pass it to function , and find whether even on odd and final print even or odd
def evenorodd(b):
    if(b%2==0):
        print("even")
    else:
        print("odd")         
a=10
evenorodd(a) 

#get input a,b and print number from a to b
def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
a=int(input("Enter a:"))
b=int(input("Enter b:"))         
printrange(a,b)   

