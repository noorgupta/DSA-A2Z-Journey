arr = [10,20,30,40,50]

target = 30 

found = -1

for i in range(len(arr)):
    if arr[i] == target:
        found = i
        break 

print(found)
    