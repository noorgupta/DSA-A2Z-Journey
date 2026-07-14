# List

## Mistake 1

Thinking Python lists are linked lists.

### Learning

Python lists are implemented as **dynamic arrays**, not linked lists.

---

## Mistake 2

Using a list for every problem.

### Learning

A list is powerful, but sometimes another collection like a set, dictionary, or deque is a better choice.

---

## Mistake 3

Assuming all insertions and deletions are O(1).

### Learning

Only operations at the end are efficient on average. Inserting or deleting in the middle requires shifting elements and is O(n).

# Tuple

## Mistake 1

Trying to modify a tuple.

```python
t = (1, 2, 3)

t[0] = 10
```

Error:

```
TypeError
```

---

## Mistake 2

Creating a single-element tuple incorrectly.

Wrong

```python
t = (5)
```

Correct

```python
t = (5,)
```

Without the comma, Python treats it as an integer.

# Set

## Mistake 1

Trying to access a set using an index.

```python
numbers = {10, 20, 30}

print(numbers[0])
```

Error

```
TypeError
```

### Learning

Sets are unordered and do not support indexing.

---

## Mistake 2

Thinking duplicate values are stored.

```python
numbers = {1, 1, 2, 2, 3}
```

Result

```
{1, 2, 3}
```

Duplicate values are automatically removed.

# Dictionary

## Mistake 1

Accessing a key that doesn't exist.

```python
student["marks"]
```

Error

```
KeyError
```

Learning

Check if the key exists or use:

```python
student.get("marks")
```

---

## Mistake 2

Using duplicate keys.

```python
student = {
    "age":20,
    "age":21
}
```

Output

```
{'age': 21}
```

The last value overwrites the previous one.

# Deque

## Mistake

Using a Python list as a queue.

```python
arr.pop(0)
```

Time Complexity

```
O(n)
```

Instead use

```python
deque.popleft()
```

Time Complexity

```
O(1)
```

# Heap

## Mistake

Thinking a heap stores elements in sorted order.

Learning:

A heap only guarantees that the smallest element is at the root.
The remaining elements are **not necessarily sorted**.