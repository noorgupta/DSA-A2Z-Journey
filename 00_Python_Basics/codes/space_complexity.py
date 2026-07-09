# O(1) Extra Space

arr = [1, 2, 3, 4, 5]

total = 0

for num in arr:
    total += num

print(total)

print("-" * 30)

# O(n) Extra Space

copy = []

for num in arr:
    copy.append(num)

print(copy)