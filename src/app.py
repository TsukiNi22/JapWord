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
    from src.const import CATEGORIES, ACTION, HEIGHT, WIDTH
    from src.windows import choice_window
    import customtkinter as ctk
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Program """
def launch_app(app):
    # setup theme
    ctk.set_appearance_mode("dark")  # dark | light
    ctk.set_default_color_theme("dark-blue")  # blue | green | dark-blue

    # init the window
    app.JapWord = ctk.CTk()
    app.JapWord.title("JapWord App")
    app.setup_size(app.JapWord, WIDTH, HEIGHT)
    app.setup_grid(app.JapWord, len(CATEGORIES), len(ACTION))
    app.JapWord.resizable(False, False)

    # call the main window
    choice_window(app)

    # loop to keep open the window
    app.JapWord.mainloop()
