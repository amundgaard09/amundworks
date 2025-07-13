"""Fusion Anvil is the main program of the FUTUREFORGE Engineering System. This is where your ideas get forged and realized with intelligent programming"""

from foundry import toolsteel
import questionary
import os 

### convert long if elif chains to function dicts
### expand resistorspec() with 5-color decoding
### expand resistorspec with value-to-color encoding (use bool in function "color2value == True")

def asciibanner():
    print(toolsteel.LOGO)
def placeholder():
    print("no functionality added!")
    exit()
def clearterminal():
    os.system("cls")

### 1. TIER FUNCTIONS

def electrical():
    while True:
        choice = questionary.select(
            " --- FUTUREFORGE Electrotechnical Tools --- ",
            choices=[
                questionary.Choice("1 - Resistor Tools",   shortcut_key="1"),
                questionary.Choice("2 - Capacitor Tools",  shortcut_key="2"),
                questionary.Choice("3 - Inductor Tools",   shortcut_key="3"),
                questionary.Choice("4 - Diode Tools",      shortcut_key="4"),
                questionary.Choice("5 - Transistor Tools", shortcut_key="5"),
                questionary.Choice("6 - Return",           shortcut_key="6"),
            ]
        ).ask()
    
        match choice[0]:
            case "1": resistortools()
            case "2": capacitortools()
            case "3": inductortools()
            case "4": diodetools()
            case "5": transistortools()
            case "6": break 
def mechanical():
    """FUTUREFORGE CLI Mechanical Engineering Functions Library"""
    placeholder()
def robokinematics():
    """FUTUREFORGE CLI Robokinematics Engineering Functions Library"""
    placeholder()
def chemical():
    """FUTUREFORGE CLI Chemical Engineering Functions Library"""
    placeholder()

### 2. TIER ELECTRICAL FUNCTIONS

def resistortools():
    while True:
        choice = questionary.select(
            " --- FUTUREFORGE Resistor Tools --- ",
            choices=[
                questionary.Choice("1 - Resistor Specs",               shortcut_key="1"),
                questionary.Choice("2 - Required Resistor Calculator", shortcut_key="2"),
                questionary.Choice("5 - Return",                       shortcut_key="3"),
            ]
        ).ask()

        match choice[0]:
            case "1": rs_wrapper()      
            case "2": rrc_wrapper()
            case "5": break
def capacitortools():
    pass
def inductortools():
    pass
def diodetools():
    pass
def transistortools():
    pass

### 3. TIER RESISTOR FUNCTIONS

def rs_wrapper():
    """Asks user for colors on the resistor for Resistor Specs Function"""
    while True:
        colors = str(input("Resistor Colors (4): "))
        colorlist: list = colors.strip().split(" ")
        try:
            specs: tuple = toolsteel.resistorspec(colorlist[0],colorlist[1],colorlist[2],colorlist[3])
            print(" - - SPECS - - ")
            print(f"{specs[0]}") # resistance
            print(f"{specs[1]}") # range
            print(f"{specs[2]}") # ascii colored representation 
        except (toolsteel.MissingColorsError, toolsteel.WrongColorError):
            print("ERROR! Must be 4/5 valid colors. Double-check and return.")
            askcontinue = questionary.confirm("Continue?").ask()
            if askcontinue:
                continue
            else:
                print(" RETURNING... ")
                break            
def rrc_wrapper():
    """Calculates required resistor based on voltage and current"""
    while True:
        try:
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))
            resistance = voltage / current
        except (ValueError, ZeroDivisionError):
            print("ERROR! Invalid Values")
            continue
        print(f"Required Resistance: {resistance} Ω")
        askcontinue = questionary.confirm("Continue?").ask()
        if askcontinue:
            continue
        else: 
           print(" RETURNING... ")
           break            

### FUTUREFORGE ANVIL CLI

def forgeanvil_cli():
    clearterminal()
    choice = questionary.select(
        " --- FUTUREFORGE CLI version 1.0.0.1 --- ",
        choices=[
            questionary.Choice("1. - Electrotechnical Tools",    shortcut_key="1"),
            questionary.Choice("2. - Mechanical Tools",          shortcut_key="2"),
            questionary.Choice("3. - Robotics/Kinematics Tools", shortcut_key="3"),
            questionary.Choice("4. - Chemical Tools",            shortcut_key="4"),
            questionary.Choice("5. - Exit",                      shortcut_key="5"),
        ]
    ).ask()

    match choice[0]:
        case "1": electrical()
        case "2": mechanical()
        case "3": robokinematics()
        case "4": chemical()
        case "5": exit()

if __name__ == "__main__":
    forgeanvil_cli()