# fibbonaccie series :

# limit  :: 5 
# 0 1  1  2  3

limit = int(input("Enter your limit : "))

f = 0 
s = 1 
print(f"{f} {s}",end=" ")

for i in range(1,limit+1):
    ans = f + s
    print(ans,end=" ")
    f,s = s,ans