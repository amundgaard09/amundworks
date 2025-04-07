
import random
points = 0
while True:
    try:
        y = int(input("max num: "))
        if y < 0:
            print("invalid number")
            continue  
        if y == 0:
            print("goodbye")
            break    
    except ValueError:
        print("invalid input")
        continue
    realnum = random.randint(1, y)
    while True: 
        try:
            guessnum = int(input("guess:"))
            if guessnum <= 0 or guessnum > y:
                print("invalid number")
                continue      
        except ValueError:
            print("invalid input")
            continue
        if guessnum == realnum:
            print("correct!")
            points += 100
            print("points:", points)
            break  
        elif guessnum < realnum:
            print("too low")    
            points -= 5  
        elif guessnum > realnum:
            print("too high")
            points -= 5  
        print("points:", points)  
