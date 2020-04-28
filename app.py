import tkinter as tk
from tkinter import filedialog,Text
import os

root=tk.Tk()
apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempapps= f.read()
        tempapps=tempapps.split(',')
        apps=[x for x in tempapps if x.strip()]

def  addApp():

    for widget in frame.winfo_children():
        widget.destroy()
    filename=filedialog.askopenfilename(initialdir="/",title="select file",
    filetypes=(("executetables","*.exe"),("all files","*,*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame,text=app,bg="grey")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)


canvas=tk.Canvas(root,height=600,width=600,bg="#87cefa")
canvas.pack()
frame=tk.Frame(root, bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
openapp=tk.Button(root,text="open apps",padx=10,pady=5,bg="#00008b",fg="white",command=addApp)
openapp.pack()

runapp=tk.Button(root,text="run apps",padx=10,pady=5,bg="#00008b",fg="white",command=runApps)
runapp.pack()

for app in apps:
    label=tk.Label(frame,text=app)
    label.pack()
root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app+',')
