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