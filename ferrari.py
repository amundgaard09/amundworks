
import cmath
import numpy as np

#def cubic equation
def solve_cubic(a, b, c, d):
    coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    return roots
#def quartic function
def solve_quartic(a, b, c, d, e):
    #filter
    if a == 0:
        print("not a quartic, use cardanos")
        return []
    
    #pqr computer
    p = (8 * a * c - 3 * b**2) / (8 * a**2)
    q = (b**3 - 4 * a * b * c + 8 * a**2 * d) / (8 * a**3)
    r = (-3 * b**4 + 256 * a**3 * e - 64 * a**2 * b * d + 16 * a * b**2 * c) / (256 * a**4)
    
    #roots
    z_roots = solve_cubic(1, p/2, r, -q**2/8)
    solutions = []
    
    for z in z_roots:
        R = cmath.sqrt(z + p/2)
        if R == 0:
            continue
            
        D1 = cmath.sqrt(-z + p/2 + q/(2*R))
        D2 = cmath.sqrt(-z + p/2 - q/(2*R))
        
        for R_sign in [1, -1]:  
            for D in [D1, -D1, D2, -D2]: 
                x = -b / (4 * a) + R_sign * R + D
                solutions.append(x)
    
    return solutions
#main
while True:
    #input module
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = float(input("d: "))
    e = float(input("e: "))
    #solutions
    solutions = solve_quartic(a, b, c, d, e)
    #filter
    real_solutions = [x for x in solutions if x.imag == 0]
    unique_solutions = list(set(solutions))
    #printer
    print("all solutions: ", solutions)
    print("real solutions: ", real_solutions)
    print("non-duplicated solutions: ", unique_solutions)