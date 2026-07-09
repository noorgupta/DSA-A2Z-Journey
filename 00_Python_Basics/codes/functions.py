# Function without parameters

def greet():
    print("Welcome to DSA!")

greet()

print("-" * 30)

# Function with parameters

def greet_user(name):
    print("Hello", name)

greet_user("Noor")

print("-" * 30)

# Function with return value

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

print("-" * 30)

# Mutable object example

def add_element(arr):
    arr.append(100)

numbers = [1, 2, 3]

add_element(numbers)

print(numbers)