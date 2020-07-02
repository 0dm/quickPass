# Strong Password Generator with GUI
import tkinter as tk
import string as s
import random as rand
import pyperclip
i = 0

# Outputs string with random characters and button to copy
def generatePass(i):
    chars = s.ascii_uppercase + s.ascii_lowercase + s.digits + s.punctuation 
    length = 8
    passgen = ''.join(rand.choice(chars) for x in range(length))
    msg.config(text = passgen)
    copy = tk.Button(
         text = "Copy [" + str(i) + "]",
         width = 25,
         height = 5,
         command = lambda:[pyperclip.copy(passgen),msg.config(text = "Copied: " + passgen), copy.destroy()]
    )
    copy.pack()

# Assigns number to copy button
def setupPass():
    global i
    i = i + 1
    generatePass(i)

# Creates button for form
def setupForm():
  action = tk.Button(
    text = "Generate",
    width = 25,
    height = 5,
    command = setupPass
        
  )
  action.pack()

# Sets up window
window = tk.Tk()
window.title("quickPass")
window.update_idletasks()

# Get position of window to center
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('+%d+%d'%(x,y))
# Global label for easy changes later
msg = tk.Label(text="...")
msg.pack()
setupForm()


