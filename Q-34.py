list1 = ["rushik","mital","roshni","harsh","roshni"]
list2 = ["rushik","harsh","vishal","kiran","ghanshyam"]
a = False

for i in list1:
    for n in list2:
        if i == n :
            a = True
            print(a)
    if a == True:
        break    