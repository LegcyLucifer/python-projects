def inRange(num,start,end):
    if num >= start and num <= end:
        return True
    else:
        return False

start = 4
end = 14
num = 7
print(inRange(num,start,end))