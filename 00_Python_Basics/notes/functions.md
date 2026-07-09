# Functions

## What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, we can write it once inside a function and call it whenever required.

---

# Why Do We Need Functions?

Imagine calculating the area of a rectangle multiple times.

Without a function:

```python
length = 5
breadth = 4
print(length * breadth)

length = 10
breadth = 6
print(length * breadth)
```

The same logic is repeated.

Using a function:

```python
def area(length, breadth):
    return length * breadth

print(area(5, 4))
print(area(10, 6))
```

The code becomes shorter, reusable, and easier to maintain.

---

# Syntax

```python
def function_name(parameters):
    # code
    return value
```

Example:

```python
def greet():
    print("Hello")
```

---

# Function Without Parameters

```python
def greet():
    print("Welcome!")

greet()
```

Output:

```
Welcome!
```

---

# Function With Parameters

```python
def greet(name):
    print("Hello", name)

greet("Noor")
```

Output:

```
Hello Noor
```

---

# Function With Return Value

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```
30
```

---

# Difference Between print() and return

## print()

Displays the value on the screen.

```python
def add(a, b):
    print(a + b)
```

Output:

```
30
```

The value is displayed but not returned.

---

## return

Returns the value back to the caller.

```python
def add(a, b):
    return a + b
```

Now the returned value can be stored in a variable.

```python
result = add(10, 20)
```

---

# Function Call

Defining a function does not execute it.

```python
def greet():
    print("Hello")
```

The function runs only after it is called.

```python
greet()
```

---

# Scope

Variables created inside a function are local.

```python
def demo():
    x = 10

print(x)
```

This results in an error because `x` exists only inside the function.

---

# Pass by Value vs Pass by Reference

### In C++

- Primitive types are generally passed by value unless references are used.
- References allow the function to modify the original variable.

### In Python

Python uses **object references**.

A simple way to remember:

- Immutable objects (`int`, `float`, `str`, `tuple`) behave like pass-by-value because you cannot modify the original object.
- Mutable objects (`list`, `dict`, `set`) can be modified inside the function, so changes are visible outside.

Example with integer:

```python
def change(x):
    x = 100

a = 10

change(a)

print(a)
```

Output:

```
10
```

The original integer remains unchanged.

Example with list:

```python
def change(arr):
    arr.append(100)

numbers = [1, 2, 3]

change(numbers)

print(numbers)
```

Output:

```
[1, 2, 3, 100]
```

The original list is modified because lists are mutable.

---

# DSA Relevance

Every LeetCode problem requires writing one or more functions.

Understanding parameters and return values is essential before solving DSA problems.

---

# Key Takeaways

- Functions improve code reusability.
- Functions can accept parameters.
- Functions can return values.
- `print()` and `return` are different.
- Local variables exist only inside functions.
- Python passes object references, so mutable and immutable objects behave differently.