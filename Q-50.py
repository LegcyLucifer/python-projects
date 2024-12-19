dictionary = {
    "name":"Rushik",
    "age":20,
    "cast":"Hindu"
}
user = input("Enter a key : ")

if user in dictionary.keys():
    print("the key is existe in the dictionary")
else:
    print("the key is not existe in the dictionary")