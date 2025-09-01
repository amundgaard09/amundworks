
import math
import cmath
import random


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
        case "exit":
            exit()

while True:
    print(execute(str(input(">>>"))))