


def sparingscalc():
    innskudd = float(input("innskudd: "))
    rente = float(input("rente: "))
    år = int(input("år: "))
    telleår = 0

    for i in range(år):
        telleår += 1
        nyverdi = innskudd + innskudd * (rente / 100)
        print(f"år {telleår}: {innskudd:.2f} * {rente}% = {nyverdi:.2f}")
        innskudd = nyverdi
    print(f"totalt: {nyverdi:.2f}")   
sparingscalc()

