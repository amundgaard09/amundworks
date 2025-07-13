"""The TOOLSTEEL Module is the steel of which your creations are forged. Here lies the FUTUREFORGE functions and formulas that helps you innovate."""

### - - - - MISCELLANEOUS - - - - ###

def prefixer(value: int, unit: str) -> str:
    return

LOGO = """
          _____                    _____                _____                    _____                    _____                    _____                    _____                   _______                   _____                    _____                    _____          
         /\    \                  /\    \              /\    \                  /\    \                  /\    \                  /\    \                  /\    \                 /::\    \                 /\    \                  /\    \                  /\    \         
        /::\    \                /::\____\            /::\    \                /::\____\                /::\    \                /::\    \                /::\    \               /::::\    \               /::\    \                /::\    \                /::\    \        
       /::::\    \              /:::/    /            \:::\    \              /:::/    /               /::::\    \              /::::\    \              /::::\    \             /::::::\    \             /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /:::/    /              \:::\    \            /:::/    /               /::::::\    \            /::::::\    \            /::::::\    \           /::::::::\    \           /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/    /                \:::\    \          /:::/    /               /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \         /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/    /                  \:::\    \        /:::/    /               /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \       /:::/__\:::\    \        /:::/  \:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \      /:::/    /                   /::::\    \      /:::/    /               /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \     /::::\   \:::\    \      /:::/    \:::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \    /:::/    /      _____        /::::::\    \    /:::/    /      _____    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\   /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\    \  /:::/____/      /\    \      /:::/\:::\    \  /:::/____/      /\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \ |:::|    |     |:::|    | /:::/\:::\   \:::\____\  /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \ 
/:::/  \:::\   \:::\____\|:::|    /      /::\____\    /:::/  \:::\____\|:::|    /      /::\____\/:::/  \:::\   \:::|    |/:::/__\:::\   \:::\____\/:::/  \:::\   \:::\____\|:::|____|     |:::|    |/:::/  \:::\   \:::|    |/:::/____/  ___\:::|    |/:::/__\:::\   \:::\____\
\::/    \:::\   \::/    /|:::|____\     /:::/    /   /:::/    \::/    /|:::|____\     /:::/    /\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /\::/    \:::\   \::/    / \:::\    \   /:::/    / \::/   |::::\  /:::|____|\:::\    \ /\  /:::|____|\:::\   \:::\   \::/    /
 \/____/ \:::\   \/____/  \:::\    \   /:::/    /   /:::/    / \/____/  \:::\    \   /:::/    /  \/____|:::::\/:::/    /  \:::\   \:::\   \/____/  \/____/ \:::\   \/____/   \:::\    \ /:::/    /   \/____|:::::\/:::/    /  \:::\    /::\ \::/    /  \:::\   \:::\   \/____/ 
          \:::\    \       \:::\    \ /:::/    /   /:::/    /            \:::\    \ /:::/    /         |:::::::::/    /    \:::\   \:::\    \               \:::\    \        \:::\    /:::/    /          |:::::::::/    /    \:::\   \:::\ \/____/    \:::\   \:::\    \     
           \:::\____\       \:::\    /:::/    /   /:::/    /              \:::\    /:::/    /          |::|\::::/    /      \:::\   \:::\____\               \:::\____\        \:::\__/:::/    /           |::|\::::/    /      \:::\   \:::\____\       \:::\   \:::\____\    
            \::/    /        \:::\__/:::/    /    \::/    /                \:::\__/:::/    /           |::| \::/____/        \:::\   \::/    /                \::/    /         \::::::::/    /            |::| \::/____/        \:::\  /:::/    /        \:::\   \::/    /    
             \/____/          \::::::::/    /      \/____/                  \::::::::/    /            |::|  ~|               \:::\   \/____/                  \/____/           \::::::/    /             |::|  ~|               \:::\/:::/    /          \:::\   \/____/     
                               \::::::/    /                                 \::::::/    /             |::|   |                \:::\    \                                         \::::/    /              |::|   |                \::::::/    /            \:::\    \         
                                \::::/    /                                   \::::/    /              \::|   |                 \:::\____\                                         \::/____/               \::|   |                 \::::/    /              \:::\____\        
                                 \::/____/                                     \::/____/                \:|   |                  \::/    /                                          ~~                      \:|   |                  \::/____/                \::/    /        
                                  ~~                                            ~~                       \|___|                   \/____/                                                                    \|___|                                            \/____/         
                                                                                                                                                                                                                                                                               
"""

### - - - - CUSTOM ERRORS - - - - ###

class MissingColorsError(Exception):
    pass
class WrongColorError(Exception):
    pass

### - - - - ELECTRICAL SEGMENT - - - - ###

def coloredresistor(c1: str, c2: str, c3: str, c4: str):
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
    return f"    <------------------------->\n    |                         |\n    |  ┌────┬────┬────┬────┐  |\n   ----│{color_block(c1)}│{color_block(c2)}│{color_block(c3)}│{color_block(c4)}│----\n    |  └────┴────┴────┴────┘  |\n    |                         |\n    <------------------------->"     
def resistorspec(band1: str, band2: str, multiplier: str, tolerance: str) -> tuple:
    """Takes in 4 colors of a resistor and returns the resistivity and tolerance range, as well as printing an ASCII representation of the resistor with colors."""
    
    if None in (band1, band2, multiplier, tolerance):
        raise MissingColorsError
    
    BAND = {
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
    MULTIPLIER = {
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
    TOLERANCE = {
        "brown":  1,
        "red":    2,
        "green":  0.5,
        "blue":   0.25,
        "violet": 0.1,
        "gray":   0.05,
        "gold":   5,
        "silver": 10,
    }

    band1int = BAND.get(band1)
    band2int = BAND.get(band2)
    multiplierint = MULTIPLIER.get(multiplier)
    tolerance_percent = TOLERANCE.get(tolerance)

    if None in (band1int, band2int, multiplierint, tolerance_percent):
        print("One or more colors are invalid.")
        raise WrongColorError

    resistance = (band1int * 10 + band2int) * multiplierint
    tolerance_decimal = tolerance_percent / 100

    low = resistance * (1 - tolerance_decimal)
    high = resistance * (1 + tolerance_decimal)

    resistancestr = f"Resistance: {resistance}Ω"
    rangestr = f"Range: {low}Ω - {high}Ω ( {tolerance_percent}% )"

    return (resistancestr, rangestr, coloredresistor(band1, band2, multiplier, tolerance))
    