for i in "apple":
    print(i)

for i in range(5):
    print(i) 

# find 2 table by for loop condition
for i in range(1,11):
    print(i,"x2=",i*2)      
   
a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)  

#print even number btw 1 to 10
for i in range(1,11):
    if(i%2==0):
        print(i)

# count the even number btw 1 to 10 
     count=0
for i in range(1,10):
    if(i%2==0):
        count=count+1   
print(count)   

# find even & odd btw (range-1,10)
e_count=0
o_count=0 
for i in range(1,11):
    if(i%2==0):
        e_count=e_count+1 
    else:
        o_count=o_count+1      
print(e_count)
print(o_count)

# count the number divisible by 3 & 5 from 1 o 100
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)       
   
# find the sum of first 5 natural numbers
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)    

# get 10 number input and add the 10 numbef nd find the average
a=[]
for i in range(5):
    num=int(input("enter num"+str(i+1)))
    a.append(num)
print(a)    
