# import tkinter for GUI app

import tkinter as tk

from tkinter import filedialog,messagebox

# Main window code
root=tk.Tk()
root.title("Simple Writepad")
root.geometry("800x600")


#Creating Text area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Century",13)
)

text.pack(expand=True,fill=tk.BOTH)

# Main logic Starts

# Function 1 to create a new file:

def newfile():
    text.delete(1.0,tk.END)

# Function 2 to open a new file:

def openfile():
    #open dialogue
    file_name=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_name:
        # open file
        with open(file_name,"r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

# Function 3 to save a file:

def savefile():
    # open save file dialogue
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        # Save file
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))

    messagebox.showinfo("Info","File Saved Successfully")

# Main Menu /Create Menu Bar

Main_menu=tk.Menu(root)
root.config(menu=Main_menu)

file_menu=tk.Menu(Main_menu)
help_menu = tk.Menu(Main_menu)

# New Menu,Save menu,Load menu,Exit

# Add File menu to menubar
Main_menu.add_cascade(label="File",menu=file_menu)
Main_menu.add_cascade(label="Help",menu=help_menu)


file_menu.add_command(label="New Text File",command=newfile)
file_menu.add_command(label="Open Text File",command=openfile)
file_menu.add_command(label="Save File",command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Simple placeholder for the Help menu
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Simple Writepad v1.0"))
# Starts and keeps the window open
root.mainloop()