# Amundworks General Function Library | copyright (c) 2025 AmundWorks

import questionary
import random
import math

def serielån():
    lånbeløp = float(input("lånbeløp:"))
    etableringsgebyr = float(input("etableringsgebyr:"))
    termingebyr = float(input("termingebyr:"))
    rente = float(input("rente %:"))
    antallterminer = int(input("antall terminer:"))
    terminbeløp = lånbeløp/antallterminer
    totalkostnad = etableringsgebyr
    restbeløp = lånbeløp
    totalrente = 0
    print(" - /"*40,"-")
    for i in range(antallterminer):
        terminbeløpetterrente = terminbeløp + restbeløp * (rente/100) + termingebyr
        totalkostnad += terminbeløpetterrente
        restbeløp -= terminbeløp
        totalgebyr = termingebyr * antallterminer
        terminrente = restbeløp * (rente/100)
        totalrente += terminrente
        print(f"termin {i+1}: |restbeløp:{restbeløp:.2f}|avdrag:{terminbeløp:.2f}|termingebyr:{termingebyr}|rente:{terminrente:.2f}|terminbeløp:{terminbeløpetterrente:.2f}")
    print("--------------------------------------------------")
    print(f"total kostnad: {totalkostnad:.2f}") 
    print(f"total gebyr: {totalgebyr:.2f}")
    print(f"total rente: {totalrente:.2f}")
    print(" - /"*40,"-")
def sparingscalc():
    innskudd = float(input("innskudd: "))
    rente = float(input("rente: "))
    år = int(input("år: "))
    telleår = 0

    for i in range(år):
        telleår += 1
        nyverdi = innskudd + innskudd * (rente / 100)
        print(f"år {telleår}: {innskudd:.2f} * {rente}% = {nyverdi:.2f}")
        innskudd = nyverdi
    print(f"totalt: {nyverdi:.2f}")   
def fibonacci():
    '''Fibonacci sequence generator'''
    action = questionary.select(
        "Choose a cipher/decoding method:",
        choices=[ 
            "list()",
            "int()",
        ]
    ).ask()
def fibonacci_list():
    '''Fibonacci sequence generator'''
    try:
        n = int(input("how many fibs:"))
        if n < 1:
            print("invalid number")
            fibonacci_list()
    except ValueError:
        print("invalid input")
        fibonacci_list()
    totalfib = [0, 1]
    fib0, fib1 = 0, 1
    for i in range(0, (n - 2)):
        newfib = fib0 + fib1
        fib0 = fib1
        fib1 = newfib
        totalfib.append(newfib)
    goldenratio = newfib / fib0
    print(totalfib)
    print(f"golden ratio:{goldenratio}")
def fibonacci_int():
    '''Fibonacci integer generator'''
    try:
        n = int(input("which fib:"))
        if n < 1:
            print("invalid number")
            fibonacci_int()
    except ValueError:
        print("invalid input")
        fibonacci_int()
    fib0, fib1 = 0, 1
    for i in range(0, (n - 2)):
        newfib = fib0 + fib1
        fib0 = fib1
        fib1 = newfib
    lastfib = newfib
    goldenratio = lastfib / fib0
    print(f"{n}th fib: {lastfib}")
    print(f"golden ratio: {goldenratio:.100f}")
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
def solve_quadratic():
    a = float(input("A-verdi:"))
    b = float(input("B-verdi:"))
    c = float(input("C-verdi:"))
    if a == 0:
        print("Dette er ikke en andregradsligning (a kan ikke være 0).")
        solve_quadratic()
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        solutions = [x1,x2]
        print(f"To løsninger: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x1 = -b / (2 * a)
        solutions = [x1]
        print(f"Én løsning: x = {x1}")
    else:
        solutions = []
        print("Ingen løsninger med ikke-imaginære tall")
    return solutions
def randstr():
    strlength = int(input("string length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&()_+-=[]{}|;:\<>?/~"
    rand_str = ''.join(random.choice(chars) for _ in range(strlength))
    if strlength < 1:    
        print("string length must be greater than 0")
        return
    print("Random string:", rand_str)
    return rand_str
def ctaa():
    known_side = input("known side:")
    side_value = float(input("side length:"))
    angle_a = float(input("angle a:"))
    angle_b = float(input("angle b:"))
    angle_c = float(input("angle c:"))
    rada = math.radians(angle_a)
    radb = math.radians(angle_b)
    radc = math.radians(angle_c)
    sina = math.sin(rada)
    sinb = math.sin(radb)
    sinc = math.sin(radc)
    cosa = math.cos(rada)
    cosb = math.cos(radb)
    cosc = math.cos(radc)
    tana = math.tan(rada)
    tanb = math.tan(radb)
    tanc = math.tan(radc)
    if known_side == 'a':
        side_a = side_value
        side_b = (side_a * sinb) / sina
        side_c = (side_a * sinc) / sina
    elif known_side == 'b':
        side_b = side_value
        side_a = (side_b * sina) / sinb
        side_c = (side_b * sinc) / sinb
    elif known_side == 'c':
        side_c = side_value
        side_a = (side_c * sina) / sinc
        side_b = (side_c * sinb) / sinc
    area = (1/2) * side_a * side_b * sinc
    print(f"sines: a:{sina}, b:{sinb}, c:{sinc}")
    print(f"cosines: a:{cosa}, b:{cosb}, c:{cosc}")
    print(f"tangents: a:{tana}, b:{tanb}, c:{tanc}")
    print(f"sides: a:{side_a}, b:{side_b}, c:{side_c}")
    print(f"area:{area}")
