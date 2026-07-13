# Linear Search

## What is Linear Search?

Linear Search is the simplest searching algorithm.

It checks each element one by one until the target element is found or the array ends.

---

## Example

```python
arr = [10, 20, 30, 40, 50]
target = 30
```

Traversal:

```
10 ❌

20 ❌

30 ✅ Found
```

---

## Algorithm

1. Start from the first element.
2. Compare it with the target.
3. If matched, return its index.
4. Otherwise, move to the next element.
5. If the array ends, the element is not present.

---

## Syntax

```python
for i in range(len(arr)):
    if arr[i] == target:
        return i

return -1
```

---

## Time Complexity

Best Case

```
O(1)
```

(Target found at the first position.)

Average Case

```
O(n)
```

Worst Case

```
O(n)
```

(Target is at the last position or not present.)

---

## Space Complexity

```
O(1)
```

---

## Applications

- Small datasets
- Unsorted arrays
- Simple searching tasks

---

## Key Takeaways

- Checks elements one by one.
- Works on both sorted and unsorted arrays.
- Easy to implement.