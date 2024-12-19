status = True
while status: 
    input1 = input("Enter a word : ")
    if input1 > input1[0:3]:
        a = input1 + "in"
        if input1[-3:] == "ing":
            a = input1 + "ly "
    else :
        a = input1
    print(f"Your output is : {a}")
    choice = input("do you want repet this program : yes or no : ")
    if choice == "yes":
        status = True
    else : 
        status = False