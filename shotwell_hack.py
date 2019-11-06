#deploy: sudo apt install xdotool
#create shortcut
 

import time
from os.path import expanduser

import subprocess

result = subprocess.run(['xdotool', "search", "--onlyvisible","--class", "Shotwell", 'getwindowname'], stdout=subprocess.PIPE)

window_name = str(result.stdout)

result = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE)
window_id=str(result.stdout).replace("b'","").replace("\\n'","")

if not "Shotwell" in window_name:
    quit()

chunks = window_name.split("~/")
filename = chunks[0].replace("b'","")[:-1].strip()
folder = "/"+chunks[1].split(" - ")[0][:-1]+"/"

full_filename = expanduser("~")+folder+filename


import tkinter as tk
from tkinter import messagebox

root= tk.Tk() 
root.withdraw()

MsgBox = tk.messagebox.askquestion ('Fájl törlése '+window_id,'Biztos benne, hogy törölni szeretné a(z) '+full_filename+' fájlt?',icon = 'warning')
#MsgBox.pack()
if MsgBox == 'yes':
    result = subprocess.run(["xdotool", "windowminimize", window_id], stdout=subprocess.PIPE)
    time.sleep(0.1)
    result = subprocess.run(["xdotool", "search", "--onlyvisible","--class", "Shotwell", "windowactivate"], stdout=subprocess.PIPE)
    time.sleep(0.1)
    result = subprocess.run(["xdotool", "key", "space"], stdout=subprocess.PIPE)
    time.sleep(0.3)
    result = subprocess.run(["rm",full_filename], stdout=subprocess.PIPE)
    time.sleep(0.1)
    root.destroy()

else:
    root.destroy()
  
root.mainloop()