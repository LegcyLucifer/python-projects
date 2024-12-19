list1 = ["abc","aba","ewe","mam","sir","net"]
count = 0
for i in list1:
    if len(i) >=2 and i[0] == i[-1]:
        count += 1
print(list1)
print(f"{count}")
