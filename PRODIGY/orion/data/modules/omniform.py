"""Utility Library for the ORION CLI - Iteration I"""

from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
from typing_extensions import Callable
from typing import Literal
import questionary
import numpy
import shlex
import math
import sys

#Electrical (extending what you have)                                        DONE

#Ohm's Law — voltage, current, resistance triangle                           DONE
#Voltage divider output voltage                                              DONE
#RC time constant                                                            DONE
#Inductor impedance at frequency                                             DONE
#Power dissipation in a resistor                                             DONE
#Decibels from voltage or power ratio                                        DONE

#Mechanics / Mechatronics                                                    DONE

#Torque from force and moment arm                                            DONE
#Gear ratio from tooth counts                                                DONE
#Angular velocity from RPM                                                   DONE
#Kinetic energy                                                              DONE
#Potential energy                                                            DONE

#General Engineering                                                         .

#Unit conversions                                                            CURRENTLY BEING IMPLEMENTED
#degrees to radians - radians to degrees                                     DONE
#RPM to rad/s                                                                DONE
#PSI to Pascal                                                               DONE
#dB to linear scale and back                                                 .
#Significant figures rounding                                                .

# Will be implemented in V2:

#Control Systems                                                             .

#PID output from error, integral, derivative terms                           .
#Natural frequency of a spring-mass system                                   .
#Damping ratio                                                               .

#Aerospace                                                                   .

#Thrust to weight ratio                                                      .
#Lift equation from air density, velocity, area, lift coefficient            .
#Drag equation — same structure as lift                                      .
#Reynolds number from velocity, length, viscosity                            .
#Tsiolkovsky rocket equation — delta-v from exhaust velocity and mass ratio  .
#Dynamic pressure from air density and velocity                              .
#Mach number from velocity and speed of sound                                .

#Engineering                                                                 .

#Moment of inertia for common shapes (cylinder, rod, disk)                   .
#Mechanical advantage of a lever                                             .
#Stress and strain from force and cross-sectional area                       .

