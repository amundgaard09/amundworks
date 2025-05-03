# TACTICAL AEROSPACE NETWORKED GLOBAL OPERATOR


import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkintermapview import TkinterMapView
import hashlib
import os
import locale

def hash_passord(passord):
    return hashlib.sha256(passord.encode()).hexdigest()
def login(email, pwd):
    hashed_input = hash_passord(pwd)
    try:
        with open("tangocred.txt", "r") as f:
            for linje in f:
                if "," in linje:
                    e, h = linje.strip().split(",")
                    if email == e and hashed_input == h:
                        return True
    except FileNotFoundError:
        pass
    return False
def signup(email, pwd):
    hashed_pwd = hash_passord(pwd)
    if os.path.exists("tangocred.txt"):
        with open("tangocred.txt", "r") as f:
            for linje in f:
                if "," in linje:
                    e, _ = linje.strip().split(",")
                    if email == e:
                        return False
    with open("tangocred.txt", "a") as f:
        f.write(f"{email},{hashed_pwd}\n")
    return True

class TANGOApp(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("TANGO I")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))
        self.frames = {}

        container = tb.Frame(self)
        container.pack(fill="both", expand=True)

        for F in (loginpage, dashboard, MISCON, MAP, STATUS, COMM, USER):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame(loginpage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

class tangobp(tb.Frame):
    def __init__(self, parent, controller, label_text):
        super().__init__(parent)
        self.controller = controller

        header = tb.Frame(self)
        header.pack(fill="x", padx=20, pady=(20, 10))

        tb.Label(header, text=label_text, font=("Arial", 20)).pack(side="left", padx=10, pady=10)
        tb.Button(header, text="← Return", command=lambda: controller.show_frame(dashboard), bootstyle=SECONDARY).pack(side="right", padx=10, pady=10)

class loginpage(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tb.Label(self, text="T.A.N.G.O. login", font=("", 24)).pack(pady=20)

        self.username = tb.StringVar()
        self.password = tb.StringVar()

        tb.Label(self, text="Username").pack()
        tb.Entry(self, textvariable=self.username).pack(pady=5)

        tb.Label(self, text="Password").pack()
        tb.Entry(self, show="*", textvariable=self.password).pack(pady=5)

        frame = tb.Frame(self)
        frame.pack(pady=20)

        tb.Button(frame, text="Login", command=self.log_in, bootstyle=PRIMARY).grid(row=0, column=0, padx=10)
        tb.Button(frame, text="Sign Up", command=self.sign_up, bootstyle=SECONDARY).grid(row=0, column=1, padx=10)

    def log_in(self):
        email = self.username.get()
        pwd = self.password.get()
        if email and pwd:
            if login(email, pwd):
                self.controller.show_frame(dashboard)
            else:
                messagebox.showerror("Error", "Invalid email or password.")
        else:
            messagebox.showerror("Error", "Please enter both email and password.")

    def sign_up(self):
        email = self.username.get()
        pwd = self.password.get()
        if email and pwd:
            if signup(email, pwd):
                messagebox.showinfo("Success", "Registration successful. Please log in.")
                self.username.set("")
                self.password.set("")
            else:
                messagebox.showerror("Error", "Email already registered.")
        else:
            messagebox.showerror("Error", "Please enter both email and password.")

class dashboard(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tb.Label(self, text="TANGO I Dashboard", font=("Arial", 24)).pack(pady=20)
        frame = tb.Frame(self)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        buttons = [
            ("Mission Control", MISCON, 0, 0, 1),
            ("Map", MAP, 0, 1, 2),
            ("Status", STATUS, 0, 2, 1),
            ("Communications", COMM, 1, 0, 1),
            ("User Management", USER, 1, 2, 1)
        ]

        frame.rowconfigure((0, 1, 2), weight=1)
        frame.columnconfigure((0, 2), weight=1)
        frame.columnconfigure(1, weight=2)

        for text, page, r, c, span in buttons:
            tb.Button(frame, text=text, command=lambda p=page: controller.show_frame(p), bootstyle=INFO).grid(
                row=r, column=c, rowspan=span, sticky="nsew", padx=10, pady=10)

        footer = tb.Frame(self)
        footer.pack(fill="x", padx=20, pady=10)
        for i in range(3):
            footer.columnconfigure(i, weight=1)
        tb.Button(footer, text="Exit", command=controller.quit, bootstyle=DANGER).grid(row=0, column=0, padx=10)
        tb.Button(footer, text="Logout", command=lambda: controller.show_frame(loginpage), bootstyle=SECONDARY).grid(row=0, column=1, padx=10)
        tb.Button(footer, text="Settings", command=lambda: messagebox.showinfo("Settings", "Settings not implemented."), bootstyle=WARNING).grid(row=0, column=2, padx=10)

class MISCON(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Mission Control")
        panel = tb.Frame(self)
        panel.pack(expand=True, fill="both", padx=20, pady=20)

        tb.Label(panel, text="State: No active missions").pack(pady=10)
        tb.Label(panel, text="Mission Data: No mission data available").pack(pady=10)

class MAP(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Map")

        mappage = tb.Frame(self)
        mappage.pack(expand=True, fill="both", padx=20, pady=20)

        mappage.rowconfigure((0, 1, 2), weight=1)
        mappage.columnconfigure((0, 1, 2, 3), weight=1)

        sidebar = tb.Frame(mappage)
        sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)
        sidebar.rowconfigure(list(range(15)), weight=1)
        sidebar.columnconfigure((0, 1), weight=1)

        tb.Label(sidebar, text="Map Controls").grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        tb.Label(sidebar, text="Latitude").grid(row=1, column=0, padx=10, pady=5)
        lat_entry = tb.Entry(sidebar)
        lat_entry.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        tb.Label(sidebar, text="Longitude").grid(row=1, column=1, padx=10, pady=5)
        lon_entry = tb.Entry(sidebar)
        lon_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        map = TkinterMapView(mappage, width=800, height=600, corner_radius=0)
        map.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew", padx=10, pady=10)

        def mark_position():
            try:
                lat = float(lat_entry.get())
                lon = float(lon_entry.get())
                map.set_position(lat, lon)
                map.delete_all_marker()
                map.set_marker(lat, lon, text="Your Position")
            except ValueError:
                messagebox.showerror("Error", "Invalid latitude or longitude.")

        tb.Button(sidebar, text="Mark Position", command=mark_position, bootstyle=SUCCESS).grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

class STATUS(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Status")

class COMM(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Communications")

class USER(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "User Management")

if __name__ == "__main__":
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except locale.Error:
        pass 
    app = TANGOApp()
    app.mainloop()