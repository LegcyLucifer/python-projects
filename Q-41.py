list1 = [1,2,3,4,5,6]
list2 = [5,6,7,8,9,10]
list3 = []

for i in list1:
    for n in list2:
        if n == i:
            list3.append(n)
            
print(list3)