### CONSTANTS

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
ANSI_COLORS = {
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

### ERRORS

class InvalidColorCount(Exception):
    """Raised when the color count passed into a function of the resistor group is invalid."""
    def __init__(self, Function: Callable):
        super().__init__(f"Invalid Color Count for {Function}")
class EmptyTokenList(Exception):
    """Raises when the TokenList passed into VerifyTokens() is empty."""
    def __init__(self):
        super().__init__(f"Empty TokenList! Make sure of correct tokens before verification attempt.")
class IncorrectArgumentCount(Exception):
    """Raises when the count of arguments given to a function is incorrect."""
    def __init__(self, function: Callable, GivenArgumentCount: int, WantedArgumentCount: set):
        self.function = function
        self.GivenArgumentCount = GivenArgumentCount
        self.WantedArgumentCount = WantedArgumentCount
        super().__init__(f"Incorrect count of arguments for {function}. {function} takes {self.WantedArgumentCount} but was given {self.GivenArgumentCount}")
class UnknownModule(Exception):
    """Raises when an unknown module gets caught in VerifyTokens()."""
    def __init__(self, GivenModule: str):
        super().__init__(f"Unknown Module: {GivenModule}")
class UnknownSubCommand(Exception):
    """Raises when an unknown subcommand gets caught in VerifyTokens()."""
    def __init__(self, Module: str, GivenCommand: str):
        super().__init__(f"Unknown command for {Module}: {GivenCommand}")
class MissingCommand(Exception):
    def __init__(self, module):
        super().__init__(f"Missing subcommand for {module}")    
class InvalidColors(Exception):
    def __init__(self, function: Callable, IndexOfInvalidColors: list):
        super().__init__(f"Invalid colors for {function} at indices {IndexOfInvalidColors}")
class MissingParameters(Exception):
    def __init__(self, Function: Callable, MissingParameters: list):
        super().__init__(f"Missing parameter {MissingParameters} for {Function}.")
class InconsistencyError(Exception):
    def __init__(self, Function: Callable, Inconsistency: str):
        super().__init__(Function, Inconsistency)

### SYSTEM

def Tokenize(RawCommandString: str) -> list[str]:
    """Tokenize a raw command string and return token list."""
    return shlex.split(RawCommandString)
def dispatcher(RawCommandString: str) -> str:
    Tokens = Tokenize(RawCommandString) 
    VerifyTokens(Tokens)
    ValidateArgs(Tokens)
    Module, Command, RawArgs = Tokens[0], Tokens[1], Tokens[2:]
    Args = []
    for arg in RawArgs:
        if arg == "_":
            Args.append(None)
        else:
            try:
                Args.append(float(arg))
            except ValueError:
                Args.append(arg)
            
    return COMMANDMAP[Module][Command](*Args)

### MISCELLANEOUS

def ColorText(Text: str, Color: str):
        ansi = ANSI_COLORS.get(Color.lower(), "\033[0m")
        reset = "\033[0m"
        return f"{ansi}{Text}{reset}"

### UNIPOWER

def OhmsLaw(V: float | None = None, I: float | None = None, R: float | None = None):
    """Ohms Law calculation for Voltage, Current, and Resistivity.
    V = I * R
    I = V / R
    R = V / I
    """
    for value in (V, I, R):
        if value is not None:
            value = float(value)
            
    if (V, I, R).count(None) > 1:
        MissingParams = []
        for idx, value in enumerate((V, I, R)):
            if value is None:
                MissingParams.append(("V", "I", "R")[idx])
        
        raise MissingParameters(OhmsLaw, MissingParams)
    
    if V == None:
        V = I * R
    elif I == None:
        I = V / R
    elif R == None:
        R = V / I
        
    return (f"V: {V}", f"I: {I}", f"R: {R}")
def VoltDivider(VIn: float, R1: float, R2: float) -> float:
    return VIn * (R2 / (R1 + R2))
def RCTimeConstant(Capacitance: float, Resistance: float) -> float:
    return Capacitance * Resistance
def InductorImpedance(Hertz: float, Inductance: float) -> float:
    return 2 * numpy.pi * Hertz * Inductance
def PowerDissipation(V: float | None = None, I: float | None = None, R: float | None = None) -> float:
    if (V, I, R).count(None) > 1:
        MissingParams = []
        for idx, value in enumerate((V, I, R)):
            if value is None:
                MissingParams.append(("V", "I", "R")[idx])
        
        raise MissingParameters(PowerDissipation, MissingParams)

    if (V, I, R).count(None) == 1:
        if V is None:
            P = I ** 2 * R
        elif I is None:
            P = V ** 2 / R
        elif R is None:
            P = V * I
        return P
    
    else:
        P1 = I ** 2 * R
        P2 = V ** 2 / R
        P3 = V * I
        
        if math.isclose(P1, P2):
            if math.isclose(P2, P3):
                return (P1 + P2 + P3) / 3
            else:
                raise InconsistencyError(PowerDissipation, "Inconsistency with P3 = V * I")
        else:
            if math.isclose(P1, P3):
                raise InconsistencyError(PowerDissipation, "Inconsistency with P2 = V ** 2 / R")
            else:
                raise InconsistencyError(PowerDissipation, "Inconsistency with P1 = I ** 2 * R")
    
def ResistorViz(C1: str, C2: str, C3: str, C4: str, C5: str | None = None):
    """Prints a ASCII representation of a resistor with the color code""" 
    def color_block(color: str):
        ansi = ANSI_COLORS.get(color.lower(), "\033[0m")
        reset = "\033[0m"
        return f"{ansi}    {reset}"
    if C5 is not None:
        return f"    <----------------------------->\n    |                             |\n    |  ┌────┬────┬────┬────┬────┐ |\n   ----│{color_block(C1)}│{color_block(C2)}│{color_block(C3)}│{color_block(C4)}│{color_block(C5)}|----\n    |  └────┴────┴────┴────┴────┘ |\n    |                             |\n    <----------------------------->" 
    else:
        return f"    <------------------------->\n    |                         |\n    |  ┌────┬────┬────┬────┐  |\n   ----│{color_block(C1)}│{color_block(C2)}│{color_block(C3)}│{color_block(C4)}│----\n    |  └────┴────┴────┴────┘  |\n    |                         |\n    <------------------------->" 
def ResistorInsight(C1: str, C2: str, C3: str, C4: str, C5: str | None = None) -> tuple:
    """Takes in 4/5 colors of a resistor and returns the resistivity and tolerance range."""
    
    ColorList = [C1, C2, C3, C4, C5] if C5 is not None else [C1, C2, C3, C4]
   
    band1int = BAND.get(ColorList[0])
    band2int = BAND.get(ColorList[1]) 
    band3int = None
    
    if C5 is None:
        multiplierint = MULTIPLIER.get(ColorList[2])
        tolerance_percent = TOLERANCE.get(ColorList[3])
        bands = (band1int, band2int, multiplierint, tolerance_percent)
        
        if None in bands:
            raise InvalidColors(ResistorInsight, bands.index(None) + 1)
        
        resistance = (band1int * 10 + band2int) * multiplierint
        
    else:
        band3int = BAND.get(ColorList[2])
        multiplierint = MULTIPLIER.get(ColorList[3])
        tolerance_percent = TOLERANCE.get(ColorList[4])
        bands = (band1int, band2int, band3int, multiplierint, tolerance_percent)
        
        if None in bands:
            raise InvalidColors(ResistorInsight, bands.index(None)+1)
        
        resistance = (band1int * 100 + band2int * 10 + band3int) * multiplierint

    tolerance_decimal = tolerance_percent / 100
    low = resistance * (1 - tolerance_decimal)
    high = resistance * (1 + tolerance_decimal)
    
    resistancestr = f"Resistance: {resistance}Ω"
    rangestr = f"Range: {low}Ω - {high}Ω ( {tolerance_percent}% )"

    return (resistancestr, rangestr)

def TotalESR(caps: list[tuple], connectiontype: Literal["parallel", "series"]) -> float:
    if connectiontype == "series":
        return sum(cap[2] for cap in caps)
    elif connectiontype == "parallel":
        try:
            return 1 / sum(1 / cap[2] for cap in caps if cap[2] != 0)
        except ZeroDivisionError:
            return 0  
    else:
        raise ValueError("Connection type must be 'parallel' or 'series'")
def TotalCapacitance(caps: list[tuple], connectiontype: Literal["parallel", "series"]) -> tuple: ### caps (capacitance, voltage, esr) (for now)
    if connectiontype == "parallel":
        totalcap = 0
        for cap in caps:
            totalcap += cap[0]
        voltlimit = min([cap[1] for cap in caps])
    else: # series connection
        rawtotalcap = 0
        for cap in caps:
            rawtotalcap += ((cap[0])**(-1))
        totalcap = rawtotalcap**(-1)
        voltlimit = sum([cap[1] for cap in caps])     
    return (totalcap, voltlimit, TotalESR(caps, connectiontype))

### UNIMAKE

def Torque(MomentArmDistance: float, Force: float) -> float:
    """Returns torque in newtons from moment arm distance and force."""
    return MomentArmDistance * Force
def GearRatio(DrivingGearTeethCount: int, DrivenGearTeethCount: int) -> tuple:
    """Returns the gear ratio from the driving gear's teeth count and the driven gear's teeth count."""
    Ratio = DrivenGearTeethCount / DrivingGearTeethCount
    if Ratio > 1:
        return (Ratio, ColorText("Speed-", "red"), ColorText("Torque+", "green"))
    elif Ratio < 1:
        return (Ratio, ColorText("Speed+", "green"), ColorText("Torque-", "red"))
    else:
        return (Ratio, ColorText("Unchanged Speed", "yellow"), ColorText("Unchanged Torque", "yellow"))
def AngularVelocityR(RPM: float) -> float:
    """Returns angular velocity from RPM in radians/s"""
    return RPM * numpy.pi / 30
def AngularVelocityD(RPM: float) -> float:
    """Returns angular velocity from RPM in degrees/s"""
    return R2D((RPM * numpy.pi / 30))
def KineticEnergy(Mass: float, Velocity: float) -> float:
    """Returns the kinetic energy from mass in KGs and velocity in meters/s"""
    return (0.5 * Mass * Velocity**2)
def PotentialEnergy(Mass: float, Height: float, Gravity: float | None = 9.8) -> float:
    """Returns the potential energy of a mass. Gravity is defaulted to 9.8m /s^2"""
    return Mass * Gravity * Height

def PSI2Pascal(PSI: float) -> float:
    return PSI * 6894,76
def Pascal2PSI(Pascal: float) -> float:
    return Pascal / 6894,76

### UNIMATH

### REFACTOR CTAA \/
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

def solve_quadratic(A: float, B: float, C: float) -> tuple:
    """Solves quadratic equations and returns x-values in a tuple."""
    if A == 0:
        return ValueError("Invalid quadratic equation! A cannot be 0.")
    delta = B**2 - 4*A*C
    if delta > 0:
        x1 = (-B - math.sqrt(delta)) / (2 * A)
        x2 = (-B + math.sqrt(delta)) / (2 * A)
        return (x1, x2)
    
    elif delta == 0:
        x1 = -B / (2 * A)
        return (x1)
    
    else:
        return None

def D2R(Degrees: float) -> float:
    return Degrees / 180 * math.pi
def R2D(Radians: float) -> float:
    return Radians / math.pi * 180

def SineRule(
    Sides: list[float | None],
    Angles: list[float | None],
    AngleMeasurementMode: Literal["Degrees", "Radians"]
) -> list[list[float], list[float]] | None:
    """
    Sine Rule

    Formula: A / sin(a) = B / sin(b) = C / sin(c)

    Return Format: [Angles:[A, B, C], Sides:[A, B, C]]
    """
   
    angles_rad = []
    for angle in Angles:
        if angle is not None and AngleMeasurementMode == "Degrees":
            angles_rad.append(math.radians(angle))
        else:
            angles_rad.append(angle)

    known_angle_indices = [i for i in range(3) if angles_rad[i] is not None]
    if len(known_angle_indices) == 2:
        missing = next(i for i in range(3) if angles_rad[i] is None)
        angles_rad[missing] = math.pi - sum(angles_rad[i] for i in known_angle_indices)

    ReferenceRatio = None
    for idx in range(3):
        if Sides[idx] is not None and angles_rad[idx] is not None:
            ReferenceRatio = Sides[idx] / math.sin(angles_rad[idx])
            break

    ### Return None if no reference ratio could be established, meaning there is not enough information to solve the triangle.
    if ReferenceRatio is None:
        return None

    for idx in range(3):
        if Sides[idx] is None and angles_rad[idx] is not None:
            Sides[idx] = ReferenceRatio * math.sin(angles_rad[idx])
        elif angles_rad[idx] is None and Sides[idx] is not None:
            value = Sides[idx] / ReferenceRatio
            if not -1 <= value <= 1:
                return None
            asin_val = math.asin(value)
            known_sum = sum(a for a in angles_rad if a is not None)
            
            ### Check for the ambiguous case of the sine rule, where there may be two possible angles that satisfy the equation
            if math.pi - asin_val + known_sum <= math.pi:
                angles_rad[idx] = math.pi - asin_val
            else:
                angles_rad[idx] = asin_val

    if AngleMeasurementMode == "Degrees":
        Angles_out = [math.degrees(a) if a is not None else None for a in angles_rad]
    else:
        Angles_out = angles_rad

    return [Angles_out, Sides]

def CosineRule(LengthA: float, LengthB: float, AngleA: float) -> float:
    return math.sqrt(LengthA ** 2 + LengthB ** 2 - ((2 * LengthA * LengthB) * math.cos(math.radians(AngleA))))
def ReverseCosineRule(LengthA: float, LengthB: float, LengthC: float) -> tuple[float]:
    """ 
    Returns a tuple of the three angles in degrees, in the order of AngleA, AngleB, AngleC 
    
    Formula: AngleA = arccos((B^2 + C^2 - A^2) / (2BC))
    """

    return (
        math.degrees(math.acos((LengthB ** 2 + LengthC ** 2 - LengthA ** 2) / (2 * LengthB * LengthC))),  # AngleA
        math.degrees(math.acos((LengthC ** 2 + LengthA ** 2 - LengthB ** 2) / (2 * LengthC * LengthA))),  # AngleB
        math.degrees(math.acos((LengthA ** 2 + LengthB ** 2 - LengthC ** 2) / (2 * LengthA * LengthB)))   # AngleC
    )

def SASArea(LengthA: float, LengthB: float, AngleC: float) -> float:
    return (0.5 * LengthA * LengthB * math.sin(math.radians(AngleC)))
def HeronsFormula(LengthA: float, LengthB: float, LengthC: float) -> float:
    """
    Returns the area of a triangle from the side lengths.

    Args:
        LenghtA (float):
        LenghtB (float):
        LenghtC (float):

    Returns:
        Area (float):
    """
    SemiPerimiter = (LengthA + LengthB + LengthC) / 2
    return math.sqrt(SemiPerimiter * (SemiPerimiter - LengthA) * (SemiPerimiter - LengthB) * (SemiPerimiter - LengthC))

### UNIALGO

def FibonacciList(ListLength: float) -> list[int]:
    """Fibonacci sequence generator"""
    try:
        ListLength = int(ListLength)  
    except ValueError:
        raise ValueError("FibonacciInteger does not take floats!")      
    fib0, fib1 = 0, 1
    FiboList = [fib0, fib1]
    for _ in range(0, (ListLength - 2)):
        fib2 = fib0 + fib1
        fib0, fib1 = fib1, fib2
        FiboList.append(fib2)
        
    return FiboList   
def FibonacciInteger(FiboIndex: float) -> int:
    """Fibonacci integer generator"""   
    try:
        FiboIndex = int(FiboIndex)  
    except ValueError:
        raise ValueError("FibonacciInteger does not take floats!")       
    fib0, fib1 = 0, 1
    for _ in range(0, (FiboIndex - 2)):
        fib2 = fib0 + fib1
        fib0, fib1 = fib1, fib2
        
    return fib2

def LovelacesAlgorithm(a: float, b: float, c: float, d: float, e: float, f: float) -> tuple:
    """Lovelace's algorithm for solving systems of linear equations"""
    D = a*e - b*d
    if D == 0:
        raise ValueError("The system has no unique solution.")
    
    Dx = c*e - b*f
    Dy = a*f - c*d
    x = Dx / D
    y = Dy / D
    return (x, y)

### UNICRYPT

def BinaryEncrypt(InputString: str) -> str:
    RawBinary = ''.join(format(ord(i), '08b') for i in InputString)
    OutputString = ' '.join(RawBinary[i:i+8] for i in range(0, len(RawBinary), 8))
    return OutputString
def BinaryDecrypt(InputString: str) -> str:
    OutputString = ''.join(chr(int(b, 2)) for b in InputString.split())
    return OutputString
def CeasarEncrypt(InputString: str, Shift: int) -> str:
    newtext = ""
    for character in InputString:
        if character.isalpha():               
            pos = ord(character.lower()) - 96 
            newpos = (pos + Shift - 1) % 26 + 1   
            newchar = chr(newpos + 96)        
            newtext += newchar                
        else:                                
            newtext += character 
    return newtext
def CeasarDecrypt(InputString: str, Shift: int) -> str:
    newtext = ""
    for character in InputString:
        if character.isalpha():               
            pos = ord(character.lower()) - 96
            newpos = (pos - Shift - 1) % 26 + 1   
            newchar = chr(newpos + 96)        
            newtext += newchar                
        else:                                 
            newtext += character
    return newtext 
def VigenereEncrypt(InputString: str, Key: str) -> str:
    ciphertext = ""

    for i in range(len(InputString)):
        if InputString[i].isalpha():
            if InputString[i].isupper():
                ciphertext += chr((ord(InputString[i]) - ord(Key[i % len(Key)].upper()) + 26) % 26 + ord("A"))
            else:
                ciphertext += chr((ord(InputString[i]) - ord(Key[i % len(Key)].lower()) + 26) % 26 + ord("a"))
        else:
            ciphertext += InputString[i]
    return ciphertext
def VigenereDecrypt(InputString: str, Key: str) -> str:
    plaintext = ""
    Key = Key.lower()
    key_index = 0

    for char in InputString:
        if char.isalpha():
            shift = ord(Key[key_index % len(Key)]) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char

    return plaintext
def RailfenceEncrypt(InputString: str, Key: str) -> str:
    pos = 0
    direction = 1
    rows = [[] for _ in range(Key)]

    for char in InputString:
        rows[pos].append(char)
    
        pos += direction
        if pos == 0 or pos == Key - 1:
            direction *= -1
    
    return ''.join([''.join(row) for row in rows])
def RailfenceDecrypt(InputString: str, Key: str) -> str:
    length = len(InputString)
    pattern = []
    pos = 0
    direction = 1
    for _ in range(length):
        pattern.append(pos)
        pos += direction
        if pos == 0 or pos == Key - 1:
            direction *= -1

    counts = [pattern.count(r) for r in range(Key)]
    rows = []
    index = 0
    for c in counts:
        rows.append(list(InputString[index:index + c]))
        index += c

    plaintext = ''
    row_pointers = [0] * Key
    for r in pattern:
        plaintext += rows[r][row_pointers[r]]
        row_pointers[r] += 1

    return plaintext
def OTPEncrypt(InputString: str, KeyString: str) -> str:
    bitext = ''.join(format(ord(i), '08b') for i in InputString)
    bikey = ''.join(format(ord(i), '08b') for i in KeyString)
    cipher = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bitext, bikey))
    return ' '.join(cipher[i:i+8] for i in range(0, len(cipher), 8))
