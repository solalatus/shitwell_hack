#deploy: sudo apt install xdotool
#create shortcut
 
import time
from os.path import expanduser
import shlex

import subprocess

result = subprocess.run(['xdotool', "search", "--onlyvisible","--class", "Shotwell", 'getwindowname'], stdout=subprocess.PIPE)

window_name = result.stdout.decode('utf-8')

result = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE)
window_id=str(result.stdout).replace("\\n'","")

if not "Shotwell" in window_name:
    quit()

#print(window_name)

window_name = window_name.replace("\n","")

window_name = window_name.replace(") - Shotwell","")
if " (/" in window_name:
    chunks = window_name.split(" (/")
    filename = chunks[0]
    folder = "/"+chunks[1]+"/"
elif " (~/" in window_name:
    chunks = window_name.split(" (~/")
    filename = chunks[0]
    folder = expanduser("~")+"/"+chunks[1]+"/"
else:
    quit()


full_filename = folder+filename

#print(full_filename)

import tkinter as tk
from tkinter import messagebox

root= tk.Tk() 
root.withdraw()

MsgBox = tk.messagebox.askquestion ('Fájl törlése '+window_id,'Biztos benne, hogy törölni szeretné a(z) '+full_filename+' fájlt?',icon = 'warning')

if MsgBox == 'yes':
    result = subprocess.run(["xdotool", "windowminimize", window_id], stdout=subprocess.PIPE)
    time.sleep(0.1)
    result = subprocess.run(["xdotool", "search", "--onlyvisible","--class", "Shotwell", "windowactivate"], stdout=subprocess.PIPE)
    time.sleep(0.1)
    result = subprocess.run(["xdotool", "key", "space"], stdout=subprocess.PIPE)
    time.sleep(0.3)
    full_filename = str(shlex.quote(full_filename)).replace("'","")
    result = subprocess.run(["rm",full_filename], stdout=subprocess.PIPE)
    time.sleep(0.1)
    root.destroy()

else:
    root.destroy()
  
root.mainloop()