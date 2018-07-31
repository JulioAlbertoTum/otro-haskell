import tkinter as tk
import time
import threading
from datetime import datetime

class Cronometro(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.count = 0
        self.encendido = False;
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text=datetime.now().strftime('%M:%S.%f')[:-4])
        self.label.pack(padx=30, pady=30)

        self.start = tk.Button(self)
        self.start["text"] = "Iniciar"
        self.start["command"] = self.say_hi
        self.start.pack(side="top", padx=100, pady=5)

        self.stop = tk.Button(self)
        self.stop["text"] = "Parar"
        self.stop["command"] = self.apagar
        self.stop.pack(side="top", padx=100, pady=5)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        self.encendido = True
        t = threading.Timer(0, self.contar_en_label)
        t.start()
            

    def contar_en_label(self):
        while self.encendido:
            time.sleep(0.001)
            self.count = self.count + 1
            self.label["text"] = self.formato_contador(self.count)

    def apagar(self):
        self.encendido = False

    def formato_contador(self, contador):
        millisec = contador % 1000
        seconds = (contador // 1000) % 60
        minutes = (contador // 60000) % 60
        min = self.output_with_zero(minutes,10)
        sec = self.output_with_zero(seconds,10)
        if millisec >= 10:
            milisec = self.output_with_zero(millisec,100)
        else:
            milisec = "00"+ str(millisec)

        return min +":"+ sec +":"+  milisec

    def output_with_zero(self, number,range):
        return str(number) if (number >= range) else "0"+ str(number)
  
root = tk.Tk()
cronometro = Cronometro(master=root)
cronometro.mainloop() 