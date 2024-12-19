string = input("Enter a String : ")

str_count = {}

for i in string:
    if i in str_count:
        str_count[i] += 1
    else :
        str_count[i] = 1

for n,r in str_count.items():   
    print(f"{n} : {r}")