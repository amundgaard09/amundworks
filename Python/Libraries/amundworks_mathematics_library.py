'''amundworks mathematics library'''
# copyright (c) 2025 AmundWorks

import math
import questionary

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
    print(" - /"*30,"-")
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
    print(" - /"*30,"-")
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
def formelark():
    kostnad = float(input("kostnad:"))
    frakt = float(input("frakt:"))
    tollsats = float(input("tollsats %:"))
    mvaprosent = float(input("mva %:"))
    fortolling_gebyr = float(input("fortollingsgebyr:"))
    beregningsgrunnlag_toll = kostnad + frakt
    toll = beregningsgrunnlag_toll * tollsats/100
    mvagrunnlag = beregningsgrunnlag_toll + toll
    mva = mvagrunnlag * mvaprosent/100
    totalpris = mvagrunnlag + mva + fortolling_gebyr
    answer = totalpris
    print(answer)     

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
    for _ in range(0, (n - 2)):
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

def solve_quadratic():
    'quadratic equation solver'
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
def ctaa():
    '''triangle analysis module'''
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
def calculate():
    ''''calculator module'''
    action = questionary.select(
        "Choose an action:",
        choices=[ 
            "addition",
            "subtraction",
            "multiplication",
            "division",
            "exponentiation",
            "square root",
            "factorial",
            "trigonometry",
        ]
    ).ask()
    if action == "addition":
        num1 = float(input("first number:"))
        num2 = float(input("second number:"))
        answer = num1 + num2
        print(f"answer: {answer}")
    elif action == "subtraction":
        num1 = float(input("first number:"))
        num2 = float(input("second number:"))
        answer = num1 - num2
        print(f"answer: {answer}")
    elif action == "multiplication":
        num1 = float(input("factor:"))
        num2 = float(input("factor:"))
        answer = num1 * num2
        print(f"answer: {answer}")
    elif action == "division":
        num1 = float(input("dividend"))
        num2 = float(input("divisor:"))
        if num2 == 0:
            print("division by zero is not allowed")
            return
        answer = num1 / num2
        print(f"answer: {answer}")
    elif action == "exponentiation":
        num1 = float(input("base:"))
        num2 = float(input("exponent:"))
        answer = num1 ** num2
        print(f"answer: {answer}")
    elif action == "square root":
        num1 = float(input("number:"))
        if num1 < 0:
            print("negative numbers not allowed")
            return
        answer = math.sqrt(num1)
        print(f"answer: {answer}")
    elif action == "factorial":
        num1 = int(input("number:"))
        if num1 < 0:
            print("negative numbers not allowed")
            return
        answer = math.factorial(num1)
        print(f"answer: {answer}")
    elif action == "trigonometry":
        action = questionary.select(
        "Choose an action:",
        choices=[ 
            "sine",
            "cosine",
            "tangent",
            "cotangent",
            "secant",
            "cosecant",
            ]
        ).ask()
        if action == "sine":
            angle = float(input("angle:"))
            answer = math.sin(math.radians(angle))
            print(f"answer: {answer}")
        elif action == "cosine":
            angle = float(input("angle:"))
            answer = math.cos(math.radians(angle))
            print(f"answer: {answer}")
        elif action == "tangent":
            angle = float(input("angle:"))
            answer = math.tan(math.radians(angle))
            print(f"answer: {answer}")
        elif action == "cotangent":
            angle = float(input("angle:"))
            answer = 1 / math.tan(math.radians(angle))
            print(f"answer: {answer}")
        elif action == "secant":
            angle = float(input("angle:"))
            answer = 1 / math.cos(math.radians(angle))
            print(f"answer: {answer}")
        elif action == "cosecant":
            angle = float(input("angle:"))
            answer = 1 / math.sin(math.radians(angle))
            print(f"answer: {answer}")

def matrixmultiplication(A, B):
    """Multiplies two matrices A and B."""

    if len(A[0]) != len(B):
        raise ValueError("Incompatible dimensions for matrix multiplication.")
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result
def vectorrotation3d(V,x,y,z):
    """Rotates a 3D vector V by angles x, y, and z around the x, y, and z axes respectively."""
    
    import math
    
    rotx = math.radians(x)
    roty = math.radians(y)
    rotz = math.radians(z)
    
    Rx = [[1, 0, 0],
          [0, math.cos(rotx), -math.sin(rotx)],
          [0, math.sin(rotx), math.cos(rotx)]]
    
    Ry = [[math.cos(roty), 0, math.sin(roty)],
          [0, 1, 0],
          [-math.sin(roty), 0, math.cos(roty)]]
    
    Rz = [[math.cos(rotz), -math.sin(rotz), 0],
          [math.sin(rotz), math.cos(rotz), 0],
          [0, 0, 1]]
    
    R = matrixmultiplication(Rz, matrixmultiplication(Ry, Rx))
    rotated_vector = matrixmultiplication(R, [[V[0]], [V[1]], [V[2]]])
    
    return [rotated_vector[0][0], rotated_vector[1][0], rotated_vector[2][0]]

def lovelaces_algorithm(a: float, b: float, c: float, d: float, e: float, f: float) -> tuple:
    '''Lovelace's algorithm for solving systems of linear equations'''
    D = a*e - b*d
    Dx = c*e - b*f
    Dy = a*f - c*d
    if D == 0:
        raise ValueError("The system has no unique solution.")
    x = Dx / D
    y = Dy / D
    return x, y
