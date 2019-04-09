import minimalmodbus
from tkinter import *
from tkinter import ttk, messagebox
import serial.tools.list_ports
from tkinter import messagebox


class BandejasApp():

    def __init__(self, parent):
        self.parent = parent

        # Preguntamos por los puertos COM Disponibles
        ports = serial.tools.list_ports.comports(include_links=False)
        #TEST
        print(ports)

        # Añadir imagen de fondo a la pantalla
        self.parent.resizable(width='False', height='False')
        self.parent.geometry('650x450')
        self.filename = PhotoImage(file="Gases.png")
        self.background_label = Label(self.parent, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Creamos los widgets que forman la UI
        Label(self.parent, text='Puerto').grid(row=0, column=0)
        Label(self.parent, text='SEN_01').grid(row=2, column=0)
        Label(self.parent, text='SEN_02').grid(row=3, column=0)
        Label(self.parent, text='SEN_03').grid(row=4, column=0)
        Label(self.parent, text='SEN_04').grid(row=5, column=0)
        Label(self.parent, text='SEN_05').grid(row=6, column=0)
        Label(self.parent, text='SEN_06').grid(row=7, column=0)
        Label(self.parent, text='SEN_07').grid(row=8, column=0)
        Label(self.parent, text='SEN_08').grid(row=9, column=0)
        Label(self.parent, text='FA_VIS').grid(row=10, column=0)
        Label(self.parent, text='FAL_AD').grid(row=11, column=0)
        Label(self.parent, text='FAL_AD_AU').grid(row=12, column=0)
        Label(self.parent, text='FA_I_1').grid(row=13, column=0)
        Label(self.parent, text='FA_I_2').grid(row=14, column=0)
        Label(self.parent, text='FL_VIS').grid(row=15, column=0)
        Label(self.parent, text='FA_GEN').grid(row=16, column=0)
        Label(self.parent, text='FA_ASP').grid(row=17, column=0)
        self.puertos = ttk.Combobox(self.parent, state="readonly")
        self.puertos["values"] = ports
        # for x in ports:
        #    self.puertos.insert(END, x)
        self.puertos.grid(row=0, column=1)
        Label(self.parent, text='Esclavo').grid(row=0, column=2)
        self.parent.ent2 = Entry(self.parent)
        self.parent.ent2.grid(row=0, column=3)
        self.conn_button = Button(self.parent, text='Conectar', command=self.conect)
        self.conn_button.grid(row=0, column=4)
        self.parent.grid()


    def conect(self):
        '''
       Creacion de la comunicación RTU y se mantendrá abierta hasta
       que se cierre la aplicación
       '''
        #guardo sólo la primera palabra del string
        puerto = str(self.puertos.get()).split()[0]
        slave = int(self.parent.ent2.get())
        #TEST
        print(puerto, "  ", slave)
        self.instrument = minimalmodbus.Instrument(puerto, slave, mode='rtu')
        self.instrument.serial.baudrate = 9600  # Baud
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.close_port_after_each_call = FALSE
        self.refresh_data()
        #datum=[SEN_01, SEN_02, SEN_03, SEN_04, SEN_05, SEN_06, SEN_07, SEN_08, SEN_FA_VIS, SEN_FAL_AD, SEN_FAL_AD_AU, SEN_FA_I_1, SEN_FA_I_2, SEN_FL_VIS, SEN_FA_GEN, SEN_FA_ASP]

    def refresh_data(self):

        print("Dentro de la función de lectura de datos")
        SEN_01 = self.leer_registro(4096, 0, 4)  # Read Analog Input Register (HR)
        SEN_02 = self.leer_registro(4097, 0, 4)
        SEN_03 = self.leer_registro(4098, 0, 4)
        SEN_04 = self.leer_registro(4099, 0, 4)
        SEN_05 = self.leer_registro(4100, 0, 4)
        SEN_06 = self.leer_registro(4101, 0, 4)
        SEN_07 = self.leer_registro(4102, 0, 4)
        SEN_08 = self.leer_registro(4103, 0, 4)
        FA_VIS = self.leer_registro(4352, 0, 4)
        FAL_AD = self.leer_registro(4353, 0, 4)
        FAL_AD_AU = self.leer_registro(4354, 0, 4)
        FA_I_1 = self.leer_registro(4355, 0, 4)
        FA_I_2 = self.leer_registro(4356, 0, 4)
        FL_VIS = self.leer_registro(4357, 0, 4)
        FA_GEN = self.leer_registro(4358, 0, 4)
        FA_ASP = self.leer_registro(4359, 0, 4)
        print(SEN_01, SEN_02, SEN_03, SEN_04, SEN_05, SEN_06, SEN_07, SEN_08, FA_VIS, FAL_AD,
        FAL_AD_AU, FA_I_1, FA_I_2, FL_VIS, FA_GEN, FA_ASP)

    def leer_registro(self, reg, dec, fun):

        try:
            value = self.instrument.read_register(reg, dec, fun)
            return value
        except IOError:
            messagebox.showinfo("Algo ha ido mal al leer el registro: ", reg)

if __name__ == '__main__':
    root = Tk()
    app = BandejasApp(root)
    root.mainloop()
