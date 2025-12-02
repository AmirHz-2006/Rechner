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
        
    # Tasten erstellen
    def create_buttons(self):
        buttons = [
            'x²','√', 'C', '⌫',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
        ]
        # Stil für Tasten definieren
        button_style = {
            'font': ('Arial', 12 , 'bold'),
            'cursor': 'hand2',
            'fg' : 'white',
            'relief': 'raised'
        }

        row, col = 0, 0
        for button_text in buttons:
            # äußerliche Einstellung von Tasten
            if button_text == '=':
                button = Button( self.buttons_frame , text=button_text,
                                 width=5, height=2, bg="#FF6B9D" ,**button_style,
                                 command=lambda: self.calculate_result()
                )
            elif button_text == 'C':
                button = Button(self.buttons_frame , text=button_text, width=5, height=2,
                                command= lambda :self.clear() ,
                                bg="#444444" , **button_style
                )
            elif button_text == '⌫':
                button = Button( self.buttons_frame, text=button_text, width=5, height=2,
                    command= lambda: self.backspace(), bg="#444444", **button_style
                )
            elif button_text == 'x²':
                button = Button( self.buttons_frame, text=button_text, width=5, height=2,
                    command= lambda: self.power(), bg="#444444",
                    **button_style
                )
            elif button_text == '√':
                button = Button( self.buttons_frame, text=button_text, width=5, height=2,
                    command=self.square_root, bg="#444444",**button_style
                )
            elif button_text in ['+', '-', '*', '/']:
                button = Button( self.buttons_frame , text=button_text, width=5, height=2,
                            command=lambda op=button_text: self.set_operation(op),
                            bg="#444444" , **button_style
                )
            else:
                button = Button( self.buttons_frame , text=button_text, width=5, height=2,
                                command=lambda num=button_text: self.append_number(num) ,
                                 bg="#666666" ,**button_style
                )
            button.grid(row= row , column=col, sticky="nsew" , ipadx=5 , ipady=5)
            col += 1
            if col == 4:
                col = 0
                row += 1

        # Zeilen und Spalten gleichmäßig verteilen
        for i in range(5):
            self.buttons_frame .rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame .columnconfigure(i, weight=1)

    # Fehlermeldungen anzeigen
    def error(self, e):
        if e == 'error':
            messagebox.showerror("Error", "Invalid operation")
        elif e == 'division':
            messagebox.showerror("Error", "Division by zero is not allowed")
        elif e == 'number':
            messagebox.showerror("Error", "Invalid number")
        elif e == 'negative_sqrt':
            messagebox.showerror("Error", "Cannot calculate square root of negative number")
            
    # Zahl bestimmen
    def append_number(self, number):
        current = self.display_value.get()

        if current == "0" and number != ".":
            self.display_value.set(number)
        elif current == "0" and number == "0":
            pass  # جلوگیری از صفرهای متوالی
        else:
            self.display_value.set(current + number)

    # Letzte Zahl löschen
    def backspace(self):
        """پاک کردن آخرین رقم از نمایشگر"""
        current = self.display_value.get()
        if len(current) > 1:
            self.display_value.set(current[:-1])
        else:
            self.display_value.set("0")

    # Quadratwurzel berechnen
    def square_root(self):
        """محاسبه جذر عدد"""
        try:
            current = float(self.display_value.get())
            if current < 0:
                self.error('negative_sqrt')
                return
            result = math.sqrt(current)
            self.display_value.set(str(result))
        except:
            self.error('number')
            
    # Quadrat berechnen
    def power(self):
        """محاسبه توان با توان مشخص"""
        try:
            current = float(self.display_value.get())
            result = current ** 2
            self.display_value.set(str(result))
        except:
            self.error('number')

    # Operation setzen
    def set_operation(self, op):
        # تنظیم عملگر برای محاسبه
        try:
            self.num1 = float(self.display_value.get())
            self.operator = op
            self.display_value.set("0")
        except:
            self.error('number')

    # Ergebnis berechnen
    def calculate_result(self):
        # انجام محاسبه
        if self.num1 is None or self.operator is None:
            return
        try:
            num2 = float(self.display_value.get())

            if self.operator == '+':
                result = self.num1 + num2
            elif self.operator == '-':
                result = self.num1 - num2
            elif self.operator == '*':
                result = self.num1 * num2
            elif self.operator == '/':
                if num2 == 0:
                    self.error('division')
                    return
                result = self.num1 / num2

            # نمایش نتیجه
            self.display_value.set(str(result))
            self.num1 = None
            self.operator = None

        except:
            self.error('error')

    # Anzeige komplett entfernen
    def clear(self):
        self.display_value.set("0")
        self.num1 = None
        self.operator = None

    def run(self):
        self.window.mainloop()

# GUI starten
if __name__ == "__main__":
    calc = Calculator()
    calc.run()