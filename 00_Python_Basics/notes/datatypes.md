# Data Types

## What Are Data Types?

A datatype defines the type of value stored in a variable.

Python uses datatypes to determine:

* How data is stored
* What operations can be performed
* How memory is managed

Example:

```python
age = 20
name = "Noor"
price = 99.99
```

Here:

```text
20      → int
"Noor"  → str
99.99   → float
```

---

# Why Do We Need Data Types?

Different kinds of data behave differently.

Example:

```python
10 + 20
```

Output:

```text
30
```

---

```python
"10" + "20"
```

Output:

```text
1020
```

Although both look similar, the result is different because the datatypes are different.

---

# int

## What is int?

`int` stands for integer.

It stores whole numbers.

Examples:

```python
age = 20
marks = 95
temperature = -10
```

Check datatype:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

---

# float

## What is float?

`float` stores decimal numbers.

Examples:

```python
cgpa = 8.5
price = 99.99
```

Check datatype:

```python
print(type(cgpa))
```

Output:

```text
<class 'float'>
```

---

# str

## What is str?

`str` stands for string.

Strings are used to store text.

Examples:

```python
name = "Noor"
city = "Delhi"
```

Check datatype:

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

---

# bool

## What is bool?

A boolean stores only two values:

```python
True
False
```

Examples:

```python
is_logged_in = True
is_admin = False
```

Check datatype:

```python
print(type(is_logged_in))
```

Output:

```text
<class 'bool'>
```

---

# type()

## What is type()?

`type()` is used to check the datatype of a variable or value.

Example:

```python
n = 10

print(type(n))
```

Output:

```text
<class 'int'>
```

---

# Type Conversion

Type conversion means converting one datatype into another.

---

## String → Integer

```python
a = "25"

b = int(a)
```

Result:

```python
b = 25
```

Datatype:

```python
<class 'int'>
```

---

## String → Float

```python
price = "99.99"

price = float(price)
```

Result:

```python
99.99
```

---

## Integer → String

```python
age = 20

age = str(age)
```

Result:

```python
"20"
```

Datatype:

```python
<class 'str'>
```

---

## Float → Integer

```python
x = 9.99

x = int(x)
```

Result:

```python
9
```

Important:

```text
int() does not round.
It removes the decimal part.
```

---

# DSA Relevance

Understanding datatypes is essential because:

* Inputs are received as strings.
* Calculations require integers or floats.
* Conditions use booleans.
* Most bugs in beginner DSA problems are caused by incorrect datatype handling.

---

# Key Takeaways

* `int` stores whole numbers.
* `float` stores decimal numbers.
* `str` stores text.
* `bool` stores `True` or `False`.
* `type()` checks the datatype.
* Type conversion is frequently used in DSA problems.
* `input()` always returns a string.
