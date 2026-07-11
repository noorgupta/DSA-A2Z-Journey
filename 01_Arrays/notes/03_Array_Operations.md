# Array Operations

## What are Array Operations?

Array operations are the basic actions that can be performed on an array.

These operations help us store, retrieve, modify, and manage data efficiently.

The five most common operations are:

- Create
- Access
- Update
- Insert
- Delete
- Search

---

# 1. Create

Creating an array means storing multiple values together.

Example:

```python
numbers = [10, 20, 30, 40]
```

Time Complexity:

```
O(n)
```

because all elements need to be stored.

---

# 2. Access

Access means retrieving an element using its index.

Example:

```python
numbers = [10, 20, 30]

print(numbers[1])
```

Output:

```
20
```

Time Complexity:

```
O(1)
```

Reason:

Python directly accesses the required position.

---

# 3. Update

Updating means changing the value stored at an index.

Example:

```python
numbers = [10, 20, 30]

numbers[1] = 99

print(numbers)
```

Output:

```
[10, 99, 30]
```

Time Complexity:

```
O(1)
```

---

# 4. Insert

Insert means adding a new element.

Python provides:

```python
insert(index, value)
```

Example:

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)
```

Output:

```
[10, 15, 20, 30]
```

Time Complexity:

```
O(n)
```

Reason:

Elements after the insertion point must shift one position to the right.

---

# 5. Delete

Delete removes an element.

Example:

```python
numbers = [10, 20, 30]

numbers.pop(1)
```

Output:

```
[10, 30]
```

Time Complexity:

```
O(n)
```

Reason:

Remaining elements may need to shift left.

---

# 6. Search

Searching means finding whether an element exists.

Example:

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```
True
```

Linear search checks elements one by one.

Time Complexity:

```
O(n)
```

---

# Summary

| Operation | Time Complexity |
|------------|-----------------|
| Access | O(1) |
| Update | O(1) |
| Search | O(n) |
| Insert | O(n) |
| Delete | O(n) |

---

# Why are Insert and Delete O(n)?

Suppose we have:

```
Index

0   1   2   3

10  20  30  40
```

Insert **15** at index **1**

```
10  15  20  30  40
```

Notice:

20 moves

30 moves

40 moves

Every element shifts.

That is why insertion is O(n).

Deletion works similarly.

---

# DSA Relevance

Almost every array problem combines these operations.

Examples:

- Insert an element.
- Delete duplicates.
- Search a target.
- Update values.
- Traverse after modification.

---

# Key Takeaways

- Access and Update are fast: O(1).
- Insert, Delete, and Search are generally O(n).
- Understanding these operations helps explain why some algorithms are efficient and others are not.