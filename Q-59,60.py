string = "w3resource"

count = 1

d1 = {}

for i in string:
    if i in d1:
        count += 1
        d1[i] = count
    else:
        d1[i] = count
    count = 1
    
print(d1)