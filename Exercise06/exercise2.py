num1 = int(input("Please enter 1. number: "))
num2 = int(input("Please enter 2. number: "))
num3 = int(input("Please enter 3. number: "))
num4 = int(input("Please enter 4. number: "))
num5 = int(input("Please enter 5. number: "))

allnumber = [num1, num2, num3, num4, num5]

maxnum = allnumber[0]

for i in allnumber:
    if i > maxnum:
        maxnum = i

print(maxnum)
