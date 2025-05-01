import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import hashlib
import os

def hash_passord(passord):
    return hashlib.sha256(passord.encode()).hexdigest()
def login(email, pwd):
    hashed_input = hash_passord(pwd)
    try:
        with open("tangocred.txt", "r") as f:
            for linje in f:
                if "," not in linje:
                    continue
                deler = linje.strip().split(",")
                if len(deler) != 2:
                    continue
                lagret_email, lagret_hash = deler
                if email == lagret_email and hashed_input == lagret_hash:
                    return True
        return False 
    except FileNotFoundError:
        return False
def signup(email, pwd):
    hashed_pwd = hash_passord(pwd)
    if os.path.exists("tangocred.txt"):
        with open("tangocred.txt", "r") as f:
            for linje in f:
                if "," not in linje:
                    continue
                deler = linje.strip().split(",")
                if len(deler) != 2:
                    continue
                lagret_email = deler[0]
                if email == lagret_email:
                    return False
    with open("tangocred.txt", "a") as f:
        f.write(f"{email},{hashed_pwd}\n")
    return True

class TANGOApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TANGO I")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))
        self.configure(bg="#1e1e1e")
        self.frames = {}

        container = tk.Frame(self, bg="#1e1e1e")
        container.pack(fill="both", expand=True)

        for F in (loginpage, dashboard, MISCON, MAP, STATUS, COMM, USER):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame(loginpage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

class loginpage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#1e1e1e")
        self.controller = controller

        label = tk.Label(self, text="T.A.N.G.O. login", font=("", 24), bg="#1e1e1e", fg="#e0e0e0")
        label.pack(pady=20)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self, text="Username", bg="#1e1e1e", fg="#e0e0e0").pack()
        tk.Entry(self, textvariable=self.username, bg="#2d2d2d", fg="#e0e0e0", insertbackground="white").pack(pady=5)

        tk.Label(self, text="Password", bg="#1e1e1e", fg="#e0e0e0").pack()
        tk.Entry(self, show="*", textvariable=self.password, bg="#2d2d2d", fg="#e0e0e0", insertbackground="white").pack(pady=5)

        frame = tk.Frame(self, bg="#1e1e1e")
        frame.pack(pady=20)

        btn_style = {"bg": "#2d2d2d", "fg": "white", "activebackground": "#3d3d3d", "activeforeground": "#00ffcc"}

        tk.Button(frame, text="Login", command=self.log_in, **btn_style).grid(row=0, column=0, padx=10)
        tk.Button(frame, text="Sign Up", command=self.sign_up, **btn_style).grid(row=0, column=1, padx=10)

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
class dashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#1e1e1e")
        self.controller = controller

        tk.Label(self, text="TANGO I Dashboard", font=("Arial", 24), bg="#1e1e1e", fg="#e0e0e0").pack(pady=20)
        frame = tk.Frame(self, bg="#1e1e1e")
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        btn_style = {"bg": "#2d2d2d", "fg": "white", "activebackground": "#3d3d3d", "activeforeground": "#00ffcc"}

        buttons = [
            ("Mission Control", MISCON, 0, 0),
            ("Map", MAP, 0, 1),
            ("Status", STATUS, 0, 2),
            ("Communications", COMM, 1, 0),
            ("User Management", USER, 1, 2)
        ]

        frame.columnconfigure((0, 2), weight=1)
        frame.columnconfigure(1, weight=2)
        frame.rowconfigure((0, 1, 2), weight=1)

        for text, page, r, c in buttons:
            tk.Button(frame, text=text, command=lambda p=page: controller.show_frame(p), **btn_style).grid(row=r, column=c, sticky="nsew", padx=10, pady=10)

        cmdsect = tk.Frame(self, bg="#1e1e1e")
        cmdsect.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        cmdsect.rowconfigure(0, weight=1)
        exitbtn = tk.Button(cmdsect, text="Exit", command=self.controller.quit, **btn_style)
        logout = tk.Button(cmdsect, text="Logout", command=lambda: controller.show_frame(loginpage), **btn_style)      
        settings = tk.Button(cmdsect, text="Settings", command=lambda: messagebox.showinfo("Settings", "Settings not implemented yet."), **btn_style)
        exitbtn.grid(row=0, column=0, padx=10, pady=10)
        logout.grid(row=0, column=1, padx=10, pady=10)
        settings.grid(row=0, column=2, padx=10, pady=10)
        cmdsect.pack(fill="x", anchor="s", padx=5, pady=5)
        
class tangobp(tk.Frame):
    def __init__(self, parent, controller, title):
        super().__init__(parent, bg="#1e1e1e")
        self.controller = controller
        tk.Label(self, text=title, font=("Arial", 24), bg="#1e1e1e", fg="#e0e0e0").pack(pady=20)
        tk.Button(self, text="< back", bg="#2d2d2d", fg="white", activebackground="#3d3d3d", activeforeground="#00ffcc", command=lambda: controller.show_frame(dashboard)).pack(pady=10)

class MISCON(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Mission Control")

        misconpanel = tk.Frame(self, bg="#1e1e1e")
        misconpanel.columnconfigure((0, 1, 2, 3), weight=1)
        misconpanel.rowconfigure((0, 1, 2), weight=1)

        state = self.get_state()
        mission_data = self.get_mission_data()

        misconstate = tk.Label(misconpanel, text=f"State: {state}", bg="#1e1e1e", fg="#e0e0e0", bd=2, relief="solid", padx=10, pady=5)
        misconstate.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        miscondata = tk.Label(misconpanel, text=f"Mission Data: {mission_data}", bg="#1e1e1e", fg="#e0e0e0", bd=2, relief="solid", padx=10, pady=5)
        miscondata.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
    



        misconpanel.pack(expand=True, fill="both", padx=20, pady=20)



    def get_state(self):
        # Placeholder for actual state retrieval logic
        return "No active missions"
    def get_mission_data(self):
        # Placeholder for actual mission data retrieval logic
        return "No mission data available"
    
class MAP(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Map")
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
    app = TANGOApp()
    app.mainloop()