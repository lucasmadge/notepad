""" Module file containing functions used in notepad.py """

import datetime
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# variables
current_file = None

def create_document(text_widget):
    global current_file
    
    text_widget.pack()
    text_widget.delete("1.0", tk.END)

    current_file = None

def open_document(text_widget):
    global current_file
    file_path = filedialog.askopenfilename(filetypes = [("Text Files", "*.txt")])

    # user cancelled the open document request
    if not file_path:
        return
    
    # read file contents
    with open(file_path, "r") as document:
        content = document.read()

    text_widget.pack()
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", content)

    current_file = file_path

def save_document(text_widget):
    global current_file

    # no file open to save
    if current_file == None:
        messagebox.showwarning("No File", "No document is currently open.")
        return

    content = text_widget.get("1.0", tk.END)

    with open(current_file, "w") as document:
        file.write(content)

def saveAs_document(text_widget):
    global current_file

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    # if no name is given, generate one based on the time
    if not file_path:
        document_name_time = datetime.datetime.now()
        document_name = "Notebook_ " + document_name_time.strftime("%d-%m-%Y %H,%M")

        file_path = f"{document_name}.txt"
        counter = 1

        # if file exists, add a number
        while os.path.exists(file_path):
            file_path = f"{document_name}_{counter}.txt"
            counter += 1

    content = text_widget.get("1.0", tk.END)

    with open(file_path, "w") as document:
        document.write(content)

    current_file = file_path

def rename_document():
    global current_file

    # no file open to rename
    if current_file == None:
        messagebox.showwarning("No File", "No document is currently open.")
        return

    new_name = simpledialog.askstring("Rename", "Enter new file name:")

    # name not given
    if not new_name:
        return

    # make sure directory doesn't change
    directory = os.path.dirname(current_file)
    new_file_path = os.path.join(directory, new_name + ".txt")


    # prevent overwriting existing file
    if os.path.exists(new_file_path):
        messagebox.showerror("Error", "A file with that name already exists.")
        return

    # rename the file
    os.rename(current_file, new_file_path)

    # update current file reference
    current_file = new_file_path
