

import random

def randstr():
    strlength = int(input("string length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&()_+-=[]{}|;:\<>?/~"
    rand_str = ''.join(random.choice(chars) for _ in range(strlength))
    if strlength < 1:    
        print("string length must be greater than 0")
        return
    print("Random string:", rand_str)
    return rand_str
randstr()