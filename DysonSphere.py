
# dysonsphere v1.0.0.1 copyright 2025 AmundWorks all rights reserved
# Amundworks Encryption Library       | copyright (c) 2025 AmundWorks
# Amundworks General Function Library | copyright (c) 2025 AmundWorks
# Amundworks Mathematics Library      | copyright (c) 2025 AmundWorks

import hashlib
import os
import amundworks_encryption_library as awel
import amundworks_general_function_library as awgfl
import amundworks_mathematics_library as awml
import questionary

def hash_passord(passord):
    '''hashing password function'''
    return hashlib.md5(passord.encode()).hexdigest()
def signup():
    '''user/admin signup function'''
    email = input("Enter email address: ").strip()
    pwd = input("Enter password: ").strip()
    conf_pwd = input("Confirm password: ").strip()
    if conf_pwd != pwd:
        print("Passwords do not match! Try again.\n")
        return
    role = input("Enter role (user/admin): ").strip().lower()
    if role not in ["user", "admin"]:
        print("Invalid role! Defaulting to user.\n")
        role = "user"
    hashed_pwd = hash_passord(pwd)
    if os.path.exists("credentials.txt"):
        with open("credentials.txt", "r") as f:
            for linje in f:
                if "," not in linje:
                    continue
                lagret_email, _, _ = linje.strip().split(",")
                if email == lagret_email:
                    print("Email already registered. Please log in.\n")
                    return
    with open("credentials.txt", "a") as f:
        f.write(f"{email},{hashed_pwd},{role}\n")
    print(f"Registered successfully as {role}!\n")
    if role == "admin":
        main_admin()
    elif role == "user":
        main_user()
def login():
    '''user/admin login function'''
    email = input("Enter email: ").strip()
    pwd = input("Enter password: ").strip()
    hashed_input = hash_passord(pwd)
    try:
        with open("credentials.txt", "r") as f:
            for linje in f:
                if "," not in linje:
                    continue
                deler = linje.strip().split(",")
                if len(deler) != 3:
                    continue
                lagret_email, lagret_hash, rolle = deler
                if email == lagret_email and hashed_input == lagret_hash:
                    print("Logged in Successfully!\n")
                    if rolle == "admin":
                        login_admin_successful()
                    else:
                        login_successful()
                    return
        print("Login failed! Wrong email or password.\n")
        login_unsuccessful()
    except FileNotFoundError:
        print("No users registered yet. Please sign up first.\n")
def startup():
    choice = questionary.select(
        "Choose a cipher/decoding method:",
        choices=[ 
            "login",
            "signup",
            "debug",
            "exit",
        ]
    ).ask()    
    if choice == "login":
        login()
    elif choice == "signup":
        signup()
    elif choice == "debug":
        main_admin()
    elif choice == "exit":
        print("Goodbye!")
        exit()
def login_successful():
    '''user login successful'''
    print("User Login Successful: Starting Up")
    main_user()
def login_unsuccessful():
    '''user login unsuccessful'''
    print("Login Unsuccessful: Please try again")
    continue_choice = input("Do you want to try again? (y/n): ").strip().lower()
    if continue_choice == 'y' or continue_choice == 'yes':
        login()
    else:
        print("Exiting...")
        exit()
def login_admin_successful():
    '''admin login successful'''
    print("Admin Login Successful: Starting Up")
    main_admin()

def ds_awel():
    '''amundworks encryption library'''
    decode_action = questionary.select(
        "Choose a cipher/decoding method:",
        choices=[ 
            "binary()",
            "vigenerè()",
            "ceasar()",
            "railfence()",
            "return()",
        ]
    ).ask()
    if decode_action == "binary()":
        binary_action = questionary.select(
        "Choose between encryption or decryption:",
        choices=[ 
            "encrypt()",
            "decrypt()",
            "return()",
            ]
        ).ask()
        if binary_action == "encrypt()":
            awel.binary_encrypt()
            ds_awel()
        elif binary_action == "decrypt()":
            awel.binary_decrypt()
            ds_awel()
        elif binary_action == "return()":
            print("Returning to main menu...")
            ds_awel()
    elif decode_action == "vigenerè()":
        vigenerè_action = questionary.select(
            "Choose between encryption or decryption:",
            choices=[ 
                "encrypt()",
                "decrypt()",
                "return()",
                ]
        ).ask()
        if vigenerè_action == "encrypt()":
            awel.vigenere_encrypt()
            ds_awel()   
        elif vigenerè_action == "decrypt()":
            awel.vigenere_decrypt()
            ds_awel()
        elif vigenerè_action == "return()":
            print("Returning to main menu...")
            ds_awel()
    elif decode_action == "ceasar()":
        ceasar_action = questionary.select(
            "Choose between encryption or decryption:",
            choices=[ 
                "encrypt()",
                "decrypt()",
                "bruteforce_decrypt()",
                "return()",
            ]
        ).ask()
        if ceasar_action == "encrypt()":
            awel.csr_encrypt()
            ds_awel()
        elif ceasar_action == "decrypt()":
            awel.csr_decrypt()
            ds_awel()  
        elif ceasar_action == "bruteforce_decrypt()":
            awel.csr_bruteforce()
            ds_awel() 
        elif ceasar_action == "return()":
            print("Returning to main menu...")
            ds_awel()   
    elif decode_action == "railfence()":
        ceasar_action = questionary.select(
            "Choose between encryption or decryption:",
            choices=[ 
                "encrypt()",
                "decrypt()",
                "return()",
            ]
        ).ask()
        if ceasar_action == "encrypt()":
            awel.railfence_encrypt()
            ds_awel()
        elif ceasar_action == "decrypt()":
            awel.railfence_decrypt()
            ds_awel()   
        elif ceasar_action == "return()":
            print("Returning to main menu...")
            ds_awel() 
    elif decode_action == "return()":
        print("Returning to main menu...")
        main_admin()
