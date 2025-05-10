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
##  dialog.py

File Description:
## Same a an InputDialog box but modifiable
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from src.const import HEIGHT, WIDTH
    import customtkinter as ctk
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Class """
class Dialog(ctk.CTkToplevel):
    
    def __init__(self, app, title, message):
        super().__init__(app.JapWord)
        # init of the learning window
        self.title(title)
        if (message.startswith("🡳 Translate 🡳")):
            app.setup_size(self, 325, 350)
        else:
            app.setup_size(self, 325, 300)
        self.resizable(False, False)
        self.transient(app.JapWord)

        self.ouput = None

        # setup of the message
        self.label = ctk.CTkLabel(self, text=message)
        self.label.pack(pady=(20, 10))

        # setup the entry
        self.var_fr = ctk.StringVar(value="French...")
        self.fr = ctk.CTkEntry(self, textvariable=self.var_fr)
        self.fr.pack(pady=5)
        self.fr.focus()
        
        self.var_ro = ctk.StringVar(value="Romanji...")
        self.ro = ctk.CTkEntry(self, textvariable=self.var_ro)
        self.ro.pack(pady=5)
        self.ro.focus()

        self.var_kana = ctk.StringVar(value="Katakana...")
        self.kana = ctk.CTkEntry(self, textvariable=self.var_kana)
        self.kana.pack(pady=5)

        self.var_hira = ctk.StringVar(value="Hiragana...")
        self.hira = ctk.CTkEntry(self, textvariable=self.var_hira)
        self.hira.pack(pady=5)

        self.var_kanji = ctk.StringVar(value="Kanji...")
        self.kanji = ctk.CTkEntry(self, textvariable=self.var_kanji)
        self.kanji.pack(pady=5)

        # Frame to place the button
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)

        # Validation button
        self.validate_btn = ctk.CTkButton(btn_frame, text="Ok", command=self.validate)
        self.validate_btn.pack(side="left", padx=10)

        # Canelation button
        self.cancel_btn = ctk.CTkButton(btn_frame, text="Stop", command=self.cancel)
        self.cancel_btn.pack(side="left", padx=10)


    def validate(self):
        self.ouput = {
            "fr": self.var_fr.get() if hasattr(self, "var_fr") else None,
            "ro": self.var_ro.get() if hasattr(self, "var_ro") else None,
            "kana": self.var_kana.get() if hasattr(self, "var_kana") else None,
            "hira": self.var_hira.get() if hasattr(self, "var_hira") else None,
            "kanji": self.var_kanji.get() if hasattr(self, "var_kanji") else None,
        }
        self.destroy()

    def cancel(self):
        self.ouput = None
        self.destroy()

    def show(self):
        self.wait_window()
        return self.ouput
