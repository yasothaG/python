# if else 
mark=int(input())
if(mark>35):
    print("pass")
else:
    print("fail")

  # if elase method       
income= int(input("income:"))
if(income>7000):
    print("eligible for scholarship")
else:
    print("not eligible for scholarship")    


#divisible 
a=10
print(a/2)

#modulas 
a=10
print(a%2)

# get input from user and if  a is divisible by both 3 and 5
a=int(input())
if(a%3==0 and a%5==0):
    print("divisible by 3and5")
else:
    print("not divisible by 3 and 5")   

# give input and find even or odd
    a=int(input())
if(a%2==0):
    print("even")
else:
    print("odd")   

    # get input  and say if input is lesser than 35 , then print poor student , if greater than 35 and less than 70 , then print average student
    #if greater than 70 print good student 
    score =int(input("out of 100:"))
     if(score<35):
    print("poor student")
if (score<35 and score<70):
    print("average student")    
if(score>70):
    print("good student")   

    #elif method
score=int(input())    
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")    
else:
    print("good student")   

    #Make a mini calculator, Get input for 2 numbers a and b  , Get input from user whether to add/sub/mul/div
           #If user selects add then add the two number and Print the result.
    a=int(input())
b=int(input())
operation =input ("add/sub/mul/div:")
if (operation=="add"):
    print (a+b)
elif (operation=="sub"):
    print(a-b)
elif (operation=="mul"):
    print(a*b)
elif (operation=="div"):
    print(a/b)
else: print("Invalid operation")
