# Array Methods (Python Lists)

## append()

### What is append()?

`append()` adds a single element to the **end** of a list.

It increases the size of the list by one.

---

## Why Do We Need append()?

Suppose you're maintaining a list of marks.

Initially:

```python
marks = [85, 90, 78]
```

A new student's marks arrive.

Instead of creating a new list, simply append them.

```python
marks.append(95)
```

Result:

```python
[85, 90, 78, 95]
```

---

## Syntax

```python
list.append(element)
```

---

## Parameters

Accepts **one element**.

Example:

```python
numbers.append(50)
```

---

## Return Value

Returns:

```python
None
```

It modifies the original list.

---

## Example

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```
[10, 20, 30, 40]
```

---

## Visual Representation

Before

```
+----+----+----+
|10  |20  |30  |
+----+----+----+
```

After

```
+----+----+----+----+
|10  |20  |30  |40  |
+----+----+----+----+
```

The new element is always added at the **end**.

---

## Time Complexity

Average Case:

```
O(1)
```

Occasionally Python needs to resize the underlying dynamic array, making a single append slower, but the average cost over many appends remains O(1).

---

## Space Complexity

```
O(1)
```

---

## DSA Usage

Commonly used when:

- Building an answer array.
- Storing traversal results.
- Creating prefix sum arrays.
- Collecting elements during iteration.

---

## Key Takeaways

- Adds exactly one element.
- Always adds at the end.
- Modifies the original list.
- Returns `None`.
- Average time complexity is O(1).

# extend()

## What is extend()?

`extend()` adds **multiple elements** from another iterable (list, tuple, etc.) to the **end** of the list.

---

## Syntax

```python
list.extend(iterable)
```

---

## Example

```python
numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)
```

Output:

```
[10, 20, 30, 40]
```

---

## append() vs extend()

```python
arr = [1, 2]

arr.append([3, 4])

print(arr)
```

Output:

```
[1, 2, [3, 4]]
```

---

```python
arr = [1, 2]

arr.extend([3, 4])

print(arr)
```

Output:

```
[1, 2, 3, 4]
```

---

## Time Complexity

```
O(k)
```

where `k` is the number of elements being added.

---

## Key Takeaways

- Adds multiple elements.
- Modifies the original list.
- Returns `None`.

# insert()

## What is insert()?

`insert()` adds an element at a specific index.

Unlike `append()`, the element is **not always added at the end**.

---

## Syntax

```python
list.insert(index, element)
```

---

## Example

```python
arr = [10, 20, 30]

arr.insert(1, 15)

print(arr)
```

Output:

```
[10, 15, 20, 30]
```

---

## Visual

Before

```
10 20 30
```

Insert 15 at index 1

```
10 15 20 30
```

Elements after index 1 shift one position to the right.

---

## Time Complexity

```
O(n)
```

---

## Key Takeaways

- Inserts at any index.
- Existing elements shift right.
- Modifies the original list.
- Returns `None`.

# pop()

## What is pop()?

`pop()` removes and returns an element from the list.

---

## Syntax

```python
list.pop(index)
```

If no index is given, it removes the **last element**.

---

## Example 1

```python
arr = [10, 20, 30]

arr.pop()

print(arr)
```

Output

```
[10, 20]
```

---

## Example 2

```python
arr = [10, 20, 30]

arr.pop(1)

print(arr)
```

Output

```
[10, 30]
```

---

## Return Value

Unlike `append()` and `insert()`, `pop()` returns the removed element.

```python
x = arr.pop()

print(x)
```

Output

```
30
```

---

## Time Complexity

Removing last element

```
O(1)
```

Removing from middle/front

```
O(n)
```

because elements shift left.

---

## Key Takeaways

- Removes by **index**.
- Returns the removed element.
- Default removes the last element.

# remove()

## What is remove()?

`remove()` removes the **first occurrence of a value**.

---

## Syntax

```python
list.remove(value)
```

---

## Example

```python
arr = [10, 20, 30]

arr.remove(20)

print(arr)
```

Output

```
[10, 30]
```

---

## Return Value

Returns

```
None
```

---

## Time Complexity

```
O(n)
```

Python first searches for the value, then shifts remaining elements.

---

## Key Takeaways

- Removes by **value**.
- Removes only the first occurrence.
- Returns `None`.

# clear()

## What is clear()?

`clear()` removes all elements from a list.

---

## Syntax

```python
list.clear()
```

---

## Example

```python
arr = [10, 20, 30]

arr.clear()

print(arr)
```

Output

```
[]
```

---

## Return Value

Returns

```
None
```

---

## Time Complexity

```
O(n)
```

---

## Key Takeaways

- Removes every element.
- The list still exists.
- Only its contents are removed.

# index()

## What is index()?

Returns the index of the **first occurrence** of a value.

---

## Syntax

```python
list.index(value)
```

---

## Example

```python
arr = [10, 20, 30, 20]

print(arr.index(20))
```

Output

```
1
```

---

## Return Value

Returns the index.

---

## Time Complexity

```
O(n)
```

---

## Key Takeaways

- Searches by value.
- Returns the first matching index.
- Raises `ValueError` if the value is not found.

# count()

## What is count()?

Returns how many times a value appears in the list.

---

## Syntax

```python
list.count(value)
```

---

## Example

```python
arr = [1, 2, 2, 3]

print(arr.count(2))
```

Output

```
2
```

---

## Time Complexity

```
O(n)
```
# sort()

## What is sort()?

Sorts the original list in ascending order.

---

## Syntax

```python
list.sort()
```

Descending order:

```python
list.sort(reverse=True)
```

---
## Return Value

```
None
```

---

## Time Complexity

```
O(n log n)
```

# reverse()

## What is reverse()?

Reverses the order of elements in the original list.

---

## Example

```python
arr = [1, 2, 3]

arr.reverse()

print(arr)
```

Output

```
[3, 2, 1]
```

---

## Return Value

```
None
```

---

## Time Complexity

```
O(n)
```
# copy()

## What is copy()?

Creates a shallow copy of a list.

---

## Example

```python
arr = [10, 20, 30]

new_arr = arr.copy()

print(new_arr)
```

Output

```
[10, 20, 30]
```

---

## Time Complexity

```
O(n)
```

---

## Why use copy()?

Without `copy()`:

```python
a = [1, 2, 3]
b = a
```

Both variables point to the **same list**.

With `copy()`:

```python
b = a.copy()
```

Now they are **different lists**.