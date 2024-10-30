numbers_str = input("String of numbers with commas: ")

numbers = list(map(int, numbers_str.split(',')))

largest_number = max(numbers)

count_largest = numbers.count(largest_number)

print("largest number:", largest_number)
print("count:", count_largest)