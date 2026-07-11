# Arrays - Introduction

## Mistake 1: Confusing Index with Value

### Wrong Thinking

```
Index 2 = Value 2
```

### Reality

Index is the **position**.

Value is the **data stored** at that position.

Example:

```python
arr = [10, 20, 30]
```

```
Index 2 → Value 30
```

---

## Mistake 2: Starting Index from 1

### Wrong

```
First element → Index 1
```

### Correct

```
First element → Index 0
```

Always remember that Python uses **0-based indexing**.

---

## Mistake 3: Accessing an Invalid Index

```python
arr = [10, 20, 30]

print(arr[5])
```

### Error

```
IndexError: list index out of range
```

### Learning

Always ensure the index is between:

```
0

and

len(array) - 1
```

---

## Mistake 4: Thinking Arrays and Lists Are Completely Different in Python

For DSA in Python:

- We use **lists** to implement array concepts.
- Think in terms of arrays while writing code using lists.

# Array Traversal

## Mistake 1: Using len(arr) as the Last Index

### Wrong

```python
print(arr[len(arr)])
```

### Error

```
IndexError: list index out of range
```

### Learning

The last valid index is:

```python
len(arr) - 1
```

---

## Mistake 2: Forgetting to Increment the Index in a While Loop

### Wrong

```python
i = 0

while i < len(arr):
    print(arr[i])
```

### Problem

Infinite loop.

### Learning

Always update the loop variable.

```python
i += 1
```

---

## Mistake 3: Confusing Index with Element

### Wrong

```python
for i in arr:
    print(arr[i])
```

### Why?

Here, `i` is already the element, not the index.

If `arr = [10, 20, 30]`, Python tries to access:

```python
arr[10]
```

which causes an error.

### Correct

```python
for num in arr:
    print(num)
```

or

```python
for i in range(len(arr)):
    print(arr[i])
```

---

## Mistake 4: Using enumerate() Incorrectly

### Wrong

```python
for item in enumerate(arr):
    print(item)
```

Output:

```
(0, 10)
(1, 20)
(2, 30)
```

This is not wrong syntactically, but if you want separate values, unpack them.

### Better

```python
for index, value in enumerate(arr):
    print(index, value)
```
# Array Operations

## Mistake 1: Accessing an Invalid Index

### Wrong

```python
arr = [10, 20, 30]

print(arr[5])
```

### Error

```
IndexError: list index out of range
```

### Learning

Always access indices between:

```
0

and

len(arr) - 1
```

---

## Mistake 2: Thinking Insert is O(1)

Many beginners think inserting is always fast.

Reality:

When inserting in the middle, every element after that position shifts.

Complexity:

```
O(n)
```

---

## Mistake 3: Thinking Delete Removes Only the Value

Deleting an element also shifts remaining elements.

Example:

```
10 20 30 40

Delete 20

↓

10 30 40
```

---

## Mistake 4: Confusing pop() and remove()

```python
pop(index)
```

removes using the **index**.

```python
remove(value)
```

removes using the **value**.

These are different operations.

# Array Methods

## append()

### Mistake 1

Wrong

```python
numbers = [1,2,3]

numbers = numbers.append(4)
```

Problem

```
numbers

↓

None
```

### Why?

`append()` modifies the original list and returns `None`.

Correct

```python
numbers.append(4)
```

---

## Mistake 2

Wrong

```python
numbers.append(4,5)
```

Problem

```
TypeError
```

### Learning

`append()` accepts only **one element**.

To add multiple elements use:

```python
extend()
```

# extend()

## Mistake 1

```python
arr.extend(10)
```

Error:

```
TypeError
```

Learning:

`extend()` expects an iterable.

Correct:

```python
arr.extend([10])
```

---

## Mistake 2

```python
x = arr.extend([3,4])
```

`x` becomes `None`.

Like `append()`, `extend()` modifies the original list.

# insert()

## Mistake 1

```python
x = arr.insert(1, 10)
```

`x` becomes `None`.

---

## Mistake 2

Thinking `insert()` replaces a value.

```python
arr = [10, 20, 30]

arr.insert(1, 15)
```

Result:

```
[10, 15, 20, 30]
```

It **adds**, not **replaces**.

To replace:

```python
arr[1] = 15
```

# pop()

## Mistake 1

```python
arr.pop(10)
```

Error

```
IndexError
```

Learning

Index must exist.

---

## Mistake 2

Thinking pop() removes by value.

Wrong

```python
arr.pop(20)
```

`20` is treated as an index, **not** a value.

# remove()

## Mistake 1

```python
arr.remove(100)
```

Error

```
ValueError
```

Learning

The value must exist.

---

## Mistake 2

Confusing remove() with pop().

```python
pop(index)

remove(value)
```

# clear()

## Mistake 1

Thinking clear() deletes the variable.

```python
arr.clear()

print(arr)
```

Output

```
[]
```

The variable still exists.

---

## Mistake 2

```python
x = arr.clear()
```

`x` becomes

```
None
```