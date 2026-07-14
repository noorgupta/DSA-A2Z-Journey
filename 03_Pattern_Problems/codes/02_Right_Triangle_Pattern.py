"""
Pattern 02: Right Triangle Pattern

*
**
***
****
*****

Time Complexity: O(n²)
Space Complexity: O(1)
"""

n = 1

while n < 6:
    for rows in range(n):
        print("*", end="")
    n = n + 1
    print()