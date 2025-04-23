

import random

rows = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

while True:
    try:
        thrownum = int(input("\nHow many throws?: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    for i in range(thrownum):
        dicethrow1 = random.randint(1,6)
        dicethrow2 = random.randint(1,6)
        dicesum = dicethrow1 + dicethrow2
        rows[dicesum-2].append(dicesum)

    for row in rows:
        print(row)
    print("\n--------------------\n")
    
    counter = 2
    for row in rows:
        list = len(row)
        listprcnt = (list / thrownum) * 100   
        print(f"row{counter}:{listprcnt}%")
        counter += 1
