# kabal.py | copyright (c) AW 2025

import random

spades   = ['♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K']
hearts   = ['♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K']
diamonds = ['♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K']
clubs    = ['♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']

deck = spades + hearts + diamonds + clubs
temp_deck = deck.copy()
aces = [[], [], [], []]
acecards = ['♠A', '♥A', '♦A', '♣A']

rows = [[] for _ in range(7)] 

def color_card(card):
    if card.startswith('♥') or card.startswith('♦'):
        return f'\033[91m{card}\033[0m'
    else:
        return card
def getcard():
    return random.choice(temp_deck)
def makekabal():
    for i in range(7):
        for j in range(i + 1):
            card = getcard()
            rows[i].append(card)
            temp_deck.remove(card)
def printkabal():
    print("\nKabalstatus:")
    print("------------------")
    for rad in rows:
        print(' '.join(color_card(card) for card in rad))
    print("------------------")
def getcardvalue(card):
    if card.startswith('♠'):
        return spades.index(card) + 1
    elif card.startswith('♥'):
        return hearts.index(card) + 1
    elif card.startswith('♦'):
        return diamonds.index(card) + 1
    elif card.startswith('♣'):
        return clubs.index(card) + 1
def legalplacement(card1, card2):
    """Returnerer True hvis card1 kan plasseres på card2 (forskjellig farge og én lavere verdi)"""
    if not card2:
        return True 

    IsLegalIndex = getcardvalue(card1) == (getcardvalue(card2) - 1)

    if (card1 in spades or card1 in clubs) and (card2 in hearts or card2 in diamonds):
        IsDifferentColor = True
    elif (card1 in hearts or card1 in diamonds) and (card2 in spades or card2 in clubs):
        IsDifferentColor = True
    else: 
        IsDifferentColor = False

    return IsLegalIndex and IsDifferentColor
def moverow(fromcard_index, fromrow, torow):
    """Flytter kort og alle under det fra en rad til en annen, eller til ess"""
    if fromrow < 0 or fromrow >= len(rows) or torow < 0 or torow >= len(rows):
        print("Ugyldig rad.")
        return

    index = fromcard_index - 1

    if index < 0 or index >= len(rows[fromrow]):
        print("Ugyldig kortindeks i raden.")
        return

    fromcard = rows[fromrow][index]

    if fromcard in acecards:
        aceindex = acecards.index(fromcard)
        aces[aceindex].append(fromcard)
        rows[fromrow].remove(fromcard)
        return

    kort_som_skal_flyttes = rows[fromrow][index:]
    rows[torow].extend(kort_som_skal_flyttes)
    del rows[fromrow][index:]
def movecardtoace(row):
    """Flytter det nederste kortet i en rad til riktig ess-rad"""
    if not rows[row]:
        print("Raden er tom.")
        return
    cardtomove = rows[row][-1]
    if cardtomove in spades:
        aces[0].append(cardtomove)
    elif cardtomove in hearts:
        aces[1].append(cardtomove)
    elif cardtomove in diamonds:
        aces[2].append(cardtomove)
    elif cardtomove in clubs:
        aces[3].append(cardtomove)
    rows[row].remove(cardtomove)

def main():
    makekabal()

    while temp_deck:
        place_card = temp_deck[0]
        printkabal()

        print("Ess-rader:")
        for i in range(4):
            print(f"{['♠', '♥', '♦', '♣'][i]}: {' '.join(aces[i]) or 'Tom'}")

        print(f"\nNeste kort: {color_card(place_card)}")

        try:
            placement = int(input("Hvor vil du plassere kortet? (skip 0)(1-7)(ess 8)(flytt rad 9)(til ess 10): ")) - 1
        except ValueError:
            print("Ugyldig input. Skriv et tall mellom 1 og 10.")
            continue

        if not (-1 <= placement <= 9):
            print("Ugyldig valg. Prøv igjen.")
            continue

        if placement == -1:
            
            temp_deck.append(temp_deck.pop(0))
            continue

        if placement == 7: 
            if place_card in acecards:
                ace_index = acecards.index(place_card)
                aces[ace_index].append(place_card)
                temp_deck.remove(place_card)
            else:
                print("Kortet er ikke et ess!")
            continue

        if placement == 8:
            try:
                from_row = int(input("Fra hvilken rad? (1-7): ")) - 1
                to_row = int(input("Til hvilken rad? (1-7): ")) - 1
                from_card = int(input(f"Hvilket kort (nummer fra toppen, 1 = øverste): "))
                if rows[from_row][from_card - 1] in acecards:
                    moverow(from_card, from_row, to_row) 
                else:
                    moverow(from_card, from_row, to_row)
            except (ValueError, IndexError):
                print("Ugyldig input for flytting.")
            continue

        if placement == 9:  
            try:
                row = int(input("Hvilken rad vil du flytte fra? (1-7): ")) - 1
                movecardtoace(row)
            except (ValueError, IndexError):
                print("Ugyldig rad.")
            continue

        if rows[placement]:
            topp_kort = rows[placement][-1]
            if not legalplacement(place_card, topp_kort):
                print("Ulovlig trekk!")
                temp_deck.append(temp_deck.pop(0))
                continue

        rows[placement].append(place_card)
        temp_deck.remove(place_card)

    print("Ingen flere kort igjen. Spillet er over!")

main()
