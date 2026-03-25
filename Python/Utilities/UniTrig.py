### UniTrig CLI - iteration I - AmundWorks Unified Trigonometry Assistant

import sys
import math
from typing import Literal

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
def ReverseCosineRule(LengthA: float, LengthB: float, LengthC: float) -> float:
    """ 
    Returns a tuple of the three angles in degrees, in the order of AngleA, AngleB, AngleC 
    
    Formula: AngleA = arccos((B^2 + C^2 - A^2) / (2BC))
    """

    return (
        math.degrees(math.acos((LengthB ** 2 + LengthC ** 2 - LengthA ** 2) / (2 * LengthB * LengthC))),  # AngleA
        math.degrees(math.acos((LengthC ** 2 + LengthA ** 2 - LengthB ** 2) / (2 * LengthC * LengthA))),  # AngleB
        math.degrees(math.acos((LengthA ** 2 + LengthB ** 2 - LengthC ** 2) / (2 * LengthA * LengthB)))   # AngleC
    )

def ConventionalTriangleArea(LengthA: float, LengthB: float, AngleC: float) -> float:
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

def Executor(UserInput: str) -> str:
    StrippedInput = UserInput.strip().split()
    if len(StrippedInput) == 0:
        return ""
    
    Command, Arguments = StrippedInput[0], StrippedInput[1:]
    CommandList = ["D2R", "R2D", "SR", "CSR", "RCSR", "CTA", "HF", "break"]
    
    ### Wanted Argument for each Function
    ArgumentsForFunctions = {
        "D2R":  1,
        "R2D":  1,
        "SR":   3,
        "CSR":  3,
        "RCSR": 3,
        "CTA":  3,
        "HF":   3,
        "help": 0,
        "break":0 
    }
    
    if Command not in CommandList:
        print(f"unknown command! {Command}")
        return ""
    
    GivenArgumentCount = len(Arguments)
    
    ### Incorrect Arguments Error Catcher
    if GivenArgumentCount != ArgumentsForFunctions[Command]:
        print(f"Incorrect amount of arguments for {Command}! {Command} takes {ArgumentsForFunctions[Command]} arguments but was given {len(Arguments)}")
        return ""
    
    match Command:
        case "D2R":
            return str(D2R(float(Arguments[0])))
        case "R2D":
            return str(R2D(float(Arguments[0])))
        case "SR":
            sides = [float(x) if x != "None" else None for x in Arguments[0].split(",")]
            angles = [float(x) if x != "None" else None for x in Arguments[1].split(",")]
            mode = Arguments[2]
            result = SineRule(sides, angles, mode)
            return str(result) if result else "No solution"
        case "CSR":
            return str(CosineRule(float(Arguments[0]), float(Arguments[1]), float(Arguments[2])))
        case "RCSR":
            return str(ReverseCosineRule(float(Arguments[0]), float(Arguments[1]), float(Arguments[2])))
        case "CTA":
            return str(ConventionalTriangleArea(float(Arguments[0]), float(Arguments[1]), float(Arguments[2])))
        case "HF":
            return str(HeronsFormula(float(Arguments[0]), float(Arguments[1]), float(Arguments[2])))
        case "help":
            print("Functions: \nDegrees 2 Radians (D2R) \nRadians 2 Degrees (R2D) \nSine Rule (SR) \nCosineRule (CSR) \nReverse Cosine Rule (RCSR) \nConventional Triangle Area (CTA) \nHerons Formula (HF) \nbreak")
        case "break":
            sys.exit()
        
while True:
    print(Executor(str(input(" >>> "))))