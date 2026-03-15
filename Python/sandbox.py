
def f(x: int) -> float:
    return (1-2*x) / (x-2)

x = 8

while x >= -8:
    if x != 2:
        print(x, f(x))
    x -= 1

