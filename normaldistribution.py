

import random

thrownum = int(input("How many throws?: "))
dicenum = int(input("How many dice per throw?: "))

min_sum = dicenum * 1
max_sum = dicenum * 6

rows = [[] for _ in range(min_sum, max_sum + 1)]

for _ in range(thrownum):
    dicesum = sum(random.randint(1, 6) for _ in range(dicenum))
    rows[dicesum - min_sum].append(dicesum)

for idx, row in enumerate(rows, start=min_sum):
    print(f"{idx}:","'" * sum(row))
  