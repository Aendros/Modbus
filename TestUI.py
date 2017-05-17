import minimalmodbus
from tkinter import *
from tkinter import ttk


class BandejasApp(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        # Añadir imagen de fondo a la pantalla
        filename = PhotoImage(file="Gases.png")
        background_label = Label(self, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.resizable(width='False', height='False')
        self.geometry('650x450')

        # Creamos los widgets que forman la UI
     #   Label(self, text='Puerto').grid(row=0, column=0)
     #   dpl1 = ttk.Combobox(self)
        dpl1['values'] = ['COM1', 'COM2']
        dpl1.grid(row=0, column=1)
        Label(self, text='Esclavo').grid(row=0, column=2)
        ent2 = Entry(self)
        ent2.grid(row=0, column=3)
        conn_button = Button(self, text='Conectar')
        conn_button.grid(row=0, column=4)
        self.grid()

#    def create_conn(puerto, slave):
#        '''
#        Creacion de la comunicación RTU y se mantendrá abierta hasta
#        que se cierre la aplicación
#        '''
#        instrument = minimalmodbus.Instrument(puerto, slave,
#                                              minimalmodbus.MODE_RTU)  # port name, slave address (in decimal)
#        instrument.serial.baudrate = 9600  # Baud
#        instrument.serial.bytesize = 8
#        instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
#        instrument.serial.stopbits = 1
#        instrument.close_port_after_each_call = FALSE

        #self.refresh_data(instrument)

    # datum=[SEN_01, SEN_02, SEN_03, SEN_04, SEN_05, SEN_06, SEN_07, SEN_08, SEN_FA_VIS, SEN_FAL_AD, SEN_FAL_AD_AU, SEN_FA_I_1, SEN_FA_I_2, SEN_FL_VIS, SEN_FA_GEN, SEN_FA_ASP]

#    def refresh_data(self):
#        SEN_01 = self.read_register(4096, 0, 4)  # Read Analog Input Register (HR)
#        SEN_02 = self.read_register(4097, 0, 4)
#        SEN_03 = self.read_register(4098, 0, 4)
#        SEN_04 = self.read_register(4099, 0, 4)
#        SEN_05 = self.read_register(4100, 0, 4)
#        SEN_06 = self.read_register(4101, 0, 4)
#        SEN_07 = self.read_register(4102, 0, 4)
#        SEN_08 = self.read_register(4103, 0, 4)
#        SEN_FA_VIS = self.read_register(4352, 0, 4)
#        SEN_FAL_AD = self.read_register(4353, 0, 4)
#        SEN_FAL_AD_AU = self.read_register(4354, 0, 4)
#        SEN_FA_I_1 = self.read_register(4355, 0, 4)
#        SEN_FA_I_2 = self.read_register(4356, 0, 4)
#        SEN_FL_VIS = self.read_register(4357, 0, 4)
#        SEN_FA_GEN = self.read_register(4358, 0, 4)
#        SEN_FA_ASP = self.read_register(4359, 0, 4)
#        # print(SEN_01, SEN_02, SEN_03, SEN_04, SEN_05, SEN_06, SEN_07, SEN_08, SEN_FA_VIS, SEN_FAL_AD,
#        # SEN_FAL_AD_AU, SEN_FA_I_1, SEN_FA_I_2, SEN_FL_VIS, SEN_FA_GEN, SEN_FA_ASP])

if __name__ == '__main__':
    app = BandejasApp(None)
    app.title('BandejasApp')
    app.mainloop()