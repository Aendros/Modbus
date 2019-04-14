from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import minimalmodbus
import serial.tools.list_ports


class BandejasApp:

    def __init__(self):
        super(BandejasApp, self).__init__()
        self.parent = Tk()
        self.parent.resizable(width='false', height='false')
        self.parent.geometry('1024x600')

        # Añadir Frame para la imagen y colocar imagen
        # self.bottomframe = Frame(self.parent, height=450, width=650)
        # self.filename = PhotoImage(file="Gases.png")
        # self.picture = Label(self.bottomframe, image=self.filename)
        # self.picture.place(x=0, y=0, relwidth=1, relheight=1)
        # self.bottomframe.grid(column=3, row=3)
        # self.bottomframe.pack()
        self.parent.mainloop()

        # Preguntamos por los puertos COM Disponibles
        ports = serial.tools.list_ports.comports(include_links=FALSE)
        # TEST
        print(ports)

        # Creamos los widgets que forman la UI
        Label(self.parent, text='Puerto').grid(row=0, column=0)
        Label(self.parent, text='sen_01').grid(row=2, column=0)
        Label(self.parent, text='sen_02').grid(row=3, column=0)
        Label(self.parent, text='sen_03').grid(row=4, column=0)
        Label(self.parent, text='sen_04').grid(row=5, column=0)
        Label(self.parent, text='sen_05').grid(row=6, column=0)
        Label(self.parent, text='sen_06').grid(row=7, column=0)
        Label(self.parent, text='sen_07').grid(row=8, column=0)
        Label(self.parent, text='sen_08').grid(row=9, column=0)
        Label(self.parent, text='fa_vis').grid(row=10, column=0)
        Label(self.parent, text='fal_ad').grid(row=11, column=0)
        Label(self.parent, text='fal_ad_au').grid(row=12, column=0)
        Label(self.parent, text='fa_i_1').grid(row=13, column=0)
        Label(self.parent, text='fa_i_2').grid(row=14, column=0)
        Label(self.parent, text='fl_vis').grid(row=15, column=0)
        Label(self.parent, text='fa_gen').grid(row=16, column=0)
        Label(self.parent, text='fa_asp').grid(row=17, column=0)

        self.combo1 = ttk.Combobox(self.parent, state="readonly")
        self.combo1["values"] = ports

        # for x in ports:
        #    self.puertos.insert(END, x)

        self.combo1.grid(row=0, column=1)
        Label(self.parent, text='Esclavo').grid(row=0, column=2)
        self.parent.ent2 = Entry(self.parent)
        self.parent.ent2.grid(row=0, column=3)
        self.conn_button = Button(self.parent, text='Conectar', command=self.conect)
        self.conn_button.grid(row=0, column=4)
        self.parent.grid()

    def conect(self):
        # Creacion de la comunicación RTU y se mantendrá abierta hasta
        # que se cierre la aplicación

        # guardo sólo la primera palabra del string
        puerto = str(self.combo1.get()).split()[0]
        slave = int(self.parent.ent2.get())
        # TEST
        print(puerto, "  ", slave)
        self.instrument = minimalmodbus.Instrument(puerto, slave, mode='rtu')
        self.instrument.serial.baudrate = 9600  # Baud
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.close_port_after_each_call = FALSE
        self.refresh_data()
        # datum=[sen_01, sen_02, sen_03, sen_04, sen_05, sen_06, sen_07, sen_08, sen_fa_vis, sen_faL_AD, sen_faL_AD_AU, sen_fa_I_1, sen_fa_I_2, sen_fl_vis, sen_fa_gen, sen_fa_asp]

    def refresh_data(self):

        print("Dentro de la función de lectura de datos")
        sen_01 = self.leer_registro(4096, 0, 4)  # Read Analog Input Register (HR)
        sen_02 = self.leer_registro(4097, 0, 4)
        sen_03 = self.leer_registro(4098, 0, 4)
        sen_04 = self.leer_registro(4099, 0, 4)
        sen_05 = self.leer_registro(4100, 0, 4)
        sen_06 = self.leer_registro(4101, 0, 4)
        sen_07 = self.leer_registro(4102, 0, 4)
        sen_08 = self.leer_registro(4103, 0, 4)
        fa_vis = self.leer_registro(4352, 0, 4)
        fal_ad = self.leer_registro(4353, 0, 4)
        fal_ad_au = self.leer_registro(4354, 0, 4)
        fa_i_1 = self.leer_registro(4355, 0, 4)
        fa_i_2 = self.leer_registro(4356, 0, 4)
        fl_vis = self.leer_registro(4357, 0, 4)
        fa_gen = self.leer_registro(4358, 0, 4)
        fa_asp = self.leer_registro(4359, 0, 4)
        print(sen_01, sen_02, sen_03, sen_04, sen_05, sen_06, sen_07, sen_08, fa_vis, fal_ad,
              fal_ad_au, fa_i_1, fa_i_2, fl_vis, fa_gen, fa_asp)

    def leer_registro(self, reg, dec, fun):

        try:
            value = self.instrument.read_register(reg, dec, fun)
            return value
        except IOError:
            messagebox.showinfo("Algo ha ido mal al leer el registro: ", reg)


app = BandejasApp()