def ds_awml():
    '''amundworks mathematics library'''
    awml_action = questionary.select(
        "Choose a function:",
        choices=[ 
            "serielån()",
            "sparing()",
            "tollberegner()",
            "fibonacci()",
            "abc formel()",
            "triangle analysis()",
            "calculate()",
            "return()",
        ]
    ).ask()
    if awml_action == "serielån()":
        awml.serielån()
        ds_awml()
    if awml_action == "sparing()":
        awml.sparingscalc()
        ds_awml()
    if awml_action == "tollberegner()":
        awml.formelark()
        ds_awml()
    if awml_action == "fibonacci()":
        fibonacci_action = questionary.select(
            "Choose between list or int:",
            choices=[ 
                "list()",
                "int()",
                "return()",
            ]
        ).ask()
        if fibonacci_action == "list()":
            awml.fibonacci_list()
            ds_awml()
        elif fibonacci_action == "int()":
            awml.fibonacci_int()
            ds_awml()
        elif fibonacci_action == "return()":
            print("Returning to main menu...")
            ds_awml()
    if awml_action == "abc formel()":
        awml.solve_quadratic()
        ds_awml()
    if awml_action == "triangle analysis()":
        awml.ctaa()
        ds_awml()
    if awml_action == "calculate()":
        awml.calculate()
        ds_awml()
    elif awml_action == "return()":
        print("Returning to main menu...")
        main_admin()
def ds_awgfl():
    '''amundworks general function library'''
    awgfl_action = questionary.select(
        "Choose a function:",
        choices=[ 
            "dices()",
            "return()",
        ]
    ).ask()
    if awgfl_action == "dices()":
        awgfl.dices()
        ds_awgfl()
    elif awgfl_action == "return()":
        print("Returning to main menu...")
        main_admin()

def main_user():
    '''main program for user'''
    print("welcome, user")
    #placeholder for main function
def main_admin():
    '''main program for admin'''
    print("\n")
    action = questionary.select(
        "What would you like to do today?",
        choices=[ 
            "listusers()",
            "delete_user()",
            "AW Encryption Library()",
            "AW General Function Library()",
            "AW Mathematics Library()",
            "shutdown()",
        ]
    ).ask()
    print("\n")
    if action == "listusers()":
        listusers()
        main_admin()
    elif action == "delete_user()":
        delete_user()
        main_admin()
    elif action == "AW Encryption Library()":
        ds_awel()
    elif action == "AW General Function Library()":
        ds_awgfl()
    elif action == "AW Mathematics Library()":
        ds_awml()
    elif action == "shutdown()":
        print("Shutting down...")
        exit()

def listusers():
    '''list all users'''
    try:
        with open("credentials.txt", "r") as f:
            print("Registered Users:")
            for linje in f:
                if "," not in linje:
                    continue
                email, _, role = linje.strip().split(",")
                print(f"Email: {email}, Role: {role}\n")
    except FileNotFoundError:
        print("No users registered yet.\n")
def delete_user():
    '''delete a user'''
    email = input("Enter the email of the user to delete: ").strip()
    try:
        with open("credentials.txt", "r") as f:
            lines = f.readlines()
        with open("credentials.txt", "w") as f:
            for linje in lines:
                if "," not in linje:
                    continue
                lagret_email, _, _ = linje.strip().split(",")
                if lagret_email != email:
                    f.write(linje)
        print(f"User {email} deleted successfully.")
    except FileNotFoundError:
        print("No users registered yet.")
 
startup()

    