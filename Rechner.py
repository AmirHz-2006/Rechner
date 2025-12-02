import math
from tkinter import *
from tkinter import messagebox

class Calculator:
    # Hauptfenster erstellen
    def __init__(self):
        self.window = Tk()
        self.window.title("Rechner")
        self.window.geometry("380x400")
        self.window.resizable(width=False, height=False)
        self.farbe = "#222222"
        self.window.configure(bg=self.farbe)

        # Variablen
        self.num1 = None
        self.operator = None
        self.display_value = StringVar()
        self.display_value.set("0")
        self.display_value.trace('w' , self.update_display_size)