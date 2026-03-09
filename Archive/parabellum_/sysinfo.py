
import socket
import hashlib
import os

CLASSIFICATIONS = {
    1: "Public",
    2: "Restricted",
    3: "Classified",
    4: "Secret",
    5: "Top Secret",
    6: "Above Top Secret",
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

class NotConnectedError(Exception):
    """Exception for failed and methods/functions called while offline/not connected"""
    pass
class NoReplyError(Exception):
    """Exception for when the server does not acknowledge cmdsend()"""
    pass
class FalseCredError(Exception):
    """Exception for incorrect username or password in login protocol"""
    pass

SERVER_IP: str
USERPATH: str
PORT: int
Connected: bool
client: socket.socket

class MISSION:
    def LOAD():
        pass
    def INIT():
        pass
    def NEW():
        pass
    def EDIT():
        pass
class USER:
    def NEW(self, user: str="", password: str="") -> bool | Exception:
        if Connected:
            cmdsend(f"USER NEW {user} {hash_password(password)}")
            data = client.recv(1024).decode()
            if data.startswith("ACK"):
                return True
            elif not data:
                return NoReplyError
        else:
            return NotConnectedError
    def LOGIN(self, user: str="", password: str="") -> bool | Exception:
        if Connected: 
            cmdsend(f"USER LOGIN {user} {password}")
            data = client.recv(1024).decode()
            if data.startswith("ACK"):
                return True
            elif data.startswith("NOT"):
                return FalseCredError
            elif not data:
                return NoReplyError
        else:
            return NotConnectedError


    def DELETE(self, user: str="") -> bool | Exception:
        if Connected:
            cmdsend(f"USER DELETE {user}")
            data = client.recv(1024).decode()
            if data.startswith("ACK"):
                return True
            elif not data: 
                return NoReplyError
        else:
            return NotConnectedError 
class SYSTEM:
    def RESTART():
        pass #IDK

class MISSIONR:
    def LOAD():
        pass
    def ACTIVATE():
        pass
    def NEW():
        pass
    def EDIT():
        pass
class USERR:
    def NEW():
        pass    
    def LOGIN():
        pass
    def DELETE():
        pass
class SYSTEMR:
    def RESTART():
        pass

classdict = {
    "MISSION": MISSION,
    "USER": USER,
    "SYSTEM": SYSTEM,
    "MISSIONR": MISSIONR,
    "USERR": USERR,
    "SYSTEMR": SYSTEMR,

}

def serverconnect(ip: str, port: int) -> (tuple[socket.socket, bool]) | (tuple[None, bool]):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip, port))
        print("[CLIENT] Tilkoblet.")
        return client, True
    except (ConnectionRefusedError, TimeoutError) as e:
        print(f"[CLIENT] Tilkobling feilet: {e}")
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

def cmdsend(cmd: str) -> str | Exception:
    client.sendall(cmd.encode())
    reply: str = client.recv(1024).decode()
    return reply

def cmdRPER(cmd: str, user: str) -> tuple[bool, str] | tuple[bool, Exception]:
    """Command RPER (Receive, Parse, Execute, Reply)"""
    try:
        cmdclass_name, method_name, *args = cmd.strip().split(" ")

        cmdclass = classdict.get(cmdclass_name.upper())
        if not cmdclass:
            raise ValueError(f"Ukjent kommando: {cmdclass_name}")
        
        method = getattr(cmdclass, method_name, None)
        if not callable(method):
            raise ValueError(f"Ukjent metode: {method_name} for {cmdclass_name}")

        # Fyll på med None hvis args mangler
        max_expected_args = method.__code__.co_argcount - 2 # self og user
        padded_args = args + [None] * (max_expected_args - len(args))

        result = method(user, *padded_args)
        print(f"[{user}] EXECUTING: ",result)
        return (True, str(result))


    except Exception as e:
        return (False, e)

    


