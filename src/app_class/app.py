"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  10/05/2025 by Tsukini

File Name:
##  app.py

File Description:
## Class of the mini application
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from src.const import DICO_PATH
    from src.app_class.data import Data
    from src.windows import learning_window
    from screeninfo import get_monitors
    from pyautogui import position
    from random import shuffle
    from json import load, dump
    from os import path
    import customtkinter as ctk

except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Class """
class JapWord():

    def __init__(self):
        self.dico = []

    def setup_size(self, app, width, height):
        monitor = get_mouse_monitor()
        x = monitor.x + (monitor.width // 2) - (width // 2)
        y = monitor.y + (monitor.height // 2) - (height // 2)
        app.geometry(f"{width}x{height}+{x}+{y}")

    def setup_grid(self, app, cols, rows):
        for i in range(cols * 2):
            app.grid_columnconfigure(i, weight=1 * ((i + 1) % 2))
        app.grid_rowconfigure(1, weight=1)
        for i in range(rows + 1 + 1):
            app.grid_rowconfigure(i, weight=1)

    def on_choice(self, category, action):
        match category:
            case "Alphabet":
                self.list = [data for data in self.dico if (getattr(data, "Letter", False) == True)]
            case "Kanji":
                self.list = [data for data in self.dico if (getattr(data, "Kanji", False) == True)]
            case "Word":
                self.list = [data for data in self.dico if (getattr(data, "Word", False) == True)]
            case _:
                print(f"Unknow category: {category}\n")
                return
        shuffle(self.list)
        self.learning_i = 0
        learning_window(self, category, action)

    def getdico(self):
        if (not path.exists(DICO_PATH)):
            return
        with open(DICO_PATH, "r", encoding="utf-8") as f:
            dico = load(f)
            for js_data in dico:
                data = Data(0)
                data.setdico(js_data)
                self.dico.append(data)

    def savedico(self):
        with open(DICO_PATH, "w", encoding="utf-8") as f:
            dico = []
            for data in self.dico:
                dico.append(data.getdico())
            dump(dico, f, indent=4)

def get_mouse_monitor():
    mouse_x, mouse_y = position()
    for monitor in get_monitors():
        if (monitor.x <= mouse_x <= monitor.x + monitor.width and
            monitor.y <= mouse_y <= monitor.y + monitor.height):
            return monitor
    return get_monitors()[0]
