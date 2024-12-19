# How Do You Check the Presence of a Key in A Dictionary? 

# 1. Using the in Keyword
# This is the most common and straightforward way to check if a key exists in a dictionary.


my_dict = {"name": "Alice", "age": 25, "city": "New York"}

if "name" in my_dict:
    print("Key 'name' exists")
else:
    print("Key 'name' does not exist")