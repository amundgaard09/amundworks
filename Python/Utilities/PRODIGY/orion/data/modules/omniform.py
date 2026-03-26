"""Utility Library for the ORION CLI - Iteration I"""

from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.completion import NestedCompleter
from typing_extensions import Callable
from typing import Literal
import questionary
import shlex
import sys

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
    def __init__(self, GivenCommand: str):
        self.GivenCommand = GivenCommand
        super().__init__(f"Unknown Command: {GivenCommand}")
class UnknownSubCommand(Exception):
    """Raises when an unknown subcommand gets caught in VerifyTokens()."""
    def __init__(self, Module: str, GivenCommand: str):
        self.Module = Module
        self.GivenCommand = GivenCommand
        super().__init__(f"Unknown command for {Module}: {GivenCommand}")
class MissingCommand(Exception):
    def __init__(self, module):
        super().__init__(f"Missing subcommand for {module}")    
class InvalidColors(Exception):
    def __init__(self, function: Callable, IndexOfInvalidColors: list):
        super().__init__(f"Invalid colors for {function} at indices {IndexOfInvalidColors}")

def Tokenize(RawCommandString: str) -> list[str]:
    """Tokenize a raw command string and return token list."""
    return shlex.split(RawCommandString)
def dispatcher(RawCommandString: str) -> str:
    Tokens = Tokenize(RawCommandString) 
    VerifyTokens(Tokens)
    ValidateArgs(Tokens)
    Module, Command, Args = Tokens[0], Tokens[1], Tokens[2:]
    return COMMANDMAP[Module][Command](Args)

def ResistorViz(colorlist: list):
    """Prints a ASCII representation of a resistor with the color code""" 
    def color_block(color: str):
        ansi = ANSI_COLORS.get(color.lower(), "\033[0m")
        reset = "\033[0m"
        return f"{ansi}    {reset}"
    
    if len(colorlist) == 5:
        c1, c2, c3, c4, c5 = colorlist
        
    elif len(colorlist) == 4:
        c1, c2, c3, c4 = colorlist
        c5 = None
        
    else:
        raise InvalidColorCount(ResistorViz)
        
    if c5 is not None:
        return f"    <----------------------------->\n    |                             |\n    |  ┌────┬────┬────┬────┬────┐ |\n   ----│{color_block(c1)}│{color_block(c2)}│{color_block(c3)}│{color_block(c4)}│{color_block(c5)}|----\n    |  └────┴────┴────┴────┴────┘ |\n    |                             |\n    <----------------------------->" 
    else:
        return f"    <------------------------->\n    |                         |\n    |  ┌────┬────┬────┬────┐  |\n   ----│{color_block(c1)}│{color_block(c2)}│{color_block(c3)}│{color_block(c4)}│----\n    |  └────┴────┴────┴────┘  |\n    |                         |\n    <------------------------->" 
def ResistorInsight(colorlist: list) -> tuple:
    """Takes in 4/5 colors of a resistor and returns the resistivity and tolerance range."""
    
    if None in colorlist:
        raise InvalidColorCount(ResistorInsight)
    
    band1int = BAND.get(colorlist[0])
    band2int = BAND.get(colorlist[1]) 
    band3int = None
    
    if len(colorlist) == 4:
        multiplierint = MULTIPLIER.get(colorlist[2])
        tolerance_percent = TOLERANCE.get(colorlist[3])
        
    elif len(colorlist) == 5:
        band3int = BAND.get(colorlist[2])
        multiplierint = MULTIPLIER.get(colorlist[3])
        tolerance_percent = TOLERANCE.get(colorlist[4])
        
    else:
        raise InvalidColorCount(ResistorInsight)
        
    if len(colorlist) == 4:
        bands = (band1int, band2int, multiplierint, tolerance_percent)
        
        if None in bands:
            raise InvalidColors(ResistorInsight, bands.index(None) + 1)
        
        resistance = (band1int * 10 + band2int) * multiplierint
    
    else:
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

ARGUMENTMAP: dict[str, set] = {
    "resistor": {
        "spec": {4, 5},
        "viz": {4, 5}
        },
    "capacitor": {
        "capacitance": {2},
        "esr": {2},
    }    
}
COMMANDMAP: dict[str, dict[str, callable]] = {
    "resistor": {
        "spec": ResistorInsight,
        "viz": ResistorViz,
    },
    "capacitor": {
        "capacitance": TotalCapacitance,
        "esr": TotalESR,  
    }
}
COMPLETER = NestedCompleter.from_nested_dict({
    "resistor": {
        "spec": None,
        "viz": None
        },
    "capacitor": {
        "capacitance": None,
        "esr": None, 
    } 
})

def VerifyTokens(TokenList: list) -> bool:
    """Verify validity of tokens before dispatching."""
    if not TokenList: 
        raise EmptyTokenList
    elif len(TokenList) < 2:
        raise MissingCommand(TokenList[0])
    elif TokenList[0] not in COMMANDMAP:
        raise UnknownModule(TokenList[0])
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

def REPL():
    while True:
        try:
            commandstr = prompt("ORION >>> ", completer=COMPLETER)
            print(dispatcher(commandstr))
            
        except Exception as e:
            print(e)
            continue_ = questionary.confirm("An error occured, continue?")
            
            if not continue_:
                sys.exit()
            
    REPL()