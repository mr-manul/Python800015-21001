print ("Which number is bigger?")
#input
a = int(input("Enter first number:" ))
b = int(input("Enter first number:" ))
#compare
if a > b:
    print (f"{a} is bigger")
elif b > a:
    print (f"{b} is bigger")
elif a == b:
    print ("number is even")
else:
    print("error")
