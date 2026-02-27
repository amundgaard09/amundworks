
import math
import os
from sympy import sympify, symbols, lambdify

def execute(userinput: str) -> str:
    userinput = userinput.strip().split(" ")
    match userinput[0]:
        case "sqrt":
            try:
                num = float(userinput[1])
                return str(math.sqrt(num))
            except (ValueError, IndexError):
                return "Invalid input for sqrt. Please provide a valid number."
        case "cbrt":
            try:
                num = float(userinput[1])
                return str(num ** (1/3))
            except (ValueError, IndexError):
                return "Invalid input for cbrt. Please provide a valid number."
        case "log":
            try:
                num = float(userinput[1])
                base = float(userinput[2]) if len(userinput) > 2 else 10
                return str(math.log(num, base))
            except (ValueError, IndexError):
                return "Invalid input for log. Please provide a valid number and optional base."
        case "ln":
            try:
                num = float(userinput[1])
                return str(math.log(num))
            except (ValueError, IndexError):
                return "Invalid input for ln. Please provide a valid number."
        case "sin":
            try:
                angle = float(userinput[1])
                return str(math.sin(math.radians(angle)))
            except (ValueError, IndexError):
                return "Invalid input for sin. Please provide a valid angle in degrees."
        case "cos":
            try:
                angle = float(userinput[1])
                return str(math.cos(math.radians(angle)))
            except (ValueError, IndexError):
                return "Invalid input for cos. Please provide a valid angle in degrees."
        case "tan":
            try:
                angle = float(userinput[1])
                return str(math.tan(math.radians(angle)))
            except (ValueError, IndexError):
                return "Invalid input for tan. Please provide a valid angle in degrees."
        case "sum" | "add":
            try:
                numbers = list(map(float, userinput[1:]))
                return str(sum(numbers))
            except ValueError:
                return "Invalid input for sum/add. Please provide valid numbers."
        case "standardform" | "sf":
            try:
                num = float(userinput[1])
                if num == 0:
                    return "0"
                exponent = int(math.floor(math.log10(abs(num))))
                mantissa = num / (10 ** exponent)
                return f"{mantissa} x 10^{exponent}"
            except (ValueError, IndexError):
                return "Invalid input for standardform. Please provide a valid number."
        case "rstandardform" | "evalsf":
            try:
                expr = userinput[1] 
                if "x10^" not in expr:
                    return "Invalid input format. Example: 3x10^5"
        
                multiple_str, exponent_str = expr.split("x10^")
                multiple = float(multiple_str.strip())
                exponent = int(exponent_str.strip())
                result = multiple * (10 ** exponent)
                return str(result)
    
            except (ValueError, IndexError):
                return "Invalid input for evalsf. Please provide a valid standard form expression like 3x10^5."
        case "hm" | "halveringsmetode" | "bisection" | "binarysearch":
            try:
                usedvariable = userinput[1].lower().strip()
                vrbl = symbols(usedvariable)
                
                function = userinput[2].lower().strip()
                function = sympify(function)
                f = lambdify(vrbl, function, modules=['math'])
                
                start = float(userinput[3])
                end = float(userinput[4])
                precision = float(userinput[5]) if len(userinput) > 5 else 0.0001
                
                if start * end > 0:
                    return "f(start) and f(end) must have opposite signs."
                if precision <= 0:
                    return "Precision must be a positive number."
                if f(start) * f(end) > 0:
                    return "f(start) and f(end) must have opposite signs."
                
                m = (start + end) / 2
                
                while (end - start) > precision:
                    if f(m) == 0:
                        return str(m)
                    elif f(start) * f(m) < 0:
                        end = m
                    else:
                        start = m
                    m = (start + end) / 2
                return str(m)
            except (ValueError, IndexError):
                return "Invalid input for Binary Search. Please provide valid start, end, and optional precision."
        case "primefactorize" | "pf":
            try:
                num = int(userinput[1])
                if num <= 1:
                    return "Number must be greater than 1 for prime factorization."
                factors = []
                divisor = 2
                while num > 1:
                    while num % divisor == 0:
                        factors.append(divisor)
                        num //= divisor
                    divisor += 1
                return " * ".join(map(str, factors))
            except (ValueError, IndexError):
                return "Invalid input for Prime Factorization. Please provide a valid integer greater than 1."
        case "divfinder" | "divs" | "df" :
            try: 
                num = int(userinput[1])
                if num <= 0:
                    return "Number must be a positive integer."
                divisors = [i for i in range(1, num + 1) if num % i == 0]
                return (", ".join(map(str, divisors)), len(divisors))
            except (ValueError, IndexError):
                return "Invalid input for divfinder. Please provide a valid positive integer."
        case "nk" | "binomial":
            try:
                n = int(userinput[1])
                k = int(userinput[2])
                
                if k > n or n < 0 or k < 0:
                    return "Invalid values for n and k. Ensure that 0 <= k <= n."
                def factorial(x):
                    return 1 if x == 0 else x * factorial(x - 1)
                result = factorial(n) / (factorial(k) * factorial(n - k))
                return str(result)
            except (ValueError, IndexError):
                return "Invalid input for nk. Please provide valid integers n and k in the format n,k."
        case "howto":
            return (
                "Available commands:\n"
                "sqrt [number] - Calculate square root\n"
                "cbrt [number] - Calculate cube root\n"
                "log [number] [base=10] - Calculate logarithm\n"
                "ln [number] - Calculate natural logarithm\n"
                "sin [angle in degrees] - Calculate sine\n"
                "cos [angle in degrees] - Calculate cosine\n"
                "tan [angle in degrees] - Calculate tangent\n"
                "sum/add [numbers...] - Sum multiple numbers\n"
                "standardform/sf [number] - Convert to standard form\n"
                "rstandardform/evalsf [expression] - Evaluate standard form expression\n"
                "hm [variable] [function] [start] [end] [precision=0.0001] - Binary Search for root finding\n"
                "primefactorize/pf [integer > 1] - Prime factorization\n"
                "divfinder/df [positive integer] - Find divisors and count\n"
                "nk [n] [k] - Calculate binomial coefficient\n"
                "howto - Show this help message\n"
                "exit - Exit the program"
            )
        case "exit":
            exit()

while True:
    print(execute(str(input(">>>"))))
    