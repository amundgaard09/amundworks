"""The complete engine for the ICARUS NUI Complex"""

import speech_recognition as sr
import electratex as etex

class NoCmdError(Exception):
    pass

def cmdexe(cmdstr: str) -> object | Exception:
    COMMANDS = {
        "resistorscan": etex.resistancecalc
    }
    """ICARUS command parse funcction. It parses a command string and returns a function"""
    tokenlist: list = cmdstr.strip().lower().split()
    if not tokenlist:
        return 
    
    command, tokens = tokenlist[0], tokenlist[1:]
    


