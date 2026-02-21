""" Main File for Notepad Application """

# imports
import tkinter as tk
from notepad_module import create_document, open_document, save_document, saveAs_document, rename_document

# make the screen
root = tk.Tk()
root.title("Notepad") # set window's name
root.geometry("800x300") # set window size

# create menu
menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=lambda: create_document(text_widget))
filemenu.add_command(label="Open...", command=lambda: open_document(text_widget))
filemenu.add_command(label="Save", command=lambda: save_document(text_widget))
filemenu.add_command(label="Save As...", command=lambda: saveAs_document(text_widget))
filemenu.add_separator()
filemenu.add_command(label="Rename", command=rename_document)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

# create text entry box
text_widget = tk.Text(root, height = 20, width = 100)

root.mainloop()
