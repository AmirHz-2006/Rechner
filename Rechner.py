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
        
        self.create_sections()
        
    # Frames erstellen
    def create_sections(self):
        self.display_frame  = Frame(self.window, width= 380, height=75, bg=self.farbe)
        self.display_frame .pack(side=TOP ,pady=15 , fill='both' )

        self.buttons_frame  = Frame(self.window , width=380, height=325, bg=self.farbe)
        self.buttons_frame .pack(padx= 5 ,fill="both" , pady=10 , expand=True)
        self.create_display()
        self.create_buttons()

    # Anzeige erstellen
    def create_display(self):
        self.display_label = Label(self.display_frame, font=("Arial", 27, 'bold'),
                                   textvariable=self.display_value, bg=self.farbe,
                                    fg="white", anchor="e", padx=10,
                                    relief="flat")
        self.display_label.pack(ipadx=20, ipady=10, fill="both", expand=True)

    # Schriftgröße dynamisch anpassen
    def update_display_size(self , *args):
        current_text = self.display_value.get()
        text_length = len(current_text)

        if text_length <= 16:
            font_size = 27
        elif text_length <= 20:
            font_size = 24
        elif text_length <= 24:
            font_size = 20
        else:
            font_size = 17
        self.display_label.config(font=("Arial", font_size, "bold"))