# Exercise:
# Get a year from the user and determine whether it is a leap year.
# Rules:
# - Multiples of 400: leap year
# - Multiples of 4 and not multiples of 100: leap year
# - All other cases: not leap year
# If the input is not a positive number, print "input error".

# Get the year from the user
year = int(input("Enter a year: "))

# Check if the input is a positive number
if year <= 0:
    print("Input error: Year must be a positive number.")
else:
    # Determine if the year is a leap year
    if year % 400 == 0:
        print("leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print("leap year")
    else:
        print("not leap year")
