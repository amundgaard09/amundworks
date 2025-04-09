import hashlib
import os

def hash_passord(passord):
    return hashlib.md5(passord.encode()).hexdigest()
def signup():
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
    while True:
        print("DysonSphere Login!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

def main_user():
    print("welcome, user")
    #placeholder for main function'
def main_admin():
    print("welcome, admin")
    #placeholder for main function
def login_successful():
    print("User Login Successful: Starting Up")
    main_user()
def login_unsuccessful():
    print("Login Unsuccessful: Please try again")
    continue_choice = input("Do you want to try again? (y/n): ").strip().lower()
    if continue_choice == 'y':
        login()
    else:
        print("Exiting...")
        exit()
def login_admin_successful():
    print("Admin Login Successful: Starting Up")
    main_admin()
def login_admin_unsuccessful():
    print("Admin Login Unsuccessful: Please try again")
    continue_choice = input("Do you want to try again? (y/n): ").strip().lower()
    if continue_choice == 'y':
        login()
    else:
        print("Exiting...")
        exit()

    while True:
        print("Welcome to the Dyson Sphere Program!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

startup()


