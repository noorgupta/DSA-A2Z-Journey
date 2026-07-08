# For Loops

## What is a Loop?

A loop is a programming construct that allows us to execute the same block of code multiple times without writing it repeatedly.

Instead of writing the same statement again and again, a loop performs the repetition automatically.

---

# Why Do We Need Loops?

Suppose we want to print:

```
Hello
```

10 times.

Without a loop:

```python
print("Hello")
print("Hello")
print("Hello")
...
```

This is repetitive and inefficient.

Using a loop:

```python
for i in range(10):
    print("Hello")
```

The same task is completed with much less code.

---

# Types of Loops in Python

Python provides two types of loops:

- `for` loop
- `while` loop

---

# What is a For Loop?

A `for` loop is used when we know how many times we want to repeat a task or when we want to iterate over a sequence such as numbers, lists, or strings.

---

# Syntax

```python
for variable in iterable:
    # code
```

Example:

```python
for i in range(5):
    print(i)
```

---

# Understanding range()

The `range()` function generates a sequence of numbers.

It is commonly used with `for` loops.

---

## range(stop)

Syntax:

```python
range(stop)
```

Starts from **0** and stops before **stop**.

Example:

```python
range(5)
```

Sequence:

```
0 1 2 3 4
```

---

## range(start, stop)

Syntax:

```python
range(start, stop)
```

Starts from **start** and stops before **stop**.

Example:

```python
range(2, 7)
```

Sequence:

```
2 3 4 5 6
```

---

## range(start, stop, step)

Syntax:

```python
range(start, stop, step)
```

Moves according to the given step value.

Example:

```python
range(1, 10, 2)
```

Sequence:

```
1 3 5 7 9
```

---

# Flow of Execution

Example:

```python
for i in range(3):
    print(i)
```

Execution:

Iteration 1

```
i = 0
```

Iteration 2

```
i = 1
```

Iteration 3

```
i = 2
```

Loop ends after reaching the stop value.

---

# Examples

Example 1

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

Example 2

```python
for i in range(2, 7):
    print(i)
```

Output:

```
2
3
4
5
6
```

---

Example 3

```python
for i in range(10, 0, -2):
    print(i)
```

Output:

```
10
8
6
4
2
```

---

# DSA Relevance

For loops are one of the most frequently used constructs in Data Structures and Algorithms.

They are used for:

- Traversing arrays
- Traversing strings
- Searching
- Sorting
- Counting
- Nested iterations

Almost every beginner DSA problem uses a `for` loop.

---

# Key Takeaways

- A loop is used to repeat code.
- `for` loops are used when the number of iterations is known.
- `range()` generates a sequence of numbers.
- The stop value is **not included**.
- `step` controls how much the value changes after each iteration.