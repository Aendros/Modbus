from tkinter import *
from tkinter import ttk
import serial.tools.list_ports

# Get the number of ports available
ports = list(serial.tools.list_ports.comports())
ports = ['Casa', 'Perro']
# Iniciamos UI
myUi = Tk()
myUi.title('Gases')
myUi.geometry('650x450')

# Añadir imagen de fondo a la pantalla
filename = PhotoImage(file="Gases.png")
background_label = Label(myUi, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Creamos los widgets que forman la UI
Label(myUi, text='Puerto').grid(row=0, column=0)
dpl1 = ttk.Combobox(myUi)
dpl1.values = ports
dpl1.grid(row=0, column=1)
Label(myUi, text='Esclavo').grid(row=0, column=2)
ent2 = Entry(myUi)
ent2.grid(row=0, column=3)
conn_button = Button(myUi, text='Conectar')
conn_button.grid(row=0, column=4)

myUi.resizable(width='False', height='False')
myUi.mainloop()
