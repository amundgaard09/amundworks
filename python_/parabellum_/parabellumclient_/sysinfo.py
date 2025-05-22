
import socket
import hashlib
import os

CLASSIFICATIONS = {
    1: "Public",
    2: "Restricted",
    3: "Classified",
    4: "Secret",
    5: "Top Secret",
}
FOREIGNENTITIES = {
    1: "ALLY",
    2: "FRIENDLY",
    3: "NEUTRAL",
    4: "UNFRIENDLY",
    5: "HOSTILE",
    6: "THREAT",
}

ARMYRANKS = {
    "OF-1": "2ND LIEUTENANT",
    "OF-1": "1ST LIEUTENANT",
    "OF-2": "CAPTAIN",
    "OF-3": "MAJOR",
    "OF-4": "LIEUTENANT COLONEL",
    "OF-5": "COLONEL",
    "OF-6": "BRIGADIER",
    "OF-7": "MAJOR GENERAL",
    "OF-8": "LIEUTENANT GENERAL",
    "OF-9": "GENERAL",
}
AIRRANKS = {
    "OF-1": "2ND LIEUTENANT",
    "OF-1": "1ST LIEUTENANT",
    "OF-2": "LIEUTENANT CAPTAIN",
    "OF-3": "CAPTAIN",
    "OF-4": "COMMANDING CAPTAIN",
    "OF-5": "COMMANDER",
    "OF-6": "COMMODORE",
    "OF-7": "COUNTER ADMIRAL",
    "OF-8": "VICE ADMIRAL",
    "OF-9": "ADMIRAL",
} 
NAVYRANKS = {
    "OF-1": "2ND LIEUTENANT",
    "OF-1": "1ST LIEUTENANT",
    "OF-2": "CAPTAIN",
    "OF-3": "MAJOR",
    "OF-4": "LIEUTENANT COLONEL",
    "OF-5": "COLONEL",
    "OF-6": "BRIGADIER",
    "OF-7": "MAJOR GENERAL",
    "OF-8": "LIEUTENANT GENERAL",
    "OF-9": "GENERAL",
}

SERVER_IP: str
USERPATH: str
PORT: int
client: socket.socket

def serverconnect(ip: str, port: int) -> (tuple[socket.socket, bool]) | (tuple[None, bool]):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip, port))
        print("[CLIENT] Tilkoblet.")
        return client, True
    except ConnectionRefusedError:
        print("[CLIENT] Server er avslått.")
        return None, False
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
def login(user: str, pwd: str) -> bool:
    hashed_input = hash_password(pwd)
    try:
        with open(USERPATH, "r") as f:
            for linje in f:
                if "," in linje:
                    u, h = linje.strip().split(",")
                    if user == u and hashed_input == h:
                        return True
    except FileNotFoundError:
        pass
    return False
def signup(user: str, pwd: str) -> bool:
    hashed_pwd = hash_password(pwd)
    if os.path.exists(USERPATH):
        with open(USERPATH, "r") as f:
            for linje in f:
                if "," in linje:
                    u, _ = linje.strip().split(",")
                    if user == u:
                        return False
    with open(USERPATH, "a") as f:
        f.write(f"{user},{hashed_pwd}\n")
    return True

def cmdsend(cmd: str) -> bool:
    client.sendall(cmd.encode())