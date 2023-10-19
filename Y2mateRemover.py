import os
from customtkinter import *
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox



description = "This will target all the files with the prefix specified in the textbox and remove it.\n This includes all the files in the subdirectories as well"
defaultMatchString = "y2mate.com - "


def formatNicely(l):
    s = ''
    for (index, item) in enumerate(l):
        s+=(f"  {index+1}.{str(item)}\n")
    return s
def removeThingy(*e):
    currentDir = filedialog.askdirectory()
    if currentDir == '' or currentDir == None:
        CTkMessagebox(app, message="Please select a valid Folder", icon="cancel")
        return
    
    
    renamedFiles = []
    couldNotRename = []
    matchToRemove = entryVar.get()
    
    
    for (root, dir, files) in os.walk(currentDir, topdown=True):
        for file in files:
            if file.find(matchToRemove) == -1:
                continue
            oldname = os.path.join(root, file)
            newname = os.path.join(root, file.removeprefix(matchToRemove))
            try:
                os.rename(oldname, newname)
                renamedFiles.append(file)
            except Exception as err:
                CTkMessagebox(app, icon="warning", message=str(err))
                couldNotRename.append(file)
    CTkMessagebox(app, icon="check", message=
                  f"SuccessFully Renamed {len(renamedFiles)} Files :\n"+formatNicely(renamedFiles)
                  +f"\nCould Not Rename {len(couldNotRename)} Files:\n"+formatNicely(couldNotRename))



app = CTk()
app.title("")
app.resizable(width=False, height=False)

Font = CTkFont("Ariak", size=15, weight="bold")
titleFont = CTkFont("Ariel", size=20, weight="normal")


mainLb = CTkLabel(app, text="Remove Annoying Prefixes", font=titleFont, text_color="#a6bcff")
mainLb.grid(row=0, column=0, columnspan=2, pady=10, sticky='nsew')
entryVar = StringVar(app)
entryVar.set(defaultMatchString)
entry = CTkEntry(app, textvariable=entryVar, font=Font)
entry.grid(row=1, column=0, padx=30, pady=3, sticky="nsew")

btn = CTkButton(app, text="Remove Thingy", command=removeThingy, font=Font)
btn.grid(row=1, column=1, padx=30, pady=5, sticky='nsew')

lb = CTkLabel(app, text=description, font=CTkFont("Ariak", size=15))
lb.grid(row=2,columnspan=2, column=0, padx=30, pady=3)

app.mainloop()