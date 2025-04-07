
x = []
y = int(input("savespace:"))
savenum = 0

for i in range(0,y):

    savenum += 1
    addx = str(input(f"save nr.{savenum}:"))
    x.append(addx)

print(x)
    