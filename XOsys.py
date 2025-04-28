
#Bruk klasser inshallah
import os
import hashlib
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
                        print("Welcome Admin!\n")
                    else:
                        print("Welcome User!\n")
        print("login failed! Wrong email or password.\n")
        choice = questionary.select(
            "Try Again or Exit?",
            choices=[ 
                "Try Again",
                "exit",
            ]
        ).ask()
        if choice == "Try Again":
            login()
        elif choice == "exit":
            print("Goodbye!")
            exit()
    except FileNotFoundError:
        print("No users registered yet. Please sign up first.\n")

class XOsys:
    def __init__(self):
        self.startup()
    def startup(self):
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
        elif choice == "dev":
            placeholder = placeholder
        elif choice == "exit":
            print("Goodbye!")
            exit()
        
class admin(XOsys):
    def __init__(self):
        super().__init__()
        self.startup()
