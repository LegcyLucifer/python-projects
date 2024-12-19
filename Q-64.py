def palindrome(n):
    return n[::-1] == n

name = input("Enter a name : ")
print(palindrome(name))        