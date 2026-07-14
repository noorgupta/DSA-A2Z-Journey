# Heap

## 📖 What is a Heap?

A Heap is a specialized tree-based data structure that always keeps the **highest-priority element** at the top.

In Python, the `heapq` module implements a **Min Heap**, which means the **smallest element is always available first**.

Unlike a sorted list, a heap does **not** keep every element in sorted order. It only guarantees that the smallest element is always at the root (or index `0` in Python).

---

# 🤔 Why Am I Learning Heap?

Imagine I have the following numbers:

```python
[5, 2, 8, 1]
```

If I want the smallest element using a normal list, I have to search through the entire list.

Time Complexity:

```
O(n)
```

A Heap is designed to solve this problem efficiently.

It always keeps the smallest element ready to access.

This makes it ideal for problems where I repeatedly need the smallest (or largest) element.

---

# 🏥 Real-Life Analogy

Imagine I am managing a hospital.

Patients arrive with different priorities.

| Patient | Priority |
|---------|----------|
| Rahul | 5 |
| Aman | 1 |
| Neha | 3 |
| Priya | 2 |

The patient with the **highest priority** should be treated first.

Instead of checking every patient each time, a Heap automatically keeps the highest-priority patient ready.

This is exactly how a Priority Queue works.

---

# 🌳 Heap Representation

A Min Heap follows one important rule:

> Every parent node is **less than or equal to** its children.

Example:

```text
        1
      /   \
     2     3
    /
   5
```

Notice:

- 1 ≤ 2
- 1 ≤ 3
- 2 ≤ 5

The smallest element is always at the top.

---

# ⚠️ Heap is NOT a Sorted Array

Many beginners think:

```
Heap = Sorted Array
```

❌ Incorrect.

Example:

```python
[1, 2, 8, 5]
```

This is a valid heap.

Notice:

```
2 < 8
```

but

```
8 > 5
```

The elements are **not completely sorted**.

A heap only guarantees that the smallest element is at the root.

---

# 📦 Python Heap

Python provides Heap functionality through:

```python
import heapq
```

Python implements a **Min Heap** by default.

---

# Common Heap Operations

## 1. heapify()

Converts a normal list into a heap.

Example:

```python
import heapq

arr = [5, 2, 8, 1]

heapq.heapify(arr)
```

### Purpose

Instead of sorting the list, Python rearranges it to satisfy the heap property.

Time Complexity:

```
O(n)
```

---

## 2. heappush()

Adds a new element while maintaining the heap property.

Example:

```python
heapq.heappush(arr, 3)
```

Time Complexity:

```
O(log n)
```

---

## 3. heappop()

Removes and returns the smallest element.

Example:

```python
smallest = heapq.heappop(arr)
```

Time Complexity:

```
O(log n)
```

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| heapify() | O(n) |
| heappush() | O(log n) |
| heappop() | O(log n) |
| Peek Smallest | O(1) |

---

# DSA Applications

Heaps are commonly used in:

- Priority Queues
- Kth Largest / Smallest Element
- Top K Frequent Elements
- Merge K Sorted Lists
- Scheduling Problems
- Greedy Algorithms
- Graph Algorithms (Dijkstra's Algorithm)

---

# 💡 Key Takeaways

- A Heap is **not** a sorted array.
- Python provides a **Min Heap** using the `heapq` module.
- The smallest element is always available at the top.
- Heap operations are much faster than sorting repeatedly when priorities matter.
- Heaps become extremely useful in advanced DSA problems.