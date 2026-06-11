# Mistakes

---

# Input / Output

## Mistake 1: Invalid Integer Conversion

### Code

```python
n = int(input("Enter anything: "))

```

### Input Given

```text
a
```

### Error

```python
ValueError: invalid literal for int() with base 10: 'a'
```

### Why It Happened

`input()` always returns a string.

When the user entered:

```text
a
```

Python received:

```python
"a"
```

Then Python tried to execute:

```python
int("a")
```

Since `"a"` is not a valid integer, Python raised a `ValueError`.

### Learning

Only use:

```python
int(input())
```

when numeric input is expected.

Examples:

 Valid

```text
10
25
100
```

 Invalid

```text
a
hello
python
```

### Key Takeaway

`input()` returns a string.

Before converting to an integer, ensure the input contains a valid numeric value.

# Common Mistakes

## Mistake 1

```python
int("hello")
```

Error:

```text
ValueError
```

Reason:

Python cannot convert alphabetic text into an integer.

---

## Mistake 2

```python
n = input()
```

Input:

```text
100
```

Many beginners think:

```python
n = 100
```

Reality:

```python
n = "100"
```

because `input()` always returns a string.

---
