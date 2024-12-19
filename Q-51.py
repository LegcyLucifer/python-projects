# How Do You Traverse Through a Dictionary Object in Python? 

# Traverse through keys : 

d1 = {"d1":1,"d2":2,"d3":3,"d4":4}

for i in d1.keys():
    print(i)
print()
    
# Traverse through value : 

for n in d1.values():
    print(n)
print()
    
# Traverse through key-value pairs

for i,o in d1.items():
    print(f"{i} = {o}")
print()