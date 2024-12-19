# swap with temp variable

a = 10
temp = 0
b = 20

temp = a
a = b
b = temp

print(f"a : {a}")
print(f"b : {b}")

# swap without any variable

c = 100
d = 200

c,d = d,c

print(f"c : {c}")
print(f"d : {d}")