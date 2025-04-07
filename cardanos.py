import cmath

#input module
a = float(input("A-verdi:"))
b = float(input("B-verdi:"))
c = float(input("C-verdi:"))
d = float(input("D-verdi:"))

#def function
def solve_qubic(a,b,c,d):
    #to avoid false cubics (quadratics)
    if a == 0:
        print("Not a real cubic!")
        return 
    else:
        #computer
        deltanull = (b**2) - (3*a*c)
        deltaone = (2*(b**3)) - (9*a*b*c) + (27*a**2*d)
        omega = (-1 + cmath.sqrt(-3)) / 2 
        C = ((deltaone + cmath.sqrt(deltaone**2 - 4*deltanull**3)) / 2) ** (1/3)
        #avoids division by zero
        if C == 0:
            C = ((deltaone - cmath.sqrt(deltaone**2 - 4*deltanull**3)) / 2) ** (1/3)
        #computer
        x1 = - (1 / (3*a)) * (b + omega**0 * C + deltanull / (omega**0 * C))
        x2 = - (1 / (3*a)) * (b + omega**1 * C + deltanull / (omega**1 * C))
        x3 = - (1 / (3*a)) * (b + omega**2 * C + deltanull / (omega**2 * C))    
        #printer
        print(f"The solution to the cubic: ({a}x^3) + ({b}x^2) + ({c}x) + ({d}) is:") 
        if abs(x1.imag) < 1e-10: 
            print(f"x1 (real) = {x1.real:.6f}")
        else:
            print(f"x1 (intgr root) = {x1}")
        if abs(x2.imag) < 1e-10:  
            print(f"x2 (real) = {x2.real:.6f}")
        else:
            print(f"x2 (cmplx root) = {x2}")
        if abs(x3.imag) < 1e-10: 
            print(f"x3 (real) = {x3.real:.6f}")
        else:
            print(f"x3 (cmplx root) = {x3}")
#function
solve_qubic(a,b,c,d)
    