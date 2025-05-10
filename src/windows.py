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
    from src.app_class.popup import PopUp
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
        if (len(app.list) == 0):
            PopUp(app, "Information", "The list of data is empty!!!", 300, 150)
            return
        app.learning_i = 0

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
        message =  f"{'Type':<10} -> {'Your Answer':<20} | Real Answer\n"
        message += "-" * 48 + "\n"
        message += f"{'French':<10} -> {ouput['fr']:<20} | {app.list[app.learning_i].fr}\n"
        message += f"{'Romanji':<10} -> {ouput['ro']:<20} | {app.list[app.learning_i].ro}\n"
        message += f"{'Katakana':<10} -> {ouput['kana']:<20} | {app.list[app.learning_i].kana}\n"
        message += f"{'Hiragana':<10} -> {ouput['hira']:<20} | {app.list[app.learning_i].hira}\n"
        message += f"{'Kanji':<10} -> {ouput['kanji']:<20} | {app.list[app.learning_i].kanji}"
        
        PopUp(app, "🡳 Awnser 🡳", message, 750, 200)
        app.learning_i += 1
        learning_window(app, category, action)

