import eel
import tkinter as tk
from tkinter import filedialog

eel.init('web')

@eel.expose
def open_file_explorer():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    return file_path

