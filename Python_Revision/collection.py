#  Collection/Array of clooection
#  list
#  tuple
#  set
#  dictionary

# List
# 1️⃣ List (list) - Ordered & Changeable 📋
# A list is like a shopping list — it keeps items in order, and you can add, remove, or change them.

# ✅ Key Features:
# Ordered (items stay in the same order)
# Mutable (you can change items)
# Allows duplicates

fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
# Modify the list
fruits.append("mango")  # Add an item
fruits[0] = "blueberry"  # Change an item
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'mango']

# tuple
# A tuple is like a locked box — you can see what’s inside, but you can’t change it!

# ✅ Key Features:
# Ordered
# Immutable (cannot be changed)
# Allows duplicates

coordinates = (10, 20, 30)
print(coordinates)  # Output: (10, 20, 30)
# Trying to change a tuple gives an error!
# coordinates[1] = 50  ❌ TypeError: 'tuple' object does not support item assignment


# Dictonary
# 3️⃣ Dictionary (dict) - Key-Value Pairs 🗂️
# A dictionary is like a contact list — you store values with unique keys for fast lookup!

# ✅ Key Features:
# Stores key-value pairs
# Unordered (but keeps order in Python 3.7+)
# Keys must be unique

person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Accessing values
print(person["name"])  # Output: Alice
# Adding & modifying values
person["age"] = 26
person["email"] = "alice@example.com"
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Set 
# 4️⃣ Set (set) - Unordered & Unique 🔥
# A set is like a bag of unique items — it doesn’t allow duplicates and is great for mathematical operations.

# ✅ Key Features:
# Unordered
# Mutable
# No duplicate values

numbers = {1, 2, 3, 4, 4, 5}  # Duplicate 4 is removed automatically
print(numbers)  # Output: {1, 2, 3, 4, 5}
# Adding elements
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}
# Removing elements
numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5, 6}

def function_2():
    # iterate using list 
    List_1 = [10,20,30,40,50]
    # iterate using for 
    for value in List_1:
        print(value)
    # iterate by index
    index_positions = list(range(len(List_1)))
    for index in index_positions:
        print(f"value at {index} = {List_1[index]}")

print("-*-"*20)

function_2()