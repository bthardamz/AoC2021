#values from AoC need to be in the same directory, here called "windows.txt"

data = list()
with open("windows.txt", "r") as file:
    for line in file.readlines():
        data.append(int(line.rstrip()))

tempvalue = 100000
bigger = 0
for shortsweep in data:
    if tempvalue < shortsweep:
        bigger +=1
    tempvalue = shortsweep

print(bigger)

prevvalue = 1000000
bigger = 0
for sweep in range(len(data)-2):
    l = data[sweep]
    m = data[sweep+1]
    r = data[sweep+2]
    total = l+m+r
    if prevvalue < total:
        bigger +=1
    prevvalue = total

print(bigger)
