# 📌 Python List Methods - Quick Revision

| Method | Purpose | Syntax | Returns | Time Complexity |
|---------|---------|--------|---------|-----------------|
| `append(x)` | Add one element at the end | `arr.append(x)` | `None` | **O(1)** (Average) |
| `extend(iterable)` | Add multiple elements at the end | `arr.extend(iterable)` | `None` | **O(k)** |
| `insert(i, x)` | Insert element at a specific index | `arr.insert(i, x)` | `None` | **O(n)** |
| `pop()` | Remove and return the last element | `arr.pop()` | Removed element | **O(1)** |
| `pop(i)` | Remove and return element at index `i` | `arr.pop(i)` | Removed element | **O(n)** |
| `remove(x)` | Remove first occurrence of a value | `arr.remove(x)` | `None` | **O(n)** |
| `clear()` | Remove all elements | `arr.clear()` | `None` | **O(n)** |
| `index(x)` | Return first index of a value | `arr.index(x)` | Index | **O(n)** |
| `count(x)` | Count occurrences of a value | `arr.count(x)` | Integer | **O(n)** |
| `sort()` | Sort the list | `arr.sort()` | `None` | **O(n log n)** |
| `reverse()` | Reverse the list | `arr.reverse()` | `None` | **O(n)** |
| `copy()` | Create a shallow copy | `arr.copy()` | New List | **O(n)** |