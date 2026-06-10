# 1. taking input 

name = input("Enter your name: ")
print(name)

# 2. Taking input but converting input's datatype in integer 

n = int(input("Enter any random number: "))
print(n)
print(type(n))

# 3. taking multiple inputs 

a, b = map(int, input("Enter any two random numbers: ").split())
print(a + b)

# 4. Taking input and putting it into a list(array)

arr = list(map(int, input().split()))
print(arr)

