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

# While Loops

## Mistake 1: Forgetting to Update the Variable

### Wrong

```python
count = 1

while count <= 5:
    print(count)
```

### Problem

The condition always remains `True`.

The loop never ends.

### Learning

Always update the loop variable.

Example:

```python
count += 1
```

---

## Mistake 2: Wrong Condition

### Wrong

```python
count = 5

while count <= 1:
    print(count)
```

### Problem

The condition is already `False`.

The loop never executes.

### Learning

Check the initial value and the loop condition carefully.

---

## Mistake 3: Infinite Loop

### Wrong

```python
while True:
    print("Hello")
```

### Problem

The loop runs forever unless manually stopped.

### Learning

Use `break` or change the condition when an infinite loop is not intended.

---

## Mistake 4: Using a for Loop When a while Loop is More Suitable

Example:

Reading user input until the user enters `"exit"`.

Using a `while` loop is simpler because the number of inputs is unknown.

### Learning

Choose the loop based on the problem, not personal preference.

# Functions

## Mistake 1: Defining a Function but Never Calling It

### Wrong

```python
def greet():
    print("Hello")
```

### Problem

Nothing happens.

### Learning

A function executes only when it is called.

```python
greet()
```

---

## Mistake 2: Forgetting return

### Wrong

```python
def add(a, b):
    a + b
```

### Problem

The function returns `None`.

### Learning

Use `return` when the result needs to be sent back.

---

## Mistake 3: Confusing print() with return

`print()` displays a value.

`return` sends a value back to the caller.

They are not the same.

---

## Mistake 4: Accessing Local Variables Outside the Function

### Wrong

```python
def demo():
    x = 10

print(x)
```

### Error

```
NameError
```

### Learning

Local variables exist only inside the function.

---

## Mistake 5: Assuming Lists Behave Like Integers

Lists are mutable.

Changes made inside a function affect the original list.

Integers are immutable.

Changing them inside a function does not affect the original variable.

# Time Complexity

## Mistake 1: Measuring Time in Seconds

### Wrong Thinking

"This code runs in 2 seconds, so its complexity is O(2)."

### Learning

Time Complexity does not measure seconds.

It measures how the number of operations grows with the input size.

---

## Mistake 2: Thinking Two Separate Loops Mean O(n²)

### Wrong

```python
for i in range(n):
    ...

for j in range(n):
    ...
```

Complexity:

```
O(n²)
```

### Correct

```
O(n + n)

↓

O(2n)

↓

O(n)
```

---

## Mistake 3: Forgetting That Nested Loops Multiply

```python
for i in range(n):
    for j in range(n):
```

Complexity:

```
O(n²)
```

Not:

```
O(2n)
```

---

## Mistake 4: Keeping Constants

```
O(5n)

↓

O(n)
```

Always ignore constants in Big O notation.

# Space Complexity

## Mistake 1: Counting the Input Array

### Wrong Thinking

```
arr = [1,2,3]

Space = O(n)
```

### Learning

The input array is **not counted**.

Only extra memory created by the algorithm is counted.

---

## Mistake 2: Confusing Time with Space

A single loop:

```python
for i in arr:
```

means

Time:

```
O(n)
```

It does **not** mean

Space:

```
O(n)
```

If no additional data structure is created, the space complexity remains:

```
O(1)
```

---

## Mistake 3: Forgetting Extra Arrays

Creating another list:

```python
copy = arr.copy()
```

requires additional memory.

Space Complexity:

```
O(n)
```