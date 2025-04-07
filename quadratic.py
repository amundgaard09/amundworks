
import math

while True:
    a = float(input("A-verdi:"))
    b = float(input("B-verdi:"))
    c = float(input("C-verdi:"))

    def solve_quadratic(a,b,c):
        if a == 0:
            print("Dette er ikke en andregradsligning (a kan ikke være 0).")
            return
    
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
    
    solve_quadratic(a,b,c)
    