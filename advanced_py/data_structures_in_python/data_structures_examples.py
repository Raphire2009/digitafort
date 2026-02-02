# Python Data Structures Examples

# --- Lists ---
my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list}")
my_list.append(6)
print(f"List after append: {my_list}")
my_list.remove(3)
print(f"List after remove: {my_list}")
print(f"Element at index 2: {my_list[2]}")

print("-" * 20)

# --- Tuples ---
my_tuple = (10, 20, 30, 40, 50)
print(f"Tuple: {my_tuple}")
# Tuples are immutable, so operations like append or remove are not available
print(f"Element at index 1: {my_tuple[1]}")

print("-" * 20)

# --- Dictionaries ---
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Dictionary: {my_dict}")
my_dict["email"] = "alice@example.com"
print(f"Dictionary after add: {my_dict}")
del my_dict["city"]
print(f"Dictionary after delete: {my_dict}")
print(f"Value for key 'name': {my_dict['name']}")

print("-" * 20)

# --- Sets ---
my_set = {1, 2, 3, 4, 5}
print(f"Set: {my_set}")
my_set.add(6)
print(f"Set after add: {my_set}")
my_set.remove(3)
print(f"Set after remove: {my_set}")
set2 = {4, 5, 6, 7, 8}
print(f"Union of sets: {my_set.union(set2)}")
print(f"Intersection of sets: {my_set.intersection(set2)}")
