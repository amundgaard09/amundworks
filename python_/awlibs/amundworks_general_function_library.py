'''amundworks general function library'''
# copyright (c) 2025 AmundWorks

import random

def randstr():
    strlength = int(input("string length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&()_+-=[]{|};:\<>?/~"
    rand_str = ''.join(random.choice(chars) for _ in range(strlength))
    if strlength < 1:    
        print("string length must be greater than 0")
        return
    print("Random string:", rand_str)
    return rand_str
def dices():
    x = []
    try:
        y = int(input("nr of dices (int): ")) 
        if y <= 0:
            print("invalid number")
            dices()     
    except ValueError:
        print("invalid input")
        dices()
    for i in range(0,y):
        addx = random.randint(1,6)
        x.append(addx)
        sumx = sum(x)
        avgx = sumx/y
    print(x)
    print(f"sum of dices:{sumx}")
    print(f"avg of dices:{avgx}")

def writefile(filepath: str, content: str, makenewfile: bool | None = None) -> bool:
    """Write content to a file."""
    import os
    if makenewfile:
        with open(filepath, 'x') as f:
            f.write(content)
            return True
    elif makenewfile is None or not makenewfile:
        if os.path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write(content)
                return True
        else:
            return FileNotFoundError(f"File {filepath} does not exist.")











