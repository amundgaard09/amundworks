
# serielån complete 
while True:
    lånbeløp = float(input("lånbeløp:"))
    etableringsgebyr = float(input("etableringsgebyr:"))
    termingebyr = float(input("termingebyr:"))
    rente = float(input("rente %:"))
    antallterminer = int(input("antall terminer:"))
    terminbeløp = lånbeløp/antallterminer
    totalkostnad = etableringsgebyr
    restbeløp = lånbeløp
    totalrente = 0
    print(" - /"*40,"-")

    for i in range(antallterminer):

        terminbeløpetterrente = terminbeløp + restbeløp * (rente/100) + termingebyr
        totalkostnad += terminbeløpetterrente
        restbeløp -= terminbeløp
        totalgebyr = termingebyr * antallterminer
        terminrente = restbeløp * (rente/100)
        totalrente += terminrente

        print(f"termin {i+1}: |restbeløp:{restbeløp:.2f}|avdrag:{terminbeløp:.2f}|termingebyr:{termingebyr}|rente:{terminrente:.2f}|terminbeløp:{terminbeløpetterrente:.2f}")
    print("--------------------------------------------------")
    print(f"total kostnad: {totalkostnad:.2f}") 
    print(f"total gebyr: {totalgebyr:.2f}")
    print(f"total rente: {totalrente:.2f}")
    print(" - /"*40,"-")