import math

num1 = int(input("first number: "))
num2 = int(input("second number: "))
num3 = int(input("third number: "))

def lcm(num1, num2, num3):
    return math.lcm(num1, num2, num3)

result = lcm(num1, num2, num3)

print(f"LMC of {num1}, {num2}, {num3} = {result}")