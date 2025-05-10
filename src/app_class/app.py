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
    from src.const import DICO_PATH, HEIGHT, WIDTH
    from src.app_class.data import Data
    from screeninfo import get_monitors
    from pyautogui import position
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

    def setup_size(self, app):
        monitor = get_mouse_monitor()
        x = monitor.x + (monitor.width // 2) - (WIDTH // 2)
        y = monitor.y + (monitor.height // 2) - (HEIGHT // 2)
        app.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

    def setup_grid(self, app, cols, rows):
        for i in range(cols):
            app.grid_columnconfigure(i, weight=1)
        for i in range(rows + 1):
            app.grid_rowconfigure(i, weight=1)

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
