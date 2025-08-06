from tkinter import *
import os

def abrirCalculadora():
    os.system("calc")

def abrirChrome():
    os.system("start chrome")

def abrirPaint():
    os.system("mspaint")

ventana = Tk()
ventana.title("Menu principal")
ventana.config(bg="yellow")
ventana.geometry("520x480")
ventana.resizable(0,0)

botonCalc = Button(text="Calculadora", command=abrirCalculadora)
botonCalc.place(x=50, y=50)

botonChrome = Button(text="Chrome", command=abrirChrome)
botonChrome.place(x=50, y=80)

botonPaint = Button(text="Paint", command=abrirPaint)
botonPaint.place(x=50, y=110)

ventana.mainloop()
