"""ORION Engineering Assistant CLI - V.1"""

from data.modules import omniform # orion formula, function and methods library
import json, numpy, scipy, pandas, random, pathlib # unused != is not going to be used

ROOTPATH = pathlib.Path(__file__).parent

def InsertJSON(PathToJSON: str, ContentDict: dict) -> bool:
    try:
        with open(PathToJSON, 'w') as JSONFile:
            json.dump(ContentDict, JSONFile, indent=4, sort_keys=True)
            return True
    except Exception:
        return False
def ExtractJSON(PathToJSON: str) -> dict:
    with open(PathToJSON, 'r', encoding='utf-8') as file:
        ReturnDict = json.load(file)
        return ReturnDict

if __name__ == "__main__":
    omniform.REPL()