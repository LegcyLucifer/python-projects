# How will you create a dictionary using tuples in python ? 

# 1. Using the dict() Function:

tuple_list = [(1,"Rushik"),(2,"Mital"),(3,"Harsh")]

dictionary = dict(tuple_list)

print(dictionary)

# 2. Using a For Loop:

dictionary1 = {}

for i,o in tuple_list:
    dictionary1[i] = o
    
print(dictionary1)