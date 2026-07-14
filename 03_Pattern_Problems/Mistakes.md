# Pattern 02 - Right Triangle Pattern

## Mistake 1

Initially, I increased `n` inside the inner loop.

```python
for rows in range(n):
    ...
    n = n + 1
```

### Learning

The row counter should be updated **after** the current row is completely printed.

---

## Mistake 2

Initially, I printed:

```python
print("*" * n)
```

inside the inner loop.

### Learning

This prints multiple stars repeatedly.

Instead, the inner loop should print **one star at a time**.

---

## Mistake 3

I wasn't sure whether:

```python
n = n + 1
```

was increasing the `for` loop.

### Learning

No.

The `for` loop evaluates:

```python
range(n)
```

only once when it starts.

Updating `n` later affects only the **next iteration** of the `while` loop.