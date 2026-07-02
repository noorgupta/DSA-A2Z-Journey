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

# Conditional Statements

## Mistake 3: Using Assignment Instead of Comparison

### Wrong

```python
if age = 18:
```

### Error

```text
SyntaxError
```

### Why It Happened

`=` assigns a value.

Conditions require comparison using `==`.

### Correct

```python
if age == 18:
```

---

## Mistake 4: Wrong Order of Conditions

### Wrong

```python
if marks >= 50:
    print("C")
elif marks >= 75:
    print("B")
```

### Why It Happened

Python executes the first `True` condition and skips the rest.

A student scoring 82 will incorrectly receive grade `C`.

### Learning

Always write more specific conditions before broader ones.

---

## Mistake 5: Forgetting the Colon

### Wrong

```python
if age >= 18
    print("Eligible")
```

### Error

```text
SyntaxError
```

### Learning

Every `if`, `elif`, and `else` statement must end with a colon (`:`).

---

## Mistake 6: Incorrect Indentation

### Wrong

```python
if age >= 18:
print("Eligible")
```

### Error

```text
IndentationError
```

### Learning

Python uses indentation to define blocks of code.

Always indent the statements inside `if`, `elif`, and `else`.

---

## Mistake 7: Assuming All Conditions Execute

Some beginners think Python checks every condition.

Reality:

Python stops after the **first `True` condition** in an `if-elif-else` chain.

### Learning

Remember the execution flow:

```text
Top
 ↓
Check condition
 ↓
True?
 ↓
Execute
 ↓
Stop checking remaining conditions
```
