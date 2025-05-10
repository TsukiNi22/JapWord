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
    from src.app_class.data import Data
    from src.const import DICO_PATH
    from json import load, dump
    from os import path
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Class """
class JapWord():

    def __init__(self):
        self.dico = []

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
