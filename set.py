# -------------------------------
# Set Operations in Python
# -------------------------------

# Creating sets
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print("Set A:", set_a)
print("Set B:", set_b)

# -------------------------------
# 1. Adding Elements
# -------------------------------

# Add a single element
set_a.add(70)
print("After add:", set_a)

# Add multiple elements
set_a.update([80, 90])
print("After update:", set_a)

# -------------------------------
# 2. Removing Elements
# -------------------------------

# Remove a specific element (error if not present)
set_a.remove(20)
print("After remove:", set_a)

# Remove an element safely (no error if not present)
set_a.discard(100)
print("After discard:", set_a)

# Remove and return a random element
removed_element = set_a.pop()
print("Removed element using pop():", removed_element)
print("After pop:", set_a)

# -------------------------------
# 3. Union Operation
# -------------------------------

union_set = set_a.union(set_b)
print("Union:", union_set)

# Alternative way
print("Union using | :", set_a | set_b)

# -------------------------------
# 4. Intersection Operation
# -------------------------------

intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

# Alternative way
print("Intersection using & :", set_a & set_b)

# -------------------------------
# 5. Difference Operation
# -------------------------------

difference_set = set_a.difference(set_b)
print("Difference (A - B):", difference_set)

# Alternative way
print("Difference using - :", set_a - set_b)

# -------------------------------
# Clear the set
# -------------------------------

temp_set = {1, 2, 3}
temp_set.clear()
print("After clear:", temp_set)
