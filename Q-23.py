name = input("Enter a Name : ")
if len(name) > 2:
    name1 = name[0:2] + name[-2:]
else:
    print("Empty Name")
print(name1)    