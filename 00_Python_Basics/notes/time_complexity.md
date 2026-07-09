# Time Complexity

## What is Time Complexity?

Time Complexity is a way to measure how the running time of an algorithm grows as the input size increases.

It does **not** measure the actual time taken in seconds.

Instead, it measures how the number of operations changes with increasing input size.

---

# Why Do We Need Time Complexity?

Suppose two programs solve the same problem.

Program A takes:

```
1 second
```

Program B takes:

```
3 seconds
```

Can we conclude that Program A is always better?

No.

The result depends on:

- Computer speed
- Processor
- RAM
- Compiler
- Programming language

Instead of measuring time in seconds, we measure the **growth of operations**.

This is called Time Complexity.

---

# Example

Suppose we want to print numbers from 1 to n.

```python
for i in range(n):
    print(i)
```

If:

```
n = 5
```

The loop runs:

```
5 times
```

If:

```
n = 1000
```

The loop runs:

```
1000 times
```

The number of operations grows linearly.

Time Complexity:

```
O(n)
```

---

# What is Big O Notation?

Big O notation describes the worst-case growth of an algorithm as the input size increases.

Example:

```
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
```

---

# Common Time Complexities

## O(1) — Constant Time

The number of operations never changes.

Example:

```python
arr[0]
```

Accessing the first element takes the same amount of work whether the array has 10 elements or 1,000,000.

---

## O(n) — Linear Time

The number of operations grows directly with the input size.

Example:

```python
for i in range(n):
    print(i)
```

---

## O(n²) — Quadratic Time

Nested loops.

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The inner loop runs `n` times for each iteration of the outer loop.

Total operations:

```
n × n = n²
```

---

## O(log n)

The input size reduces every step.

Example:

Binary Search.

Instead of checking every element, Binary Search repeatedly divides the search space in half.

---

# Rules for Finding Time Complexity

## Single Loop

```python
for i in range(n):
```

```
O(n)
```

---

## Nested Loops

```python
for i in range(n):
    for j in range(n):
```

```
O(n²)
```

---

## Consecutive Loops

```python
for i in range(n):
    ...

for j in range(n):
    ...
```

```
O(n + n)

↓

O(2n)

↓

O(n)
```

Constants are ignored.

---

## Constant Operations

```python
a = 10

b = 20

print(a + b)
```

```
O(1)
```

---

# Why Do We Ignore Constants?

Example:

```
5n

↓

O(n)
```

As `n` becomes very large, the constant `5` becomes insignificant compared to the growth of `n`.

---

# DSA Relevance

Every DSA problem has multiple approaches.

Example:

Brute Force:

```
O(n²)
```

Optimized:

```
O(n)
```

Choosing the better approach is one of the most important skills in coding interviews.

---

# Key Takeaways

- Time Complexity measures growth, not actual time.
- Big O describes the worst-case complexity.
- Single loop → O(n)
- Nested loops → O(n²)
- Constant operations → O(1)
- Binary Search → O(log n)
- Always aim for a more efficient solution when possible.