#importer
import random
#while loop
while True:
    #empty list definer
    x = []
    #failsafe
    try:
        y = int(input("nr of dices (int): ")) 
        if y <= 0:
            print("invalid number")
            continue      
    except ValueError:
        print("invalid input")
        continue
    #dice roller
    for i in range(0,y):
        addx = random.randint(1,6)
        x.append(addx)
        sumx = sum(x)
        avgx = sumx/y
    #printer
    print(x)
    print(f"sum of dices:{sumx}")
    print(f"avg of dices:{avgx}")