status = True

while status:
    user = int(input("Enter a number : "))
    
    if user % 2 == 0 : 
        print(f"this is even number")
    else : 
        print("this is odd number")
    
    choice = input("do you want to repeat this program : yes or no : ") 
    if choice == "yes":
        status = True
    else :
        status = False
        print("Thanks for visiting")  