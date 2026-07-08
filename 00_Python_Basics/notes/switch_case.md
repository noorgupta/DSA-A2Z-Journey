# Switch Case (Python Alternative)

> **📝 Note:** This topic exists in Striver's sheet for C++/Java learners. Python does not have a traditional switch-case statement, so this section explains the concept and the Python alternatives.

=
## What is Switch Case?

A switch-case statement is a control structure used to execute different blocks of code based on the value of a variable.

Instead of writing multiple `if-elif` statements, a switch-case provides a cleaner way to handle many fixed choices.

---

# Why Do We Need It?

Suppose we want to print the day of the week.

Without switch-case:

```python
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
```

As the number of choices increases, the code becomes longer.

A switch-case provides a more organized solution in languages that support it.

---

# Does Python Have Switch Case?

No.

Python does **not** support the traditional switch-case statement found in languages like C++ or Java.

Instead, Python programmers use:

* `if-elif-else`
* Dictionaries (mapping)
* `match-case` (introduced in Python 3.10)

---

# Python Alternative 1: if-elif-else

```python
day = 2

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
else:
    print("Invalid")
```

---

# Python Alternative 2: Dictionary Mapping

```python
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday"
}

print(days.get(2, "Invalid"))
```

Output:

```text
Tuesday
```

The `get()` method returns a default value if the key does not exist.

---

# Python Alternative 3: match-case (Python 3.10+)

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")
```

This is the closest feature to a traditional switch-case.

---

# When Should We Use Each?

| Situation              | Preferred Choice |
| ---------------------- | ---------------- |
| Simple decision making | if-elif-else     |
| Mapping fixed values   | Dictionary       |
| Python 3.10+ projects  | match-case       |

---

# DSA Relevance

Switch-case is **rarely used** in DSA.

Most DSA problems rely on:

* `if`
* `elif`
* `else`

Understanding conditional logic is much more important than memorizing switch-case syntax.

---

# Interview Notes

* Don't worry if Python doesn't have switch-case.
* Write clean `if-elif-else` code when appropriate.
* Use dictionaries only when you're mapping fixed values.
* Understand the concept rather than the syntax.

---

# Key Takeaways

* Traditional switch-case is not available in Python.
* `if-elif-else` is the standard replacement.
* Dictionaries provide an elegant mapping solution.
* `match-case` is available in Python 3.10 and later.
