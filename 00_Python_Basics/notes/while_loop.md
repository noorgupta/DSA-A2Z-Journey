# While Loops

## What is a While Loop?

A `while` loop is a control statement that repeatedly executes a block of code **as long as a given condition remains True**.

Unlike a `for` loop, a `while` loop does not require knowing the number of iterations beforehand.

---

# Why Do We Need a While Loop?

There are situations where we don't know how many times a task needs to repeat.

Example:

Imagine filling a water tank.

```
While the tank is not full:
    Keep filling water.
```

You don't know how many buckets of water will be needed.

You only know the condition.

---

# Syntax

```python
while condition:
    # code
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

# How Does a While Loop Work?

Python follows these steps:

1. Check the condition.
2. If the condition is `True`, execute the loop body.
3. Update the variable.
4. Go back and check the condition again.
5. Stop when the condition becomes `False`.

---

# Flow of Execution

Example:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

Execution:

```
count = 1
Condition → True
Print 1

count = 2
Condition → True
Print 2

count = 3
Condition → True
Print 3

count = 4
Condition → False

Loop Ends
```

---

# Examples

## Example 1

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

## Example 2

Print even numbers from 2 to 10.

```python
num = 2

while num <= 10:
    print(num)
    num += 2
```

Output:

```
2
4
6
8
10
```

---

## Example 3

Countdown Timer

```python
count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast Off!")
```

Output:

```
5
4
3
2
1
Blast Off!
```

---

# Difference Between for and while

| for Loop | while Loop |
|-----------|------------|
| Used when the number of iterations is known. | Used when the number of iterations is unknown. |
| Uses `range()` frequently. | Uses a condition. |
| Automatically moves to the next value. | Programmer updates the variable manually. |

---

# When Should We Use a While Loop?

Use a `while` loop when:

- The number of iterations is not known.
- The loop depends on a condition.
- Waiting for user input.
- Game loops.
- Menu-driven programs.

---

# DSA Relevance

While loops are commonly used in:

- Binary Search
- Linked Lists
- Trees
- Graph Traversals
- Fast and Slow Pointer problems
- Two Pointer techniques

Understanding while loops is essential before starting DSA.

---

# Key Takeaways

- A `while` loop repeats until the condition becomes `False`.
- Always update the loop variable.
- Forgetting to update the variable can cause an infinite loop.
- Use `while` when the number of iterations is unknown.