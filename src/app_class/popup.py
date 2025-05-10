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
##  popup.py

File Description:
## Popup for information
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    import customtkinter as ctk
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Class """
class PopUp(ctk.CTkToplevel):
    
    def __init__(self, app, title, message, whidth, height):
        super().__init__(app.JapWord)
        # init of the learning window
        self.title(title)
        app.setup_size(self, whidth, height)
        self.resizable(False, False)
        self.transient(app.JapWord)

        # Message
        label = ctk.CTkLabel(self, text=message, font=("Courier", 15), justify="left")
        label.pack(expand=True, fill="both", padx=10, pady=20)

        # Bouton 'OK'
        ok_button = ctk.CTkButton(self, text="Ok", command=self.destroy)
        ok_button.pack(side="bottom", fill="x", padx=0, pady=0)

        self.wait_window()
