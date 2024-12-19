def copy(a):
    v1 = ""
    f1 = open(a,"r")

    for i in f1:
        v1+=i
    return v1
a = "Q-68.txt"
f2 = open("Q-82.txt","w")
f2.write(copy(a))
print("Copy to another file is succesfully")