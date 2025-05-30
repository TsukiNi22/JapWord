#!/bin/env python3
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
##  JapWord.py

File Description:
## Main file of the mini application JapWord
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Requirements """
from src.requirements import requirements
requirements()

""" Import """
try:
    from src.app_class.app import JapWord
    from src.app_class.data import DataType, Data
    from src.app import launch_app
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Program """
if __name__ != "__main__":
    print("JapWord is not a module!")
    exit(1)

# app initialisation
app = JapWord()
app.getdico()

# start the app
launch_app(app)

#app.dico.append(Data(DataType.Word.value, "Debut", "kara", "から", "カラ"))
# save of modif
app.savedico()
