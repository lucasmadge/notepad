# notepad
A notepad application for simple text document creation, editing and saving. Made with python, containing two files, the main file being notepad.py and the functions used as tkinter commands are in notepad_modules.py.

Created by Lucas Madge, February 2026

# How It's Made:
This application was entirely written in python. The main notepad.py file creates the tkinter window in which the application is interacted with. Each file menu has a command attached, with all the commands' functions being located inside notepad_module.py.

# How to Run:
You need to have python 3.9 installed.

# Known Issues:
Cancelling 'Save As' action does not cancel, but rather saves the notepad with a default name, being "Notebook_{time created}_{iteration (incase several were made within the same minute)}
