"""
Pattern 1

*****
*****
*****
*****
*****

Time Complexity: O(n²)
Space Complexity: O(1)
"""
##Code 

for rows in range(5):
    for columns in range(5):
        print("*", end="") # Print on same line
    print()                # Move to next line


## Observation

Rows = 5

Columns = 5

Outer Loop → Rows

Inner Loop → Columns

---

## Logic

(Short explanation after you solve it.)

---

## Time Complexity

O(n²)

---

## Space Complexity

O(1)

---

## Learning

- Learned nested loops.
- Learned `print(..., end="")`.
- Learned the purpose of `print()`.