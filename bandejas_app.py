from tkinter import *
import minimalmodbus
import serial.tools.list_ports
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class bandejas_app():

	def __init__(self):
		super(bandejas_app, self).__init__()
		self.main_window = Tk()
		self.main_window.resizable(width='FALSE', height='FALSE')
		#self.main_window.geometry('1024x600')
		self.frame1 = Frame(self.main_window, bg='grey', padx=5, pady=5, height=45, width=1024)
		self.frame2 = Frame(self.main_window, bg='grey', padx=5, pady=5)
		self.frame3 = Frame(self.main_window, bg='grey', padx=5, pady=5, height=450, width=650)
		
		# Preguntamos por los puertos COM Disponibles
		ports = serial.tools.list_ports.comports(include_links=FALSE)
		# TEST
		print(ports)

		# Creamos los widgets que forman el frame1
		Label(self.frame1, text='Puerto', bg="grey").grid(row=0, column=0)
		self.combo1 = ttk.Combobox(self.frame1, state="readonly")
		self.combo1["values"] = ports
		self.combo1.grid(row=0, column=1)
		Label(self.frame1, text='Esclavo', bg="grey").grid(row=0, column=2)
		self.ent2 = Entry(self.frame1)
		self.ent2.grid(row=0, column=3)
		self.conn_button = Button(self.frame1, text='Conectar', command=self.conect)
		self.conn_button.grid(row=0, column=4)

        # Creamos los widgets que forman el frame2
		self.b_sen01 = Label(self.frame2, text='sen_01', width=10)
		self.b_sen01.grid(row=2, column=0)
		self.b_sen02 = Label(self.frame2, text='sen_02', width=10)
		self.b_sen02.grid(row=3, column=0)
		self.b_sen03 = Label(self.frame2, text='sen_03', width=10)
		self.b_sen03.grid(row=4, column=0)
		self.b_sen04 = Label(self.frame2, text='sen_04', width=10)
		self.b_sen04.grid(row=5, column=0)
		self.b_sen05 = Label(self.frame2, text='sen_05', width=10)
		self.b_sen05.grid(row=6, column=0)
		self.b_sen06 = Label(self.frame2, text='sen_06', width=10)
		self.b_sen06.grid(row=7, column=0)
		self.b_sen07 = Label(self.frame2, text='sen_07', width=10)
		self.b_sen07.grid(row=8, column=0)
		self.b_sen08 = Label(self.frame2, text='sen_08', width=10)
		self.b_sen08.grid(row=9, column=0)
		self.b_fa_vis = Label(self.frame2, text='fa_vis', width=10)
		self.b_fa_vis.grid(row=10, column=0)
		self.b_fal_ad = Label(self.frame2, text='fal_ad', width=10)
		self.b_fal_ad.grid(row=11, column=0)
		self.b_fal_ad_au = Label(self.frame2, text='fal_ad_au', width=10)
		self.b_fal_ad_au.grid(row=12, column=0)
		self.b_fa_i_1 = Label(self.frame2, text='fa_i_1', width=10)
		self.b_fa_i_1.grid(row=13, column=0)
		self.b_fa_i_2 = Label(self.frame2, text='fa_i_2', width=10)
		self.b_fa_i_2.grid(row=14, column=0)
		self.b_fl_vis = Label(self.frame2, text='fl_vis', width=10)
		self.b_fl_vis.grid(row=15, column=0)
		self.b_fa_gen = Label(self.frame2, text='fa_gen', width=10)
		self.b_fa_gen.grid(row=16, column=0)
		self.b_fa_asp = Label(self.frame2, text='fa_asp', width=10)
		self.b_fa_asp.grid(row=17, column=0)

		#Creamos los widgets que forman el frame3
		self.filename = PhotoImage(file="Gases.png")
		self.cv = tk.Canvas(self.frame3, width=650, height=450)
		self.cv.create_image(0,0, anchor=tk.NW, image=self.filename)
		self.cv.create_text(65,  235, text="Oxígeno")
		self.cv.create_text(165,  235, text="Monóxido")
		self.cv.create_text(265,  235, text="Humedad")
		self.cv.create_text(365,  235, text="Temperatura")
		self.cv.create_text(465,  235, text="Opacidad")
		self.cv.create_text(565,  235, text="PLA")
		self.cv.pack()

		self.frame1.pack(side=TOP, fill=X)
		self.frame2.pack(side=LEFT, fill=Y)
		self.frame3.pack(side=RIGHT)
		self.main_window.mainloop()

	def conect(self):
		# Creacion de la comunicación RTU y se mantendrá abierta hasta
		# que se cierre la aplicación

		# guardo sólo la primera palabra del string
		puerto = str(self.combo1.get()).split()[0]
		slave = int(self.ent2.get())

		# TEST
		print(puerto, "  ", slave)
		self.instrument = minimalmodbus.Instrument(puerto, slave, mode='rtu')
		self.instrument.serial.baudrate = 1200  # Baud
		self.instrument.serial.bytesize = 8
		self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
		self.instrument.serial.stopbits = 1
		self.instrument.close_port_after_each_call = FALSE
		self.conn_button.configure(state="pressed")
		self.refresh_data()

	def refresh_data(self):
		"""Función de refresco de datos"""

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
		"""función para lectura de datos"""

		try:
		    value = self.instrument.read_register(reg, dec, fun)
		    return value
		except IOError:
		    messagebox.showinfo("Información", "Algo ha ido mal al leer el registro: {}".format(reg))

app = bandejas_app()
