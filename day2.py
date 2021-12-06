#values from AoC need to be in the same directory, here called "posvals.txt"

data = list()
with open("posvals.txt", "r") as file:
    for line in file.readlines():
        data.append(line.rstrip())
    # data.append(int(line.rstrip()))

# print(data)

#del ett

xpos = 0
ypos = 0
for positionvalue in data:
    direction,value = positionvalue.split(" ")
    if direction == "forward":
        xpos += int(value)
    if direction == "down":
        ypos += int(value)
    if direction == "up":
        ypos -= int(value)
'''split to get rid of direction in string form which is used to determine which direction the value is applied in'''
xpos *= ypos

print(xpos)

#del två

xpos = 0
ypos = 0
aim = 0
for positionvalue in data:
    direction, value = positionvalue.split(" ")
    if direction == "forward":
        xpos += int(value)
    ypos += int(value) * aim

    if direction == "down":
        aim += int(value)

    if direction == "up":
        aim -= int(value)

xpos *= ypos

print(xpos)
# print(aim)



