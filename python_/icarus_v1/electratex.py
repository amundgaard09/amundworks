"""Electratex is a module for basic information gathering regarding electronic components. It serves as a electrical engineering assistant with the capacity to become a universal engineering assistant.\n
   (C) AmundWorks"""

class MissingColorsError(Exception):
    pass
class WrongColorError(Exception):
    pass

def printresistor(c1, c2, c3, c4):
    """Prints a visual representation of a resistor with the color code"""
    ansi_colors = {
        "black":  "\033[40m",
        "brown":  "\033[48;5;94m",
        "red":    "\033[41m",
        "orange": "\033[48;5;208m",
        "yellow": "\033[43m",
        "green":  "\033[42m",
        "blue":   "\033[44m",
        "violet": "\033[48;5;93m",
        "gray":   "\033[100m",
        "white":  "\033[47m",
        "gold":   "\033[48;5;178m",
        "silver": "\033[48;5;7m",
    }  
    def color_block(color):
        ansi = ansi_colors.get(color.lower(), "\033[0m")
        reset = "\033[0m"
        return f"{ansi}    {reset}" 

    print(f"    <------------------------->\n    |                         |\n    |  ┌────┬────┬────┬────┐  |\n   ----│{color_block(c1)}│{color_block(c2)}│{color_block(c3)}│{color_block(c4)}│----\n    |  └────┴────┴────┴────┘  |\n    |                         |\n    <------------------------->")      
def resistancecalc(band1: str, band2: str, multi: str, toler: str) -> str | Exception:
    """Takes in 4 colors of a resistor and returns the resistivity and tolerance range"""
    if None in (band1, band2, multi, toler):
        return MissingColorsError
    
    band = {
        "black":  0,
        "brown":  1,
        "red":    2,
        "orange": 3,
        "yellow": 4,
        "green":  5,
        "blue":   6,
        "violet": 7,
        "gray":   8,
        "white":  9,
    }
    multiplier = {
        "black":  1,
        "brown":  10,
        "red":    100,
        "orange": 1000,
        "yellow": 10000,
        "green":  100000,
        "blue":   1000000,
        "violet": 10000000,
        "gray":   100000000,
        "white":  1000000000,
        "gold":   0.1,
        "silver": 0.01,
    }
    tolerance = {
        "brown":  1,
        "red":    2,
        "green":  0.5,
        "blue":   0.25,
        "violet": 0.1,
        "gray":   0.05,
        "gold":   5,
        "silver": 10,
    }
     
    band1int = band.get(band1)
    band2int = band.get(band2)
    multiplierint = multiplier.get(multi)
    tolerance_percent = tolerance.get(toler)

    if None in (band1int, band2int, multiplierint, tolerance_percent):
        print("One or more colors are invalid.")
        return WrongColorError

    resistance = (band1int * 10 + band2int) * multiplierint
    tolerance_decimal = tolerance_percent / 100

    low = resistance * (1 - tolerance_decimal)
    high = resistance * (1 + tolerance_decimal)

    print(f"Resistance: {resistance}Ω")
    print(f"Range: {low}Ω - {high}Ω ( {tolerance_percent}% )")
    printresistor(band1, band2, multi, toler)

# voltage = resistance * amperage
# amperage = voltage / resistance
# resistance = voltage / amperage

def voltcalc(amp: float, res: float) -> float:
    return amp * res
def ampcalc(volt: float, res: float) -> float:
    return volt / res
def rescalc(volt: float, amp: float) -> float:
    return volt / amp
