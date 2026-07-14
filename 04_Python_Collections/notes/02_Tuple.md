# Tuple

## 📖 What is a Tuple?

A tuple is an **ordered** and **immutable** collection in Python used to store multiple values.

Once a tuple is created, its elements cannot be modified, added, or removed.

Example:

```python
student = ("Noor", 20, "BCA")
```

---

## 🤔 Why Am I Learning Tuples?

Some data should never change after it is created.

Examples:

- Coordinates `(x, y)`
- RGB colors `(255, 255, 255)`
- Days of the week
- Months of the year

Tuples help represent such fixed data.

---

## 📌 Characteristics

- Ordered
- Immutable
- Allows duplicate values
- Supports indexing
- Supports slicing
- Faster than lists for read-only data

---

## Example

```python
coordinates = (10, 20)

print(coordinates[0])
```

---

## Difference Between List and Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Slightly slower | Slightly faster |
| More memory | Less memory |

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Access | O(1) |
| Search | O(n) |
| Index | O(n) |
| Count | O(n) |

---

## DSA Applications

- Returning multiple values from a function.
- Representing coordinates.
- Storing fixed information.
- Dictionary keys (when immutable data is needed).

---

## Key Takeaways

- Tuples are ordered and immutable.
- They are ideal for fixed data.
- They cannot be modified after creation.