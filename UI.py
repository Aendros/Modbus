from tkinter import *
import serial.tools.list_ports

# Get the number of ports available
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)
myUi = Tk()
myUi.title('Gases')
myUi.geometry('650x450')

# Añadir imagen de fondo a la pantalla
filename = PhotoImage(file="Gases.png")
background_label = Label(myUi, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(myUi, text='Puerto').grid(row=0, column=0)
for p in ports:
    dpl1.add_cascade(p)
ent1 = Entry(myUi)
mb.grid()
Label(myUi, text='Esclavo').grid(row=0, column=2)
ent2 = Entry(myUi)
ent2.grid(row=0, column=3)
conn_button = Button(myUi, text='Conectar')
conn_button.grid(row=0, column=4)

myUi.resizable(width='False', height='False')
myUi.mainloop()
