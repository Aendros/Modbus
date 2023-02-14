#!/usr/bin/env python
import minimalmodbus


def create_conn():
    #Creacion de la comunicación RTU y se mantenerto, slave):
    # drá abierta hasta
    #que se cierre la aplicación

    instrument = minimalmodbus.Instrument("COM2", "1",minimalmodbus.MODE_RTU)  # port name, slave address (in decimal)
    instrument.serial.baudrate = 9600   # Baud
    instrument.serial.bytesize = 8
    instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.close_port_after_each_call = FALSE

    refresh_data(instrument)

# datum=[SEN_01, SEN_02, SEN_03, SEN_04, SEN_05, SEN_06, SEN_07, SEN_08, SEN_FA_VIS, SEN_FAL_AD, SEN_FAL_AD_AU, SEN_FA_I_1, SEN_FA_I_2, SEN_FL_VIS, SEN_FA_GEN, SEN_FA_ASP]

def refresh_data(instrument):
    SEN_01 = instrument.read_register(4096, 0, 4)  # Read Analog Input Register (HR)
    SEN_02 = instrument.read_register(4097, 0, 4)
    SEN_03 = instrument.read_register(4098, 0, 4)
    SEN_04 = instrument.read_register(4099, 0, 4)
    SEN_05 = instrument.read_register(4100, 0, 4)
    SEN_06 = instrument.read_register(4101, 0, 4)
    SEN_07 = instrument.read_register(4102, 0, 4)
    SEN_08 = instrument.read_register(4103, 0, 4)
    SEN_FA_VIS = instrument.read_register(4352, 0, 4)
    SEN_FAL_AD = instrument.read_register(4353, 0, 4)
    SEN_FAL_AD_AU = instrument.read_register(4354, 0, 4)
    SEN_FA_I_1 = instrument.read_register(4355, 0, 4)
    SEN_FA_I_2 = instrument.read_register(4356, 0, 4)
    SEN_FL_VIS = instrument.read_register(4357, 0, 4)
    SEN_FA_GEN = instrument.read_register(4358, 0, 4)
    SEN_FA_ASP = instrument.read_register(4359, 0, 4)
    print([SEN_01, SEN_02, SEN_03, SEN_04, SEN_05, SEN_06, SEN_07, SEN_08, SEN_FA_VIS, SEN_FAL_AD,
          SEN_FAL_AD_AU, SEN_FA_I_1, SEN_FA_I_2, SEN_FL_VIS, SEN_FA_GEN, SEN_FA_ASP])


# print(datum)