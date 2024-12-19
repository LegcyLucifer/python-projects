status = True 
while status:
    letter  = input("Enter a letter : ")

    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
        print("This is a vowel number")
    else : 
        print("This is not vowel number")
    
    choice = input("do you want to repeat this program : yes or no : ")
    if choice == "yes":
        status = True
    else : 
        status = False
        print("thanks for visiting")