d1 = {"name":"Rushik",
    "age":20,
    "cast":"Hindu"}

l1 = ["name","age","cast"]

status = True

for i in l1:
    if i in d1:
        print(f"the {i} Existe in dictionary")
    else:
        print(f"the {i} dose not Existe in dictionary")
        status = False
        
if status:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
    