def OTPDecrypt(InputString: str, KeyString: str) -> str:
    bikey = ''.join(format(ord(i), '08b') for i in KeyString)
    plaintext_bits = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(InputString, bikey))
    return ''.join(chr(int(plaintext_bits[i:i+8], 2)) for i in range(0, len(plaintext_bits), 8))
    
### MAPS

ARGUMENTMAP: dict[str, set] = {
    "unipower": {
        "ohmslaw": {3},
        "voltdivider": {3},
        "rctimeconstant": {2},
        "inductorimpedance": {2},
        "powerdissipation": {3},
        "resistorsinsight": {4, 5},
        "resistorviz": {4, 5},
        "capacitance": {2},
        "esr": {2},
    },
    "unimake": {
        "torque": {2},
        "gearratio": {2},
        "angularvelocityr": {1},
        "angularvelocityd": {1},
        "kineticenergy": {2},
        "potentialenergy": {3},
    },
    "unimath": {
        "D2R": {1},
        "R2D": {1},
        "sinerule": {7},
        "cosinerule": {3},
        "reversecosinerule": {3},
        "sasarea": {3},
        "herons": {3}
    },
    "unialgo": {
        "fibonaccilist": {1},
        "fibonacciinteger": {1},
        "lovelacesalgorithm": {6},
    },
    "unicrypt": {
        "binaryencrypt": {1},
        "binarydecrypt": {1},
        "ceasarencrypt": {2},
        "ceasardecrypt": {2},
        "vigenereencrypt": {2},
        "vigeneredecrypt": {2},
        "railfenceencrypt": {2},
        "railfencedecrypt": {2},
        "otpencrypt": {2},
        "otpdecrypt": {2},
    }
}
COMMANDMAP: dict[str, dict[str, callable]] = {
    "unipower": {
        "ohmslaw": OhmsLaw,
        "voltdivider": VoltDivider,
        "rctimeconstant": RCTimeConstant,
        "inductorimpedance": InductorImpedance,
        "powerdissipation": PowerDissipation,
        "resistorinsight": ResistorInsight,
        "resistorviz": ResistorViz,
        "capacitance": TotalCapacitance,
        "esr": TotalESR,
    },
    "unimake": {
        "torque": Torque,
        "gearratio": GearRatio,
        "angularvelocityr": AngularVelocityR,
        "angularvelocityd": AngularVelocityD,
        "kineticenergy": KineticEnergy,
        "potentialenergy": PotentialEnergy,
    },
    "unimath": {
        "D2R": D2R,
        "R2D": R2D,
        "sinerule": SineRule,
        "cosinerule": CosineRule,
        "reversecosinerule": ReverseCosineRule,
        "sasarea": SASArea,
        "herons": HeronsFormula,
    },
    "unialgo": {
        "fibonaccilist": FibonacciList,
        "fibonacciinteger": FibonacciInteger,
        "lovelacesalgorithm": LovelacesAlgorithm,
    },
    "unicrypt": {
        "binaryencrypt": BinaryEncrypt,
        "binarydecrypt": BinaryDecrypt,
        "ceasarencrypt": CeasarEncrypt,
        "ceasardecrypt": CeasarDecrypt,
        "vigenereencrypt": VigenereEncrypt,
        "vigeneredecrypt": VigenereDecrypt,
        "railfenceencrypt": RailfenceEncrypt,
        "railfencedecrypt": RailfenceDecrypt,
        "otpencrypt": OTPEncrypt,
        "otpdecrypt": OTPDecrypt,
    }
}
COMPLETER = NestedCompleter.from_nested_dict({
    "unipower": {
        "ohmslaw": None,
        "voltdivider": None,
        "rctimeconstant": None,
        "inductorimpedance": None,
        "powerdissipation": None,
        "resistorinsight": None,
        "resistorviz": None,
        "capacitance": None,
        "esr": None,
    },
    "unimake": {
        "torque": None,
        "gearratio": None,
        "angularvelocityr": None,
        "angularvelocityd": None,
        "kineticenergy": None,
        "potentialenergy": None,
    },
    "unimath": {
        "D2R": None,
        "R2D": None,
        "sinerule": None,
        "cosinerule": None,
        "reversecosinerule": None,
        "sasarea": None,
        "herons": None,
    },
    "unialgo": {
        "fibonaccilist": None,
        "fibonacciinteger": None,
        "lovelacesalgorithm": None,
    },
    "unicrypt": {
        "binaryencrypt": None,
        "binarydecrypt": None,
        "ceasarencrypt": None,
        "ceasardecrypt": None,
        "vigenereencrypt": None,
        "vigeneredecrypt": None,
        "railfenceencrypt": None,
        "railfencedecrypt": None,
        "otpencrypt": None,
        "otpdecrypt": None,
    }
})

