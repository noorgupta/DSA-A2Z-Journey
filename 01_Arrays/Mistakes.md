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