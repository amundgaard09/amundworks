"""The TOOLSTEEL Module is the steel of which your creations are forged. Here lies the FUTUREFORGE functions and formulas that helps you innovate."""

from typing import Literal

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

def resistorspec(colorlist: list, colorint: int, 
                 color2value: bool = True, wantedvalue: int = None) -> tuple:
    """Takes in 4/5 colors of a resistor and returns the resistivity and tolerance range, as well as printing an ASCII representation of the resistor with colors."""
    
    if color2value: # normal function (colors to ohm value)
        if len(colorlist) != colorint:
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
    
        band1int = BAND.get(colorlist[0])
        band2int = BAND.get(colorlist[1]) 

        if colorint == 5:
            band3int = BAND.get(colorlist[2])
            multiplierint = MULTIPLIER.get(colorlist[3])
            tolerance_percent = TOLERANCE.get(colorlist[4])

        elif colorint == 4:
            band3int = None
            multiplierint = MULTIPLIER.get(colorlist[2])
            tolerance_percent = TOLERANCE.get(colorlist[3])
    
        else:
            raise MissingColorsError

        if None in (band1int, band2int, multiplierint, tolerance_percent) or (None in (band1int, band2int, band3int, multiplierint, tolerance_percent) and colorint == 5):
            print("One or more colors are invalid.")
            raise WrongColorError

        resistance = (band1int * 10 + band2int) * multiplierint
        tolerance_decimal = tolerance_percent / 100

        low = resistance * (1 - tolerance_decimal)
        high = resistance * (1 + tolerance_decimal)

        resistancestr = f"Resistance: {resistance}Ω"
        rangestr = f"Range: {low}Ω - {high}Ω ( {tolerance_percent}% )"

        return (resistancestr, rangestr)
    else: # ohm value to colors
        pass # Future expansion placeholder for now
def total_esr(caps: list[tuple], connectiontype: Literal["parallel", "series"]) -> float:
    if connectiontype == "series":
        return sum(cap[2] for cap in caps)
    elif connectiontype == "parallel":
        try:
            return 1 / sum(1 / cap[2] for cap in caps if cap[2] != 0)
        except ZeroDivisionError:
            return 0  
    else:
        raise ValueError("Connection type must be 'parallel' or 'series'")
def totalcapacitance(caps: list[tuple], connectiontype: Literal["parallel", "series"]) -> tuple: ### caps (capacitance, voltage, esr) (for now)
    if connectiontype == "parallel":
        totalcap = 0
        for i in range(len(caps)):
            totalcap += caps[i][0]
            voltlimit = min([cap[1] for cap in caps])
    else: # series connection
        rawtotalcap = 0
        for i in range(len(caps)):
            rawtotalcap += ((caps[i][0])**(-1))
        totalcap = rawtotalcap**(-1)
        voltlimit = sum([cap[1] for cap in caps])     
    return (totalcap, voltlimit, total_esr(caps, connectiontype))