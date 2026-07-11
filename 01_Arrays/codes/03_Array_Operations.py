numbers = [10, 20, 30, 40]

print("Original Array:")
print(numbers)

print("-" * 30)

# Access
print("Access Index 2:")
print(numbers[2])

print("-" * 30)

# Update
numbers[1] = 99

print("After Update:")
print(numbers)

print("-" * 30)

# Insert
numbers.insert(2, 50)

print("After Insert:")
print(numbers)

print("-" * 30)

# Delete
numbers.pop(3)

print("After Delete:")
print(numbers)

print("-" * 30)

# Search
print("Is 50 Present?")
print(50 in numbers)