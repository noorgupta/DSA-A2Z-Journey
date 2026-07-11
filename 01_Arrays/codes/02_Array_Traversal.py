# Sample Array

arr = [10, 20, 30, 40, 50]

print("Using Index")
for i in range(len(arr)):
    print(arr[i])

print("-" * 30)

print("Using Elements")
for num in arr:
    print(num)

print("-" * 30)

print("Using enumerate()")
for index, value in enumerate(arr):
    print(f"Index = {index}, Value = {value}")

print("-" * 30)

print("Using while Loop")
i = 0

while i < len(arr):
    print(arr[i])
    i += 1