"""''Si Vicem Pacem, Para Bellum - If you want peace, prepare for war'' \n 
PARABELLUM is an advanced networked tool that provides a comprehensive suite of features to make defensive and offensive actions easier for millitary/law enforcement. It is designed to assist military and law enforcement officers in identifying, assessing and engaging threatening forces and entities."""

import os, sys, time, hashlib
import ttkbootstrap as ttk
from ttkbootstrap import *
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import *
import tkintermapview as mv
import parabellum_.parabellumclient_.sysinfo as sinf

FILEPATH = f"python_\\parabellum_\\parabellum.py"
USERPATH = f"python_\\parabellum_\\users.txt"

CLASSIFICATIONS = sinf.CLASSIFICATIONS

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def login(user, pwd):
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
def signup(user, pwd):
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


