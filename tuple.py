# --------------------------------
# Tuple Operations in Python
# --------------------------------

# Creating tuples
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)

# --------------------------------
# 1. Accessing and Indexing Elements
# --------------------------------

# Access by index
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("Slice (1 to 3):", numbers[1:4])

# Looping through tuple
for item in numbers:
    print("Item:", item)

# --------------------------------
# 2. Nested Tuples (Hierarchical Data)
# --------------------------------

student = (
    "Rahul",
    20,
    ("B.Tech", "Computer Science"),
    ("Maths", "Physics", "Programming")
)

print("Student Name:", student[0])
print("Degree:", student[2][0])
print("Department:", student[2][1])
print("First Subject:", student[3][0])

# --------------------------------
# 3. Immutability and Hashing
# --------------------------------

# Tuples are immutable (cannot be modified)
# numbers[0] = 100  # ❌ This will raise TypeError

# Tuple can be used as dictionary key (hashable)
student_scores = {
    ("Rahul", "Maths"): 90,
    ("Rahul", "Physics"): 85
}

print("Tuple as dictionary key:", student_scores)

# Hash value of tuple
print("Hash of tuple:", hash(numbers))

# --------------------------------
# 4. Concatenation and Repetition
# --------------------------------

tuple_a = (1, 2, 3)
tuple_b = (4, 5)

# Concatenation
combined_tuple = tuple_a + tuple_b
print("Concatenated Tuple:", combined_tuple)

# Repetition
repeated_tuple = tuple_a * 3
print("Repeated Tuple:", repeated_tuple)
