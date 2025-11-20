# Declare and initialize a list
numbers = [10, 20, 30, 40, 50]

# Print the elements of the list
print("List elements:")
for num in numbers:
    print(num)

# Modify an element in the list (change the element at index 2)
numbers[2] = 35
print("\nModified list:")
for num in numbers:
    print(num)

# Calculate the sum of all elements in the list
total = sum(numbers)
print("\nSum of list elements:", total)
