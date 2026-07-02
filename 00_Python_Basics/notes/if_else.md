# Conditional Statements (if, elif, else)

## What are Conditional Statements?

Conditional statements allow a program to make decisions based on a given condition.

Instead of executing every line of code, the program checks whether a condition is `True` or `False` and executes only the appropriate block of code.

---

# Why Do We Need Conditional Statements?

Without conditions, a program would always produce the same output regardless of the input.

Example:

Suppose we want to check whether a person is eligible to vote.

Without conditions:

```python
print("Eligible to vote")
```

Everyone would be considered eligible, which is incorrect.

Using conditional statements:

```python
age = 17

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

The output now depends on the user's input.

---

# Syntax

## if

```python
if condition:
    # code
```

---

## if - else

```python
if condition:
    # code
else:
    # code
```

---

## if - elif - else

```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

---

# How Python Executes Conditions

Python evaluates conditions from **top to bottom**.

* If a condition is `True`, its block executes.
* The remaining conditions are skipped.
* If no condition is `True`, the `else` block executes.

---

# Comparison Operators

These operators compare two values and return either `True` or `False`.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not Equal to             |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or Equal to |
| <=       | Less than or Equal to    |

Example:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

---

# Logical Operators

Logical operators combine multiple conditions.

## and

Both conditions must be `True`.

```python
if age >= 18 and citizen:
```

---

## or

At least one condition must be `True`.

```python
if age >= 18 or has_permission:
```

---

## not

Reverses the result.

```python
if not is_logged_in:
```

---

# Examples

## Example 1

```python
age = 21

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

## Example 2

```python
marks = 82

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
```

---

# Order of Conditions

The order of conditions is extremely important.

Correct:

```python
if marks >= 90:
    ...
elif marks >= 75:
    ...
elif marks >= 50:
    ...
```

Incorrect:

```python
if marks >= 50:
    ...
elif marks >= 75:
    ...
```

In the incorrect example, a student scoring 82 will receive grade **C** instead of **B** because Python stops after the first `True` condition.

---

# DSA Relevance

Conditional statements are used in almost every DSA problem.

Examples:

* Check whether a number is even or odd.
* Find the largest element.
* Check whether an array is sorted.
* Validate edge cases.
* Compare elements during searching and sorting.

---

# Interview Notes

* Think about the order of conditions.
* Handle edge cases first when necessary.
* Keep conditions simple and readable.
* Avoid unnecessary nesting when possible.

---

# Key Takeaways

* `if` executes when the condition is `True`.
* `elif` checks additional conditions.
* `else` executes when all previous conditions are `False`.
* Python checks conditions from top to bottom.
* The first `True` condition executes.
* Correct ordering of conditions is essential.
