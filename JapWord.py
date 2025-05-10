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

""" Import """
try:
    from src.app_class.app import JapWord
    from src.app_class.data import DataType, Data
    from src.requirements import requirements
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Program """
if __name__ != "__main__":
    print("JapWord is not a module!")
    exit(1)

# requirements
requirements()

# app
app = JapWord()

app.getdico()
app.dico.append(Data(DataType.Word.value, "Debut", "kara", "から", "カラ"))
app.savedico()
