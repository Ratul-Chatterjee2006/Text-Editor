# import tkinter for GUI app

import tkinter as tk

from tkinter import filedialog,messagebox

# Lists of fonts and sont size

tupleof_Fonts=("Century","Arial","Times New Roman","Calibri(Body)","Rockwell","Courier","Helvetica","Bahnschrift SemiLight","Calisto MT","French Script MT","Sans Serif Collection")
tupleof_Fontsize=(8,9,10,11,12,13,14,15,16,18,20,24,25,28,30,32,36,38,40,42,48,50,60,70,78)

# Main window code
root=tk.Tk()
root.title("Simple Writepad")
root.geometry("800x600")

# Toolbar frame container

toolbar=tk.Frame(root,bg="lightgrey")
toolbar.pack(side=tk.TOP,fill=tk.X)

selected_font=tk.StringVar(value=tupleof_Fonts[0])
selected_fontsize=tk.StringVar(value=tupleof_Fontsize[5])
#Creating Text area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=(selected_font.get(),selected_fontsize.get())
)
text.pack(expand=True,fill=tk.BOTH)


# Function to update font size

def update_font_size(choice=None):

    try:
        present_font=selected_font.get()
        present_fontsize=int(selected_fontsize.get())

        # 2. Create unique, dynamic tag names based on the choices
        font_tag=f"font_{present_font}"
        size_tag=f"font_{present_fontsize}"

        # 3. Configure those tags with the specific properties
        text.tag_configure(font_tag,font=(present_font,present_fontsize))

        # 4. Apply these tags ONLY to the highlighted text selection
        text.tag_add(font_tag,"sel.first","sel.last")
        text.tag_add(size_tag,"sel.first","sel.last")

        text.tag_configure("makeit_bold",font=(present_font,present_fontsize,"bold"))
        text.tag_configure("makeit_italic",font=(present_font,present_fontsize,"italic"))
        text.tag_configure("makeit_underline",font=(present_font,present_fontsize,"underline"))

    except:
        pass
    

# Main logic Starts

# Function 1 to create a new file:

def newfile(event=None):
    text.delete(1.0,tk.END)
    return "break"

# Function 2 to open a new file:

def openfile(event=None):
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
    return "break"

# Function 3 to save a file:

def savefile(event=None):
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
    return "break"

# Function 1 to make it bold:

def change_to_bold(event=None):
    try:
        current_line=text.tag_names("sel.first")

        if "makeit_bold" in current_line:
            text.tag_remove("makeit_bold","sel.first","sel.last")
        else:
            text.tag_add("makeit_bold","sel.first","sel.last")
    except:
        pass
    return "break"

# Function 2 to make it italic:

def change_to_italic(event=None):
    try:
        current_line=text.tag_names("sel.first")

        if "makeit_italic" in current_line:
            text.tag_remove("makeit_italic","sel.first","sel.last")
        else:
            text.tag_add("makeit_italic","sel.first","sel.last")
    except:
        pass

    return "break"

# Function 2 to make it italic:

def change_to_underline(event=None):
    try:
        current_line=text.tag_names("sel.first")

        if "makeit_underline" in current_line:
            text.tag_remove("makeit_underline","sel.first","sel.last")
        else:
            text.tag_add("makeit_underline","sel.first","sel.last")
    except:
        pass
    return "break"

# Font Family Dropdown
font_dropdown = tk.OptionMenu(toolbar, selected_font, *tupleof_Fonts, command=update_font_size)
font_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

# Font Size Dropdown
size_dropdown = tk.OptionMenu(toolbar, selected_fontsize, *tupleof_Fontsize, command=update_font_size)
size_dropdown.pack(side=tk.LEFT, padx=5, pady=5)


# Adding Bold,Italic and underline

bold_bttn=tk.Button(toolbar,text="Bold",command=change_to_bold)
bold_bttn.pack(side=tk.LEFT,padx=5,pady=5)

italic_bttn=tk.Button(toolbar,text="Italic",command=change_to_italic)
italic_bttn.pack(side=tk.LEFT,padx=5,pady=5)

underline_bttn=tk.Button(toolbar,text="Underline",command=change_to_underline)
underline_bttn.pack(side=tk.LEFT,padx=5,pady=5)

# Main Menu /Create Menu Bar

Main_menu=tk.Menu(root)
root.config(menu=Main_menu)

file_menu=tk.Menu(Main_menu)
tool_menu=tk.Menu(Main_menu)
help_menu = tk.Menu(Main_menu)

# New Menu,Save menu,Load menu,Exit

# Add File menu to menubar
Main_menu.add_cascade(label="File",menu=file_menu)
Main_menu.add_cascade(label="Tools",menu=tool_menu)
Main_menu.add_cascade(label="Help",menu=help_menu)

# File menu
file_menu.add_command(label="New Text File(ctrl+N)",command=newfile)
file_menu.add_command(label="Open Text File(ctrl+O)",command=openfile)
file_menu.add_command(label="Save File(ctrl+s)",command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Tool menu
tool_menu.add_command(label="Bold",command=change_to_bold)
tool_menu.add_command(label="Italic",command=change_to_italic)
tool_menu.add_command(label="Underline",command=change_to_underline)

# Simple placeholder for the Help menu
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Simple Writepad v1.2"))
# Starts and keeps the window open

text.bind("<Control-n>",newfile)
text.bind("<Control-o>",openfile)
text.bind("<Control-s>",savefile)
text.bind("<Control-b>",change_to_bold)
text.bind("<Control-i>",change_to_italic)
text.bind("<Control-u>",change_to_underline)
root.mainloop()