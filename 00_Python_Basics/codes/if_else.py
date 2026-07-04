# Example 1
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

print("-" * 40)

# Example 2
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A,excellent")
elif marks >= 75:
    print("Grade B,good")
elif marks >= 50:
    print("Grade C,Improve")
else:
    print("Fail")