
# voltage = resistance * amperage
# amperage = voltage / resistance
# resistance = voltage / amperage

def voltcalc(amp: float, res: float) -> float:
    return amp * res
def ampcalc(volt: float, res: float) -> float:
    return volt * res
def rescalc(volt: float, amp: float) -> float:
    return volt / amp

