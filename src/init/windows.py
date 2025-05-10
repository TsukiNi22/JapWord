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
##  windows.py

File Description:
##  Init different windows
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from src.const import CATEGORIES, ACTION
    import customtkinter as ctk
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)


""" Program """
def choice_window(app):
    
    # init labels
    for col, category in enumerate(CATEGORIES):
        # Titre de colonne
        label = ctk.CTkLabel(app.JapWord, text=category, font=("Arial", 18, "bold"))
        label.grid(row=0, column=col, pady=(20, 10), sticky="n")

        # Boutons pour chaque action
        for row, action in enumerate(ACTION, start=1):
            button = ctk.CTkButton(app.JapWord, text=action, command=lambda c=category, a=action: on_choice(c, a))
            button.grid(row=row, column=col, padx=10, pady=5)

def on_choice(category, action):
    pass
