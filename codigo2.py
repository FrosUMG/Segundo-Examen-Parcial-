import pyfirmata
from tkinter import *
import threading
var = False
board = pyfirmata.Arduino('COM11')
it = pyfirmata.util.Iterator(board)
it.start()
board.digital[2].mode - pyfirmata. INPUT
root = Tk()
root.title("Encendido y apagado de led")
root.geometry('380x300')
root.configure(background = '#84b6f4')
etiqueta = Label (root, text='ARDUINO Y PYTHON, PUSH BUTTON Y LED', bg='#3e5f8a')
etiqueta.pack(fill=X)
def color_encendido():
   root.configure(background="#5DBB63")
def color_apagado():
   root.configure(background="#900D09")
def encender():
        global var
        var = True
        color_encendido()
def apagar():
        global var
        var = False
        color_apagado()
def encendidoBoton():
   global var
   while True:
      if (board.digital[2].read() is True) or ( var is True):
         board.digital[13].write(1)
         color_encendido()
      if (board.digital[2].read() is True) and ( var is True):
        var = False
def apagadoBoton():
   global var
   while True:
      if (board.digital[2].read() is False) and (var is False):
        board.digital[13].write(0)
        color_apagado()
Button(root, text="ON", bg="#bdecb6", command=encender ,width=20, height=5).pack(padx=30, pady=30)
Button(root, text="OFF", bg="#ff6961", command=apagar, width=20, height=5).pack()
threading. Thread (target=encendidoBoton).start()
threading. Thread (target=apagadoBoton).start()
root.mainloop()
