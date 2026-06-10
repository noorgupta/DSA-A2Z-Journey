# Python Basics

This section covers the fundamental Python concepts required before starting Data Structures and Algorithms.

---

# Input / Output

## What is Input?

Input is data provided to a program by a user or another source. Programs use input to perform operations and produce results.

### Example

```python
name = input("Enter your name: ")
```

Input:

```text
Noor
```

Output stored in variable:

```python
name = "Noor"
```

---

## What is Output?

Output is the information displayed by a program after processing data.

### Example

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

## Why Do We Need Input and Output?

Without input:

```python
age = 20
```

The value is fixed.

With input:

```python
age = int(input())
```

The user can enter any value.

This makes programs dynamic and interactive.

---

# Input → Process → Output

Every DSA problem follows this pattern:

```text
Input
↓
Process
↓
Output
```

Example:

Input:

```text
10 20
```

Process:

```python
10 + 20
```

Output:

```text
30
```

---

# input()

## What is input()?

`input()` is a built-in Python function used to receive data from the user.

### Example

```python
name = input()
```

If the user enters:

```text
Noor
```

Then:

```python
name = "Noor"
```

---

## Important Note

`input()` ALWAYS returns a string.

Example:

```python
n = input()
```

Input:

```text
100
```

Result:

```python
n = "100"
```

Type:

```python
print(type(n))
```

Output:

```text
<class 'str'>
```

---

# print()

## What is print()?

`print()` displays data on the screen.

### Example

```python
print("Hello")
```

Output:

```text
Hello
```

### Multiple Values

```python
name = "Noor"
age = 20

print(name, age)
```

Output:

```text
Noor 20
```

---

# type()

## What is type()?

`type()` is used to check the datatype of a value or variable.

### Example

```python
n = 10
print(type(n))
```

Output:

```text
<class 'int'>
```

---

# int()

## What is int()?

`int()` converts a value into an integer.

### Example

```python
n = int("100")
```

Result:

```python
n = 100
```

### Common Error

```python
n = int("abc")
```

Error:

```text
ValueError
```

Reason:

Python cannot convert alphabetic characters into integers.

---

# Multiple Input

## Taking Two Integers

```python
a, b = map(int, input().split())
```

Input:

```text
10 20
```

Output:

```python
a = 10
b = 20
```

---

# Understanding split()

## What is split()?

`split()` breaks a string into multiple parts using spaces.

Example:

```python
"10 20".split()
```

Result:

```python
["10", "20"]
```

---

# Understanding map()

## What is map()?

`map()` applies a function to every element.

Example:

```python
map(int, ["10", "20"])
```

Result:

```python
[10, 20]
```

---

# Array Input

## Taking Array Input

```python
arr = list(map(int, input().split()))
```

Input:

```text
1 2 3 4 5
```

Output:

```python
[1, 2, 3, 4, 5]
```

---

# Key Takeaways

* `input()` always returns a string.
* Use `int()` when integer input is required.
* Use `type()` to inspect datatypes.
* `split()` separates a string into multiple values.
* `map()` applies a function to each element.
* Arrays are commonly taken using:

```python
arr = list(map(int, input().split()))
```

* Every DSA problem follows:

```text
Input → Process → Output
```
