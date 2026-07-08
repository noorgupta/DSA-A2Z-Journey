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
# Switch Case

## Mistake 1: Searching for Traditional Switch Case in Python

### Problem

Trying to write C++ or Java style `switch-case` syntax in Python.

### Learning

Python does not support the traditional switch-case statement.

Use:

* `if-elif-else`
* Dictionary mapping
* `match-case` (Python 3.10+)

---

## Mistake 2: Forgetting the Default Case

When using dictionaries:

```python
days.get(day)
```

If the key does not exist, the result will be `None`.

### Better

```python
days.get(day, "Invalid Day")
```

Always provide a default value when appropriate.

# For Loops

## Mistake 1: Assuming range(5) Includes 5

### Wrong Assumption

```python
range(5)
```

Expected:

```
1 2 3 4 5
```

### Reality

```
0 1 2 3 4
```

### Learning

`range(stop)` always starts from **0** and stops **before** the stop value.

---

## Mistake 2: Forgetting Indentation

### Wrong

```python
for i in range(5):
print(i)
```

### Error

```
IndentationError
```

### Learning

Always indent the code inside a loop.

---

## Mistake 3: Using Step = 0

### Wrong

```python
range(1, 10, 0)
```

### Error

```
ValueError: range() arg 3 must not be zero
```

### Learning

The step value must never be zero.

---

## Mistake 4: Using the Wrong Loop Boundary

### Example

```python
for i in range(1, 5):
```

Some beginners expect:

```
1 2 3 4 5
```

Actual output:

```
1 2 3 4
```

### Learning

The stop value is always excluded.
