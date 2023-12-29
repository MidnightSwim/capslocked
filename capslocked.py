from pynput import keyboard
from tkinter import *
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
	

keyList = []

def on_press(key):

    if (key == keyboard.Key.caps_lock):
        keyList.append(str(key))

        if (len(keyList) == 1):
            window.deiconify() 

        else:
            window.withdraw()
            keyList.clear()
            
with keyboard.Listener(on_press=on_press) as listener :

    window = Tk()
    window.overrideredirect(True)
    picture = PhotoImage(file=resource_path('caps_lock_128.png'))
    window.title("Capslocked")
    window.withdraw()
    label = Label(window, image=picture)
    label.pack()
    window.mainloop()

    listener.join()
    