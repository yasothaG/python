# example
for i in range(1,6):
    for j in range(1,3):
        print(j,"apple")

# question is 
       # 1
       # 12
       # 123
       # 1234
       # 12345  
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end="")

# get output as:
        # *
        # **
        # ***
        # ****
        # *****
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print("*",end="")        

        
        