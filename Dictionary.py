# -------------------------------
# Dictionary Operations in Python
# -------------------------------

# 1. Creating and Initializing Dictionaries

# a) Using curly braces
student = {
    "name": "Rahul",
    "age": 20,
    "course": "B.Tech"
}

# b) Using dict() constructor
student2 = dict(name="Amit", age=21, course="B.Sc")

# c) Empty dictionary
empty_dict = {}

# d) Dictionary with mixed key types
mixed_dict = {
    1: "One",
    "two": 2,
    (3, 4): "Tuple as key"
}

# -------------------------------
# 2. Accessing Elements
# -------------------------------

# a) Access using square brackets
print("Name:", student["name"])

# b) Access using get() method (safe access)
print("Age:", student.get("age"))
print("Marks (default):", student.get("marks", 0))

# -------------------------------
# 3. Accessing Keys, Values, Items
# -------------------------------

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# -------------------------------
# 4. Accessing using loop
# -------------------------------

print("Student Details:")
for key, value in student.items():
    print(key, ":", value)
