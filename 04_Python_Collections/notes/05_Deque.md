# Deque

## 📖 What is a Deque?

A deque (Double-Ended Queue) is a collection that allows efficient insertion and deletion from both the front and the back.

Unlike Python lists, deque is optimized for operations at both ends.

---

## 🤔 Why Am I Learning Deque?

I will use deque whenever I need:

- Queue implementation
- Stack implementation
- Sliding Window problems
- Breadth First Search (BFS)

---

## 📌 Characteristics

- Ordered
- Mutable
- Allows duplicate values
- Supports insertion/removal from both ends efficiently

---

## Import

```python
from collections import deque
```

---

## Example

```python
from collections import deque

dq = deque([10,20,30])

print(dq)
```

---

## Common Operations

- append()
- appendleft()
- pop()
- popleft()

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| append() | O(1) |
| appendleft() | O(1) |
| pop() | O(1) |
| popleft() | O(1) |

---

## DSA Applications

- Queue
- Stack
- Sliding Window
- BFS Traversal

---

## Key Takeaways

- Faster than lists for front operations.
- Supports insertion and deletion from both ends efficiently.