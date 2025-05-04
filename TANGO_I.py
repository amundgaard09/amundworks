# TACTICAL AEROSPACE NETWORKED GLOBAL OPERATOR

import locale
try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    pass 

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkintermapview import TkinterMapView
import hashlib
import time
import ast
import os

class NoMissionError(Exception):
    pass
class FileAlreadyExistsError(Exception):
    pass
class DupedMissionIDError(Exception):
    pass

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
def add_placeholder(entry: tb.Entry, placeholder: str):
    entry.insert(0, placeholder)
    entry.config(foreground="gray")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(foreground="black")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(foreground="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def getmissioninfo(missionid: str) -> list:
    if os.path.exists(f"tango_missions.txt"):
        with open(f"tango_missions.txt", "r") as mis:
            for line in mis:
                if line.startswith(f"{missionid}|"):
                    missionid: str
                    misloc: tuple
                    markers: dict
                    missionid, mistitle, misloc, misstart, misend, desc, goal, missionstat, markers = line.strip().split("|")
                    misdur = (misstart, misend)
                    mislon, mislat = misloc.strip().split(",")
                    misloc = (mislat, mislon)
                    markers = ast.literal_eval(markers) if markers else {}
                    return mistitle, misloc, misdur, desc, goal, missionstat, markers
        raise NoMissionError
    else:
        messagebox.showerror("Error", "No mission folder found")
        raise FileNotFoundError     
def makemission(missionid: str, title: str, location: tuple, start: str, end: str, desc: str, goal: str, markers: dict | None) -> bool:
    missionstat = "Inactive"
    if os.path.exists("tango_missions.txt"):
        with open("tango_missions.txt", "r") as mis:
            for line in mis:
                if line.startswith(f"{missionid}|"):
                    raise DupedMissionIDError
        
        with open("tango_missions.txt", "a") as mis:
            mis.write("\n")
            mis.write(f"{missionid}|{title}|{location[0]},{location[1]}|{start}|{end}|{desc}|{goal}|{missionstat}|{str(markers)}")
            return True
    else:
        messagebox.showerror("Error", "No mission file found - Make a new file")
        raise FileNotFoundError
def makemissionfolder() -> bool:
    if os.path.exists("tango_missions.txt"):
        raise FileAlreadyExistsError("Mission file already exists.")
    else:
        with open("tango_missions.txt", "w") as f:
            f.write("")
            return True

def deacmission(missionid: str) -> bool: ##
    pass
def actimission(missionid: str) -> bool: ##
    pass
def endmission(missionid: str)  -> bool: ##
    pass
def editmission(missionid: str) -> bool: ##
    pass

class TANGOApp(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("TANGO I")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))
        self.frames = {}

        container = tb.Frame(self)
        container.pack(fill="both", expand=True)

        for F in (loginpage, dashboard, MISCON, MISCREATOR, MISVIEWER, MAP, STATUS, COMM, USER):
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

        header = tb.Frame(self, bootstyle=SECONDARY)
        header.pack(fill="x", padx=20, pady=(20, 10))

        tb.Label(header, text=label_text, style="secondary.inverse.tlabel", font=("Arial", 20)).pack(side="left", padx=10, pady=10)
        tb.Button(header, text="← Return", command=lambda: controller.show_frame(dashboard), bootstyle=(LIGHT, OUTLINE)).pack(side="right", padx=10, pady=10)

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

        tb.Label(self, text="TANGO I Dashboard", font=("Arial", 20), bootstyle="secondary-inverse", anchor="center").pack(pady=30, fill="both", padx=20)

        frame = tb.Frame(self)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        frame.rowconfigure((0, 1), weight=4)
        frame.rowconfigure(2, weight=2)
        frame.rowconfigure(3, weight=1)
        frame.columnconfigure((0, 2), weight=1)
        frame.columnconfigure(1, weight=2)                                              

        tb.Button(frame,text="Communications", command=lambda:controller.show_frame(COMM),      bootstyle=(SECONDARY,OUTLINE)).grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
        tb.Button(frame,text="Map",            command=lambda:controller.show_frame(MAP),       bootstyle=(SECONDARY,OUTLINE)).grid(row=0,column=1,sticky="nsew",padx=10,pady=10,rowspan=2)
        tb.Button(frame,text="Status",         command=lambda:controller.show_frame(STATUS),    bootstyle=(SECONDARY,OUTLINE)).grid(row=0,column=2,sticky="nsew",padx=10,pady=10)
        tb.Button(frame,text="Mission Control",command=lambda:controller.show_frame(MISCON),    bootstyle=(SECONDARY,OUTLINE)).grid(row=1,column=0,sticky="nsew",padx=10,pady=10)
        tb.Button(frame,text="User Management",command=lambda:controller.show_frame(USER),      bootstyle=(SECONDARY,OUTLINE)).grid(row=1,column=2,sticky="nsew",padx=10,pady=10)
        tb.Button(frame,text="Mission Creator",command=lambda:controller.show_frame(MISCREATOR),bootstyle=(SECONDARY,OUTLINE)).grid(row=2,column=0,sticky="nsew",padx=10,pady=10)
        tb.Button(frame,text="Mission Viewer", command=lambda:controller.show_frame(MISVIEWER), bootstyle=(SECONDARY,OUTLINE)).grid(row=3,column=0,sticky="nsew",padx=10,pady=10)

        command = tb.Frame(self)
        command.pack(fill="x", padx=20, pady=10)
        for i in range(10):
            command.columnconfigure(i, weight=1)

        tb.Button(command,text="Exit",    command=controller.quit,                                                   bootstyle=(DANGER,   OUTLINE)).grid(row=0,column=0,sticky="ew",padx=10)
        tb.Button(command,text="Logout",  command=lambda:controller.show_frame(loginpage),                           bootstyle=(WARNING,  OUTLINE)).grid(row=0,column=1,sticky="ew",padx=10)
        tb.Button(command,text="Settings",command=lambda:messagebox.showinfo("Settings","Settings not implemented."),bootstyle=(SECONDARY,OUTLINE)).grid(row=0,column=2,sticky="ew",padx=10)

