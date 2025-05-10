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
## Main loop of the app
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    import customtkinter as ctk
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

def launch_app(app):
    # setup theme
    ctk.set_appearance_mode("dark")  # dark | light
    ctk.set_default_color_theme("dark-blue")  # blue | green | dark-blue

    # init the window
    app.JapWord = ctk.CTk()
    app.JapWord.title("JapWord App")
    app.JapWord.geometry("400x300")

    # testing
    label = ctk.CTkLabel(app.JapWord, text="Hello, CustomTkinter!", font=("Arial", 20))
    label.pack(pady=20)
    bouton = ctk.CTkButton(app.JapWord, text="Fermer", command=app.JapWord.destroy)
    bouton.pack(pady=10)

    # loop to keep open the window
    app.JapWord.mainloop()
