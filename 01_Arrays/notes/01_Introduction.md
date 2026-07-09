# Arrays - Introduction

## What is an Array?

An array is a linear data structure used to store multiple values of the **same type** under a single variable name.

Instead of creating multiple variables, an array allows us to store related data together.

Example:

Without an array:

```python
student1 = 85
student2 = 92
student3 = 78
student4 = 95
student5 = 88
```

With an array (Python List):

```python
marks = [85, 92, 78, 95, 88]
```

Now all the marks are stored in one place.

---

# Why Do We Need Arrays?

Imagine a classroom with 100 students.

Without arrays, you would need:

```python
student1
student2
student3
...
student100
```

Managing this is difficult.

With an array:

```python
students = [85, 92, 78, 95, 88]
```

You can access every student's marks using its position (index).

Arrays make data easier to:

- Store
- Access
- Traverse
- Update
- Process

---

# Real-Life Analogy

Imagine a train.

```
+-----+-----+-----+-----+-----+
| 10  | 20  | 30  | 40  | 50  |
+-----+-----+-----+-----+-----+
```

Each coach stores one value.

The coaches are connected in order.

Instead of remembering each coach separately, you simply refer to the train.

An array works in the same way.

---

# Characteristics of an Array

- Stores multiple values together.
- Elements are stored in order.
- Every element has an index.
- Elements can be accessed directly using their index.
- Arrays are one of the most fundamental data structures in DSA.

---

# What is an Index?

An index represents the position of an element inside an array.

Example:

```python
marks = [85, 92, 78, 95, 88]
```

| Index | Value |
|------:|------:|
| 0 | 85 |
| 1 | 92 |
| 2 | 78 |
| 3 | 95 |
| 4 | 88 |

Accessing an element:

```python
print(marks[2])
```

Output:

```
78
```

---

# Why Does Indexing Start From 0?

This is one of the most common beginner questions.

Think of the index as the **distance from the beginning of the array**.

```
Index: 0   1   2   3   4
Value:10  20  30  40  50
```

- The first element is **0 positions away** from the beginning.
- The second element is **1 position away**.
- The third element is **2 positions away**.

That's why indexing starts at **0** in most programming languages.

---

# Array vs Variables

Without an array:

```python
a = 10
b = 20
c = 30
```

With an array:

```python
numbers = [10, 20, 30]
```

The array groups related values together, making them easier to manage.

---

# Advantages of Arrays

- Easy to store multiple values.
- Fast access using an index.
- Simple to traverse.
- Foundation for many DSA problems.

---

# Limitations

- In many languages, arrays have a fixed size.
- Inserting or deleting elements in the middle can be expensive.

> **Note:** Python uses dynamic arrays (lists), so they can grow or shrink automatically.

---

# Python Lists and Arrays

Python does not have a built-in fixed-size array like C or Java.

Instead, Python provides **lists**, which are implemented using a dynamic array internally.

For DSA, we use Python lists to understand and solve array problems.

Example:

```python
numbers = [1, 2, 3, 4, 5]
```

---

# DSA Relevance

Arrays are used in:

- Searching
- Sorting
- Prefix Sum
- Sliding Window
- Two Pointers
- Binary Search
- Dynamic Programming

Learning arrays thoroughly makes future topics much easier.

---

# Key Takeaways

- An array stores multiple related values.
- Every element has an index.
- Indexing starts from 0.
- Python uses dynamic arrays called lists.
- Arrays are the foundation of many DSA problems.