class MISCON(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Mission Control")

        self.mistitle = tb.StringVar(value="")
        self.misloc   = tb.StringVar(value="")
        self.misdur   = tb.StringVar(value="")
        self.desc     = tb.StringVar(value="")
        self.goal     = tb.StringVar(value="")
        self.misstat  = tb.StringVar(value="")
        self.pois     = tb.StringVar(value="POIS:\nNone")
        self.pois_dict = {}

        panel = tb.Frame(self)
        panel.pack(expand=True, fill="both", padx=20, pady=20)
        panel.columnconfigure((0, 1, 2, 3), weight=1)
        panel.rowconfigure((0, 1, 2,), weight=1)
        
        misinfdisplay = tb.Frame(panel, bootstyle = SECONDARY)
        misinfdisplay.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="news")
        misinfdisplay.rowconfigure(list(range(30)), weight=1)
        misinfdisplay.columnconfigure((0, 1, 2), weight=1)

        mismap = TkinterMapView(panel, width=800, height=600, corner_radius=0)
        mismap.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew", padx=10, pady=10)

        def create_new_mission():
            controller.show_frame(MISCREATOR)
        def create_new_folder():
            try:
                makemissionfolder()
            except FileAlreadyExistsError:
                messagebox.showerror("Error","Mission File already exists! \nMake a new Mission instead!")
        def load_mission():
            misid = misidentry.get()
            if not misid:
                messagebox.showerror("Error", "Missing Mission ID!")
                return
            try:
                mistitle, misloc, misdur, desc, goal, misstat, pois = getmissioninfo(misid)

                self.mistitle.set(f"Mission Info for {mistitle}")
                self.misloc.set(f"Location: {misloc[0]}, {misloc[1]}")
                self.misdur.set(f"Mission Duration: {misdur[0]} -> {misdur[1]}")
                self.desc.set(f"Description:\n{desc}")
                self.goal.set(f"Goal:\n{goal}")
                self.misstat.set(f"Mission Status:\n{misstat}")

                self.pois_dict = pois
                pois_text = "\n".join([f"{name}: ({lat}, {lon})" for name, (lat, lon) in pois.items()])
                self.pois.set(f"POIS:\n{pois_text}" if pois_text else "POIS:\nNone")
            except NoMissionError:
                messagebox.showerror("Error", "No Mission with given ID found!")
        def markplace():
            if not self.misloc.get():
                messagebox.showerror("Error","No Mission Loaded!\nLoad Mission First!")
                return
            else:
                try:
                    latlon = self.misloc.get().replace("Location: ", "").replace("(","").replace(")","").replace("'","").replace('"','')
                    lat, lon = map(float, latlon.split(","))
                    mismap.set_position(lat, lon)
                    mismap.set_marker(lat, lon, text=self.mistitle.get().replace("Mission Info for", ""))
                except (ValueError, IndexError):
                    messagebox.showerror("Error", "Invalid coordinates format.")
        def loadpois():
            if not hasattr(self, 'pois_dict') or not self.pois_dict:
                messagebox.showinfo("Info", "No POIs to load.")
                return

            for name, (lat, lon) in self.pois_dict.items():
                mismap.set_marker(lat, lon, text=name)
                mismap.set_position(lat,lon)

        misidentry = tb.StringVar()
        misid = tb.Entry(misinfdisplay, textvariable=misidentry)
        misid.grid(row=0, column=0, columnspan=2, padx=5, sticky="ew") 
        add_placeholder(misid, "Enter Mission ID")

        tb.Button(misinfdisplay, text="Load Mission With ID",command=load_mission,      bootstyle=(PRIMARY, OUTLINE)).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        tb.Button(misinfdisplay, text="Create New Mission",  command=create_new_mission,bootstyle=(SUCCESS, OUTLINE)).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        tb.Button(misinfdisplay, text="Create New Folder",   command=create_new_folder, bootstyle=(SUCCESS, OUTLINE)).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        tb.Button(misinfdisplay, text="Edit Mission",        command=editmission,       bootstyle=(WARNING, OUTLINE)).grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        tb.Button(misinfdisplay, text="Suspend Mission",     command=deacmission,       bootstyle=(WARNING, OUTLINE)).grid(row=28,column=0, padx=5, pady=5, sticky="ew",columnspan=3)
        tb.Button(misinfdisplay, text="End Mission",         command=endmission,        bootstyle=(DANGER,  OUTLINE)).grid(row=29,column=0, padx=5, pady=5, sticky="ew",columnspan=3)
        tb.Button(misinfdisplay, text="Mark Mission Site",   command=markplace,         bootstyle=(SUCCESS, OUTLINE)).grid(row=21,column=2, padx=5, pady=5, sticky="ew")
        tb.Button(misinfdisplay, text="Load POIs",           command=loadpois,          bootstyle=(INFO,    OUTLINE)).grid(row=26,column=2, padx=5, pady=5, sticky="ew")
        tb.Label(misinfdisplay, textvariable=self.mistitle).grid(row=20, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        tb.Label(misinfdisplay, textvariable=self.misloc  ).grid(row=21, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        tb.Label(misinfdisplay, textvariable=self.misdur  ).grid(row=22, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        tb.Label(misinfdisplay, textvariable=self.desc    ).grid(row=23, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        tb.Label(misinfdisplay, textvariable=self.goal    ).grid(row=24, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        tb.Label(misinfdisplay, textvariable=self.misstat ).grid(row=25, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        tb.Label(misinfdisplay, textvariable=self.pois    ).grid(row=26, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
class MISCREATOR(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Mission Creator")

        panel = tb.Frame(self, bootstyle=SECONDARY)
        panel.rowconfigure(list(range(30)), weight=1)
        panel.columnconfigure((0, 1, 2, 3), weight=1)
        panel.pack(expand=True, fill="both", padx=20, pady=20)

        map = TkinterMapView(panel, width=800, height=600, corner_radius=0)
        map.grid(row=0, column=1, rowspan=30, columnspan=3, sticky="news", padx=10, pady=10)

        self.markerdict = {}

        misid     = tb.Entry(panel)
        title     = tb.Entry(panel)
        mislat    = tb.Entry(panel)
        mislon    = tb.Entry(panel)
        misstart  = tb.Entry(panel)
        misend    = tb.Entry(panel)
        misdesc   = tb.Entry(panel)
        misgoal   = tb.Entry(panel)
        markloc   = tb.Entry(panel)
        marknam   = tb.Entry(panel)

        misid.grid(   row=1,column=0,sticky="ew",padx=5,pady=5)
        title.grid(   row=2,column=0,sticky="ew",padx=5,pady=5)
        mislat.grid(  row=3,column=0,sticky="ew",padx=5,pady=5)
        mislon.grid(  row=4,column=0,sticky="ew",padx=5,pady=5)
        misstart.grid(row=5,column=0,sticky="ew",padx=5,pady=5)
        misend.grid(  row=6,column=0,sticky="ew",padx=5,pady=5)
        misdesc.grid( row=7,column=0,sticky="ew",padx=5,pady=5)
        misgoal.grid( row=8,column=0,sticky="ew",padx=5,pady=5)
        marknam.grid( row=9,column=0,sticky="ew",padx=5,pady=5)
        markloc.grid(row=10,column=0,sticky="ew",padx=5,pady=5)
        
        add_placeholder(misid,    "Mission ID")
        add_placeholder(title,    "Mission Title")
        add_placeholder(mislat,   "Mission Location Latitude")
        add_placeholder(mislon,   "Mission Location Longitude")
        add_placeholder(misstart, "Mission Start Date eg. '01.01.2025'")
        add_placeholder(misend,   "Mission End Date eg. '01.01.2025'")
        add_placeholder(misdesc,  "Mission Description")
        add_placeholder(misgoal,  "Mission Goal")
        add_placeholder(marknam,  "Enter Mission Marker Name (optional)")
        add_placeholder(markloc,  "Enter Mission Marker Coordinates (optional)")

        def savemismark_():
            loc_str = markloc.get()
            name = marknam.get()
            if not name or not loc_str or name.isspace() or loc_str.isspace():
                messagebox.showerror("Error", "Marker name and coordinates are required.")
                return
            try:
                cleaned = loc_str.replace("(", "").replace(")", "").replace("'", "")
                lat_str, lon_str = cleaned.split(",")
                lat, lon = float(lat_str.strip()), float(lon_str.strip())

                if name in self.markerdict:
                    overwrite = messagebox.askyesno("Overwrite?", f"Marker '{name}' already exists. Overwrite?")
                    if not overwrite:
                        return

                self.markerdict[name] = (lat, lon)

            except (ValueError, TypeError):
                messagebox.showerror("Error", "Invalid marker coordinates! Use format: lat, lon")

        def savemission():
            if all(entry.get().strip() for entry in [misid, title, mislat, mislon, misstart, misend, misdesc, misgoal]):
                try:
                    misloc: tuple[float, float] = (float(mislat.get()), float(mislon.get()))
                    if makemission(misid.get(), title.get(), misloc, misstart.get(), misend.get(), misdesc.get(), misgoal.get(), self.markerdict):
                        messagebox.showinfo("Success!",f"Created new Mission {title.get()}")
                except DupedMissionIDError:
                    messagebox.showerror("Error","Mission ID already in use!")
            else:
                messagebox.showerror("Error", "Please fill in all forms!")
        def marklocation():
            if mislat.get() == "Mission Location Latitude" or mislon.get() == "Mission Location Longitude":
                messagebox.showerror("Error","Cannot mark with empty coordinates")
            else:
                lat = float(mislat.get())
                lon = float(mislon.get())
                map.set_position(lat, lon)
                map.set_marker(lat, lon, text=title.get())

        save     = tb.Button(panel,text="Save & Create Mission",command=savemission, bootstyle=SUCCESS)
        mark     = tb.Button(panel,text="Mark Mission Location",command=marklocation,bootstyle=(SUCCESS,OUTLINE))
        savemark = tb.Button(panel,text="Save Mission Marker",  command=savemismark_, bootstyle=(SUCCESS,OUTLINE))
        save.grid(    row=29,column=0,padx=5,pady=5,sticky="ew")
        mark.grid(    row=28,column=0,padx=5,pady=5,sticky="ew")   
        savemark.grid(row=27,column=0,padx=5,pady=5,sticky="ew")
class MISVIEWER(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Mission Viewer")

        mainpanel = tb.Frame(self, bootstyle=DARK)
        mainpanel.rowconfigure((0, 1, 2), weight=1)    
        mainpanel.columnconfigure((0, 1, 2, 3), weight=1)
        mainpanel.pack(expand=True, fill="both", padx=20, pady=20)

        sidebar = tb.Frame(mainpanel, bootstyle=SECONDARY)
        sidebar.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="news")
        sidebar.rowconfigure((list(range(30))), weight=1)
        sidebar.columnconfigure((0, 1), weight=1)

        #tb.Scrollbar(sidebar, bootstyle="info-round", orient="horizontal")
        mission_frames = []

        
        if os.path.exists(f"tango_missions.txt"):
            with open(f"tango_missions.txt", "r") as mis:
                counter = 1
                for line in mis:
                    if line == "":
                        continue
                    else:
                        missionid, mistitle, misloc, misstart, misend, desc, goal, missionstat, markers = line.strip().split("|")
                        frame = tb.Frame(sidebar, bootstyle=PRIMARY)
                        frame.grid(row=counter, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
                        tb.Label(frame, text=f"{mistitle} - {missionid}", bootstyle="inverse-primary").pack(padx=5, pady=5)

                        mission_frames.append(frame)
                        counter += 1
        else:
            messagebox.showerror("Error", "No mission folder found")
            raise FileNotFoundError  



class MAP(tangobp):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Map")

        mappage = tb.Frame(self)
        mappage.pack(expand=True, fill="both", padx=20, pady=20)

        mappage.rowconfigure((0, 1, 2), weight=1)
        mappage.columnconfigure((0, 1, 2, 3), weight=1)

        sidebar = tb.Frame(mappage)
        sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)
        sidebar.rowconfigure(list(range(30)), weight=1)
        sidebar.columnconfigure((0, 1), weight=1)

        tb.Label(sidebar, text="Map Controls", relief="solid", borderwidth=2, anchor="center").grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        tb.Label(sidebar, text="Latitude", borderwidth=2,).grid(row=1, column=0, padx=10, pady=5)
        tb.Label(sidebar, text="Longitude").grid(row=1, column=1, padx=10, pady=5)

        lat_entry = tb.Entry(sidebar)
        lon_entry = tb.Entry(sidebar)
        lat_entry.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        lon_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        map = TkinterMapView(mappage, width=800, height=600, corner_radius=0)
        map.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew", padx=10, pady=10)

        markername = tb.StringVar()
        markernameentry = tb.Entry(sidebar, textvariable=markername)
        markernameentry.grid(row=3, columnspan=2, padx=10, pady=5, sticky="ew")

        def mark_position():
            try:
                lat = float(lat_entry.get())
                lon = float(lon_entry.get())
                map.set_position(lat, lon)
                map.set_marker(lat, lon, text=markername.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid latitude or longitude.")

        tb.Button(sidebar, text="Mark Position", command=mark_position,         bootstyle=SUCCESS).grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="news")
        tb.Button(sidebar, text="Clear Markers", command=map.delete_all_marker, bootstyle=WARNING).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="news")
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