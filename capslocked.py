from pynput import keyboard
from tkinter import *
import os

#needed by PyInstaller to show the picture 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
	

key_pressed = False

def on_press(key):
    global key_pressed
    if (key == keyboard.Key.caps_lock) and (key_pressed == False):
        window.deiconify()
        key_pressed = True
    
    else:
        window.withdraw()
        key_pressed = False
       
            
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
    
