# Exercise:
# Write a program that gets a temperature (float) in Celsius and prints it in Fahrenheit.
# Define and use the cel2fah() function.
# Formula: Fahrenheit = (9/5) * Celsius + 32

# Function to convert Celsius to Fahrenheit
def cel2fah(celsius):
    return (9/5) * celsius + 32

# Get the temperature in Celsius from the user
celsius_temp = float(input("Enter the temperature in Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit_temp = cel2fah(celsius_temp)

# Print the temperature in Fahrenheit
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
