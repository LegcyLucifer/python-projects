list1 = ["rushik","mital","rushik","roshni","harsh","roshni"]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
    
print(f"Before List : {list1}")
print(f"After List : {list2}")