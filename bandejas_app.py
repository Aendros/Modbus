import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import minimalmodbus
import serial.tools.list_ports


class BandejasApp:

    def __init__(self):
        super(BandejasApp, self).__init__()
        self.main_window = Tk()
        self.main_window.title('Bandejas Gases')
        self.main_window.resizable(width='FALSE', height='FALSE')
        # self.main_window.geometry('1024x600')
        self.frame1 = Frame(self.main_window, bg='grey',
                            padx=5, pady=5, height=45, width=1024)
        self.frame2 = Frame(self.main_window, bg='grey', padx=5, pady=5)
        self.frame3 = Frame(self.main_window, bg='grey',
                            padx=5, pady=5, height=450, width=650)

        # Preguntamos por los puertos COM Disponibles
        ports = serial.tools.list_ports.comports(include_links=FALSE)

        # Creamos lista para los datos a leer
        # Datos de entrada discreta
        self.ent_discret = [4096, 4097, 4098, 4099, 4100, 4101,
                            4102, 4103, 4352, 4353, 4354, 4355, 4356, 4357,
                            4358, 4359]
        self.ent_regis = [12288, 12289, 12290, 12291, 12292, 12544, 12545,
                          12546, 12547, 12548, 12549, 12550, 12551, 13312,
                          13313, 13314, 13315, 13316]

        # Creamos los widgets que forman el frame1
        Label(self.frame1, text='Puerto', bg="grey").grid(row=0, column=0)
        self.combo1 = ttk.Combobox(self.frame1, state="readonly")
        self.combo1["values"] = ports
        self.combo1.grid(row=0, column=1)
        Label(self.frame1, text='Esclavo', bg="grey").grid(row=0, column=2)
        self.ent2 = Spinbox(self.frame1, from_=0, to=100)
        self.ent2.grid(row=0, column=3)
        self.conn_button = Button(
            self.frame1, text='Configurar', command=self.conect)
        self.conn_button.grid(row=0, column=4)
        Label(self.frame1, text="Lecturas/minuto",
              bg="grey").grid(row=0, column=5)
        self.vel = Scale(self.frame1, from_=2, to=30,
                         resolution=2, orient=HORIZONTAL)
        self.vel.set(2)
        self.vel.grid(row=0, column=6)

        # Creamos los widgets que forman el frame2
        self.data_frame2 = []
        self.labels_frame2 = ['EST_COM', 'COM_OPC', 'MODO_FUN', 'ERROR_OPC',
                              'TEMP_INT', 'sen_01', 'sen_02', 'sen_03', 'sen_04',
                              'sen_05', 'sen_06', 'sen_07', 'sen_08', 'fa_vis',
                              'fal_ad', 'fal_ad_au', 'fa_i_1', 'fa_i_2', 'fl_vis',
                              'fa_gen', 'fa_asp']
        self.labels_list = []
        for x in range(0, len(self.labels_frame2)):
            self.labels_list.append(
                Label(self.frame2, text=self.labels_frame2[x], width=10))
            self.labels_list[x].grid(row=(3 + x), column=0)

        # Creamos los widgets que forman el frame3
        self.data_frame3 = []
        self.filename = PhotoImage(file="Gases.png")
        self.cv = tk.Canvas(self.frame3, width=650, height=450)
        self.cv.create_image(0, 0, anchor=tk.NW, image=self.filename)
        self.list_text_frame3 = []
        self.labels_frame3 = ['Oxígeno', 'Monóxido',
                              'Humedad', 'Temperatura', 'Opacidad', 'PLA']
        for x in range(0, len(self.labels_frame3)):
            self.list_text_frame3.append(self.cv.create_text(
                (x * 100 + 65), 235, text=self.labels_frame3[x]))
        self.cv.pack()

        # Cargamos los frames creados e iniciamos la aplicación
        self.frame1.pack(side=TOP, fill=X)
        self.frame2.pack(side=LEFT, fill=Y)
        self.frame3.pack(side=RIGHT)
        self.main_window.mainloop()

    def conect(self):
        # Creación de la comunicación RTU y se mantendrá abierta hasta
        # que se cierre la aplicación

        # guardo solo la primera palabra del string
        puerto = str(self.combo1.get()).split()[0]
        slave = int(self.ent2.get())

        # imprimo valores introducidos por el usuario
        print(puerto, "  ", slave)
        self.instrument = minimalmodbus.Instrument(puerto, slave, mode='rtu')
        self.instrument.serial.baudrate = 1200  # Baud
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.close_port_after_each_call = FALSE

        self.conn_button.configure(text="Configurado", bg='green')
        self.read_data()

    def read_data(self):
        """Función de refresco de datos"""

        print("Dentro de la función de lectura de datos")
        tiempo = 60000 // (self.vel.get())
        self.main_window.after(tiempo, self.read_data)

        # Lectura de las entradas discretas
        for x in range(0, len(self.ent_discret)):
            self.data_frame2.append(self.leer_entrada(self.ent_discret[x], 2))
            print(self.ent_discret[x], ' = ', self.data_frame2[x])

        # Lectura de registros, los cinco primeros se guardan son del frame2
        for x in range(0, 5):
            self.data_frame2.insert(
                x, self.leer_registro(self.ent_regis[x], 0, 4))
            print(self.ent_regis[x], ' = ', self.data_frame2[x])
        print('Data frame2 guardado')
        for x in range(5, len(self.ent_regis)):
            self.data_frame3.append(
                self.leer_registro(self.ent_regis[x], 0, 4))
            print(self.ent_regis[x], ' = ', self.data_frame3[x - 5])
        print('Data frame3 guardado')
        self.print_data()

    def leer_entrada(self, reg, fun):
        """Función para lectura de entradas discretas"""
        try:
            value = self.instrument.read_bit(reg, fun)
            return value
        except IOError:
            messagebox.showinfo(
                "Información", "Algo ha ido mal al leer el registro: {}".format(reg))

    def leer_registro(self, reg, dec, fun):
        """función para lectura de datos"""

        try:
            value = self.instrument.read_register(reg, dec, fun)
            return value
        except IOError:
            messagebox.showinfo(
                "Información", "Algo ha ido mal al leer el registro: {}".format(reg))

    def print_data(self):
        print('Dentro de la función de escritura de datos')
        # Recorremos la lista de datos para el frame dos, pero
        # saltándonos las primeras cinco posiciones que están reservadas
        # para otros registros que leeremos mas tarde
        for x in range(0, len(self.labels_list)):
            if self.data_frame2[x] != 0:
                self.labels_list[x].configure(bg='green')
            else:
                self.labels_list[x].configure(bg='red')
        for x in range(0, len(self.list_text_frame3)):
            self.cv.itemconfigure(
                self.list_text_frame3[x], text=self.data_frame3[x])


app = BandejasApp()
