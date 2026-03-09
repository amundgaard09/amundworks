"""Miscellaneous functions - AMUNDWORKS"""

from typing import Literal

def LogicGate(
    A1: bool | Literal[0, 1], 
    B1: bool | Literal[0, 1], 
    operand: Literal["AND", "OR", "NOR", "NAND", "XOR", "XNOR"]
    ) -> bool:
    
    match operand:
        case "AND":
            return A1 + B1 == 2
        case "OR":
            return A1 + B1 >= 1
        case "NOR":
            return A1 + B1 == 0
        case "NAND":
            return A1 + B1 < 2
        case "XOR":
            return A1 + B1 == 1
        case "XNOR":
            return A1 + B1 != 1
def GetLogicTrainingSet(Operand: Literal["AND", "OR", "NOR", "NAND", "XOR", "XNOR"]):
    X_1, Y_1 = [], []
    Combinations = [[0,0], [0,1], [1,0], [1,1]]
    
    for i in range(len(Combinations)):
        X_1.append(Combinations[i])
        Y_1.append(int(LogicGate(Combinations[i][0], Combinations[i][1], Operand)))
    
    return X_1, Y_1

