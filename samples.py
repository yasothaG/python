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