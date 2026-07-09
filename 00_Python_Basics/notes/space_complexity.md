# Space Complexity

## What is Space Complexity?

Space Complexity measures the amount of additional memory (extra space) an algorithm uses as the input size increases.

Like Time Complexity, it does not measure memory in MB or GB.

Instead, it measures how memory usage grows with the size of the input.

---

# Why Do We Need Space Complexity?

Suppose two algorithms solve the same problem.

Algorithm A

Time: O(n)

Space: O(1)

Algorithm B

Time: O(n)

Space: O(n)

Both take the same amount of time.

However, Algorithm A is more memory efficient.

---

# Important Note

Input memory is **not counted**.

Only the extra memory created by the algorithm is considered.

Example:

```python
arr = [1,2,3,4,5]
```

The array itself is the input.

It is **not** counted in space complexity.

---

# O(1) Space

Constant extra memory.

Example:

```python
sum = 0

for num in arr:
    sum += num
```

Only one variable (`sum`) is used.

Space Complexity:

```
O(1)
```

---

# O(n) Space

Memory grows with input size.

Example:

```python
copy = []

for num in arr:
    copy.append(num)
```

A new array of size `n` is created.

Space Complexity:

```
O(n)
```

---

# O(n²) Space

Memory grows as the square of the input.

Example:

```python
matrix = []

for i in range(n):
    matrix.append([0] * n)
```

An `n × n` matrix is created.

Space Complexity:

```
O(n²)
```

---

# Time vs Space Complexity

Time Complexity

Measures:

```
Number of operations
```

Space Complexity

Measures:

```
Extra memory used
```

---

# Examples

## Example 1

```python
sum = 0

for num in arr:
    sum += num
```

Time:

```
O(n)
```

Space:

```
O(1)
```

---

## Example 2

```python
copy = arr.copy()
```

Time:

```
O(n)
```

Space:

```
O(n)
```

---

# DSA Relevance

Many interview problems ask for:

- O(n) time
- O(1) extra space

Understanding space complexity is as important as understanding time complexity.

---

# Key Takeaways

- Space Complexity measures extra memory.
- Input memory is not counted.
- O(1) means constant extra memory.
- O(n) means memory grows linearly.
- Always try to optimize both time and space.