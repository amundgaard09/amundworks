"""''Si Vicem Pacem, Para Bellum - If you want peace, prepare for war'' \n 
PARABELLUM is an advanced networked tool that provides a comprehensive suite of features to make defensive and offensive actions easier for millitary/law enforcement. It is designed to assist military and law enforcement officers in identifying, assessing and engaging threatening forces and entities."""

import locale
try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    pass 

import os, sys, time, hashlib
import ttkbootstrap as ttk
from ttkbootstrap import *
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import *
import tkintermapview as tkmv
import python_.parabellum_.sysinfo as sinf
import socket

CLASSIFICATIONS = sinf.CLASSIFICATIONS
FILEPATH = str(f"python_\\parabellum_\\parabellumclient\\parabellum.py")
SERVER_IP = str(f"192.168.0.141")  # IP = Server PC IP
PORT = 5000

client, Connected = sinf.serverconnect(SERVER_IP, PORT)

class parabellumcontroller(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("TANGO I")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))
        self.frames = {}

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        for F in (): # frames
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame() # login

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

while Connected:
    msg = input("Send melding: ")
    client.sendall(msg.encode())
    data = client.recv(1024).decode()
    print(f"[SERVER SVAR] {data}")



