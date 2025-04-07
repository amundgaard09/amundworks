
# pycalc.py
import math
import cmath

def add(a,b):
    return a + b
def subtr(a,b):
    return a - b
def multi(a,b):
    return a * b
def divd(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a / b
def sqrt(a):
    return cmath.sqrt(a)
def expo(a,b):
    return a**b
def sin(a):
    x = input("degrees or radians?")
    if x == 'degrees':
        return math.sin(math.radians(a))
    if x == 'radians':
        return math.sin(a)
def cos(a):
    x = input("degrees or radians?")
    if x == 'degrees':
        return math.cos(math.radians(a))
    elif x == 'radians':
        return math.cos(a)  
def tan(a):
    x = input("degrees or radians?")
    if x == 'degrees':
        return math.tan(math.radians(a))
    elif x == 'radians':
        return math.tan(a) 
def formelark(kostnad, frakt, tollsats, mvaprosent, fortolling_gebyr):
    beregningsgrunnlag_toll = kostnad + frakt
    toll = beregningsgrunnlag_toll * tollsats/100
    mvagrunnlag = beregningsgrunnlag_toll + toll
    mva = mvagrunnlag * mvaprosent/100
    totalpris = mvagrunnlag + mva + fortolling_gebyr
    answer = totalpris
    return answer
dub_variable_ops = [1,2,3,4,6] # ops that need 2 inputs
while True:
    try: # moo 
        moo = int(input("0. exit\n1. addition\n2. subtraction\n3. multiplication\n4. division\n5. square root\n6. exponentiation\n7. sine\n8. cosine\n9. tangent\n10. formelark\nChoose mode of operation: "))
        if moo < 0: 
            print("invalid number")
            continue
    except ValueError: 
        print("invalid input")
        continue
    if moo == 0: # exit
        print("shutting down...")
        print("goodbye!")
        break
    if moo == 10: # formelark
        try: 
            kostnad = float(input("kostnad:"))
            frakt = float(input("frakt:"))
            tollsats = float(input("tollsats %:"))
            mvadesimal = float(input("mva %:"))
            fortolling_gebyr = float(input("fortollingsgebyr:"))
            answer = formelark(kostnad, frakt, tollsats, mvadesimal, fortolling_gebyr)
            print(f"answer:{answer}")
            continue
        except ValueError:
            print("invalid input")
            continue
    try: # a 
        a = float(input("a:"))
    except ValueError: 
        print("invalid input")
        continue
    if moo in dub_variable_ops: # b 
        try:
            b = float(input("b:"))
        except ValueError:
            print("invalid input")
            continue
    if moo == 1: # add
        answer = add(a,b)
    if moo == 2: # subtract
        answer = subtr(a,b)
    if moo == 3: # multiply
        answer = multi(a,b)
    if moo == 4: # divide
        answer = divd(a,b)
    if moo == 5: # square root
        answer = sqrt(a)
    if moo == 6: # exponent
        answer = expo(a,b)
    if moo == 7: # sin
        answer = sin(a)
    if moo == 8: # cos
        answer = cos(a) 
    if moo == 9: # tan
        answer = tan(a)
    print(answer)