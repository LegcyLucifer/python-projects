str1 = "helloWorld"
print(str1)

str2 = input("Enter a string : ")

str3 = len(str1) // 2

result = str1[:str3] + str2 + str1[str3:]

print(result)