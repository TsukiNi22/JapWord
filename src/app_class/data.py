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
##  word.py

File Description:
## Class to store the data about word
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from enum import Enum
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Class """
class DataType(Enum):
    Letter = 1
    Kanji = 2
    Word = 4

class Data():

    def __init__(self, data_type, fr = None, ro = None, kana = None, hira = None, kanji = None):
        self.setup_type(data_type)
        self.fr = fr
        self.ro = ro
        self.kana = kana
        self.hira = hira
        self.kanji = kanji

    def setup_type(self, data_type):
        self.Letter = False
        self.Kanji = False
        self.Word = False
        match data_type:
            case DataType.Letter.value:
                self.Letter = True
            case DataType.Kanji.value:
                self.Kanji = True
            case DataType.Word.value:
                self.Word = True

    def setdico(self, dico):
        self.fr     = dico["fr"]    
        self.ro     = dico["ro"]    
        self.kana   = dico["kana"]  
        self.hira   = dico["hira"]  
        self.kanji  = dico["kanji"] 
        self.Letter = dico["Letter"]
        self.Kanji  = dico["Kanji"] 
        self.Word   = dico["Word"]  

    def getdico(self):
        dico = {}
        dico["fr"]      = self.fr
        dico["ro"]      = self.ro
        dico["kana"]    = self.kana
        dico["hira"]    = self.hira
        dico["kanji"]   = self.kanji
        dico["Letter"]  = self.Letter
        dico["Kanji"]   = self.Kanji
        dico["Word"]    = self.Word
        return dico
