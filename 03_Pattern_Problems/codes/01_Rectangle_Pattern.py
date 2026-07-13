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

for rows in range(5):
    for columns in range(5):
        print("*", end="") # Print on same line
    print()                # Move to next line