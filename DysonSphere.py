
# dysonsphere v1.0.0.1 copyright 2025 amundworks all rights reserved

import hashlib
import os
import amundworks_encryption_library as awel
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
                        isLoggedIn = True
                        isAdmin = True
                    else:
                        login_successful()
                        isLoggedIn = True
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
        signup()
    elif choice == "signup":
        login()
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
    if continue_choice == 'y':
        login()
    else:
        print("Exiting...")
        exit()
def login_admin_successful():
    '''admin login successful'''
    print("Admin Login Successful: Starting Up")
    main_admin()
def login_admin_unsuccessful():
    '''admin login unsuccessful'''
    print("Admin Login Unsuccessful: Please try again")
    continue_choice = input("Do you want to try again? (y/n): ").strip().lower()
    if continue_choice == 'y':
        login()
    else:
        print("Exiting...")
        exit()
def ds_awel():
    '''amundworks encryption library function'''
    decode_action = questionary.select(
        "Choose a cipher/decoding method:",
        choices=[ 
            "binary()",
            "vigenerè()",
            "ceasar()",
            "railfence() (coming soon)",
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
                "return()",
            ]
        ).ask()
        if ceasar_action == "encrypt()":
            awel.csr_encrypt()
            ds_awel()
        elif ceasar_action == "decrypt()":
            awel.csr_decrypt()
            ds_awel()   
        elif ceasar_action == "return()":
            print("Returning to main menu...")
            ds_awel()   
    elif decode_action == "railfence()":
        #placeholder for railfence function
        main_admin()
    elif decode_action == "return()":
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
        "Choose an action:",
        choices=[ #gjør hvert cipher om til en funksjon og lag en spørre funksjon for å velge mellom krypteringsmetodene
            "listusers()",
            "delete_user()",
            "AWEL()",
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
    elif action == "AWEL()":
        ds_awel()
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
