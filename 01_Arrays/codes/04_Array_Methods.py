# append()

numbers = [10, 20, 30]

print("Before Append:")
print(numbers)

numbers.append(40)

print()

print("After Append:")
print(numbers)

#extend()

numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)

#insert()

arr = [10, 20, 30]

arr.insert(1, 15)

print(arr)

#pop()

arr = [10, 20, 30, 40]

print(arr.pop())

print(arr)

print(arr.pop(1))

print(arr)

#remove()

arr = [10, 20, 30, 20]

arr.remove(20)

print(arr)