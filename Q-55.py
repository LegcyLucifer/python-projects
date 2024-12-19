d1 = {1 : "rushik" , 2 : "mital" , 3 : "harsh"}
d2 = {4 : "mann" , 5 : "jignesh" , 6 : "anand"}

merge_dict = {}

for i in d1:
    merge_dict[i] = d1[i]
for i in d2:
    merge_dict[i] = d2[i]
    
print(merge_dict)