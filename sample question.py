# if else 
mark=int(input())
if(mark>35):
    print("pass")
else:
    print("fail")

  # if else method       
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


# This example is to set that we can add input inside the if condition  also 
#/ get input for score, if score is greater than the 70 then only get the name, and department and finally print eligible or not 

score=int(input())
if(score>=70):
    name=input("enter your name:")
    department=input("enter the department")
    print("eligible")
else:
    print("not eligible")
        

# if condition can carry the more if condition and the inputalso added
   # Get input for salary and age.
   #If salary greater than or equal to 20000 or age less than or equal to 25, get input for required loan amount. If not print you are not eligible for loan.
   #If required loan amount is less than or equal to 50,000 print You are eligible for loan. If it is greater than 50,000 print maximum loan amount is 50000.

salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
    loan=int(input("enter the loan amount"))
    if(loan>500000):
        print("maximun amount for loan is 50000")
    else:
        print("not eligible for loan")   
else:
    print("not eligible for loan")


 #9. get input for five subjects marks. Add all of it And find average. If average mark is less than 35. Print "Additional class is required" else Print "you are good to go"

Tamil=int(input())
English=int(input())
Maths=int(input())
Science=int(input())
Social=int(input())
a=(Tamil+English+Maths+Science+Social)/5
print(a)
if (a<35):
    print("additional class is required")
else:
    print("you are good to go")

#for loop statements:
  #  print 2 table
for i in range(1,11):
      print(i,"x2=",i*2) 

      