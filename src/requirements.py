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
##  requirements.py

File Description:
## Install the requirements
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from src.const import REQUIREMENTS_PATH
    from subprocess import check_call, CalledProcessError
    from sys import executable
    from os import path
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Program """
def requirements():
    if path.exists(REQUIREMENTS_PATH):
        try:
            check_call([executable, "-m", "pip", "install", "-r", REQUIREMENTS_PATH])
        except CalledProcessError as e:
            print("Dependency installation error:", e)
            exit(1)
    else:
        print("Can't found " + REQUIREMENTS_PATH)
        exit(1)