### SYSTEM

def VerifyTokens(TokenList: list) -> bool:
    """Verify validity of tokens before dispatching."""
    if not TokenList: 
        raise EmptyTokenList
    elif TokenList[0] not in COMMANDMAP:
        raise UnknownModule(TokenList[0])
    elif len(TokenList) < 2:
        raise MissingCommand(TokenList[0])
    elif TokenList[1] not in COMMANDMAP[TokenList[0]]:
        raise UnknownSubCommand(TokenList[0], TokenList[1])
    else:
        return True
def ValidateArgs(TokenList: list) -> bool:
    """Validate that the arguments passed into a function are of the correct lenght."""
    Module, Command, Args = TokenList[0], TokenList[1], TokenList[2:]
    if len(Args) not in ARGUMENTMAP[Module][Command]:
        raise IncorrectArgumentCount(COMMANDMAP[Module][Command], len(Args), ARGUMENTMAP[Module][Command])
    else:
        return True

### RECIEVE EVAL PRINT LOOP --- MAIN FUNCTION

def REPL() -> None:
    while True:
        try:
            commandstr = prompt("ORION >>> ", completer=COMPLETER)
            print(dispatcher(commandstr))
            
        except Exception as e:
            print(e)
            continue_ = questionary.confirm("An error occured, continue?")
            
            if not continue_:
                sys.exit()   
                               