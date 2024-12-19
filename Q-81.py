def write(a,b):
    f = open(a,"w")
    for i in b:
        f.write(f"{i}\n")
    print("succesfully written the list in text file")
    
a = "Q-81.txt"
b = ["Rushik","Mital","Harsh","Ghanshyam","Roshni"]

write(a,b)
