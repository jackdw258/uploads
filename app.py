import tkinter
from tkinter import messagebox

# Create a hidden root window
root = tkinter.Tk()
root.withdraw()

# Show a warning popup
messagebox.showwarning("Warning", "Test succeed")

# Close the root window after popup is closed
root.destroy()
