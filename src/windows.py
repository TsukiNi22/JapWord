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
    from src.app_class.dialog import Dialog
    from random import choice
    import customtkinter as ctk
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)


""" Program """
def choice_window(app):
    # line parameter
    line_color = "grey"
    line_thickness = 2

    # nbumber of row and column
    total_cols = len(CATEGORIES)
    total_rows = len(ACTION)

    for col, category in enumerate(CATEGORIES):
        # double for the white line
        grid_col = col * 2

        # Category title
        label = ctk.CTkLabel(app.JapWord, text=category, font=("Arial", 18, "bold"))
        label.grid(row=0, column=grid_col, pady=(20, 10), sticky="n")

        # Button of the action
        for row, action in enumerate(ACTION, start=1):
            button = ctk.CTkButton(app.JapWord, text=action, command=lambda c=category, a=action: app.on_choice(c, a))
            button.grid(row=row + 1, column=grid_col, padx=10, pady=5)

        # Vertical line
        if col < total_cols - 1:
            sep = ctk.CTkFrame(app.JapWord, width=line_thickness, fg_color=line_color)
            sep.grid(row=0, column=grid_col + 1, rowspan=total_rows + 2, sticky="ns", padx=5)

    # line between the category and the action
    sep_h = ctk.CTkFrame(app.JapWord, height=line_thickness, fg_color=line_color)
    sep_h.grid(row=1, column=0, columnspan=2 * total_cols - 1, sticky="ew", pady=5)

def learning_window(app, category, action):
    if (app.learning_i >= len(app.list)):
        return

    if (action == "Fr → Jp" or (action == "Random" and choice([True, False]))):
        word = f"🡳 Translate '{app.list[app.learning_i].fr}' 🡳"
    else:
        word = "🡳 Translate 🡳\n"
        word += f"Romanji -> '{app.list[app.learning_i].ro}'\n"
        word += f"Katakana -> '{app.list[app.learning_i].kana}'\n"
        word += f"Hiragana -> '{app.list[app.learning_i].hira}'\n"
        word += f"Kanji -> '{app.list[app.learning_i].kanji}'"
    
    # init the learning window
    app.Learning = Dialog(app, f"{category} with {action}", word)
    ouput = app.Learning.show()

    # check the user input
    if ouput is None:
        return
    else:
        print(f"Entrée: {ouput}")
        app.learning_i += 1
        learning_window(app, category, action)

