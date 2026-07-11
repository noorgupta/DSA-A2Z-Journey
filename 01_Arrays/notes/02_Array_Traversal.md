# Array Traversal

## What is Array Traversal?

Array traversal means visiting every element of an array one by one in a specific order.

It is one of the most fundamental operations performed on arrays.

Example:

```python
arr = [10, 20, 30, 40, 50]
```

Traversal means visiting:

```
10
↓

20
↓

30
↓

40
↓

50
```

Every element is processed exactly once.

---

# Why Do We Need Traversal?

Traversal is required whenever we want to perform an operation on every element of an array.

Examples:

- Find the largest element
- Find the smallest element
- Calculate the sum
- Count even numbers
- Search for an element
- Update values
- Print the array

Without traversal, these operations are not possible.

---

# Visual Representation

```
Index

 0     1     2     3     4

┌────┬────┬────┬────┬────┐
│ 10 │ 20 │ 30 │ 40 │ 50 │
└────┴────┴────┴────┴────┘

Traversal

↑

Start here

↓

Move one step at a time

↓

Visit every element

↓

End
```

---

# Methods of Traversal

Python provides multiple ways to traverse an array.

1. Using Index
2. Using Elements
3. Using enumerate()
4. Using while loop

Each method has its own use case.

---

# Method 1: Traversing Using Index

```python
arr = [10, 20, 30, 40, 50]

for i in range(len(arr)):
    print(arr[i])
```

Explanation:

- `len(arr)` gives the number of elements.
- `range(len(arr))` generates valid indices.
- `arr[i]` accesses each element.

This method is useful when the index is needed.

---

# Method 2: Traversing Using Elements

```python
arr = [10, 20, 30, 40, 50]

for num in arr:
    print(num)
```

Explanation:

Instead of using indices, Python directly gives each element.

This is cleaner and more readable when the index is not required.

---

# Method 3: Traversing Using enumerate()

```python
arr = [10, 20, 30]

for index, value in enumerate(arr):
    print(index, value)
```

Output:

```
0 10

1 20

2 30
```

Use `enumerate()` when both the index and value are required.

---

# Method 4: Traversing Using while

```python
arr = [10, 20, 30]

i = 0

while i < len(arr):
    print(arr[i])
    i += 1
```

Useful when manual control of the index is needed.

---

# Time Complexity

All traversal methods visit every element exactly once.

Time Complexity:

```
O(n)
```

---

# Space Complexity

No additional data structures are created.

Space Complexity:

```
O(1)
```

---

# Which Method Should We Use?

| Situation | Preferred Method |
|-----------|------------------|
| Need only values | `for element in array` |
| Need index | `for i in range(len(arr))` |
| Need index and value | `enumerate()` |
| Need manual control | `while` |

---

# DSA Relevance

Traversal is used in almost every array problem.

Learning traversal thoroughly is the first step toward solving array-based questions efficiently.

---

# Key Takeaways

- Traversal means visiting every element.
- Every array problem begins with traversal.
- Python provides multiple traversal techniques.
- Choose the traversal method based on the problem.
- Traversing an array takes O(n) time and O(1) extra space.