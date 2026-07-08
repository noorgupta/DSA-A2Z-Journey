# Using if-elif-else

day = int(input("Enter day number (1-3): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Invalid Day")

print("-" * 40)

# Using Dictionary

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday"
}

print(days.get(day, "Invalid Day"))