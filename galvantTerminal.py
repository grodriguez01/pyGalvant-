'''
Description:
This program uses pySerial python library 
to communicate with the galvantGPIB Adapter.
Forwarding input from python onto the serial console.  
Version: 1.0

NOTE: Additional system requirement.
    1. Virtual com port driver
    2. Python 3.+

NOTE:The address is different depending on 
    your Opertating System.
    You can use pySerial's tool to see the ports 
    that available. 

excute this in a terminal to list ports:
    python -m serial.tools.list_ports

#depends what port you plug it on. 
Address: /dev/ttyUSB0 

'''
import serial 
import time 

port = serial.Serial('/dev/ttyUSB0', baudrate=460800,stopbits=1,timeout=1)
#                      ^PORT ADDRESS CHANGE THIS^        
def write_read(cmd):
    '''
    This function sends input to the native serial console
    and prints output. 

    Parameters:
    cmd: a str type, command.
    
    Returns:
    a str type. 
    '''
    port.write(cmd.encode() + '\r'.encode())
    #port.readline() #prevent ts
    time.sleep(.1)
    output = port.read_until('CR').decode()
    
    if output == '':
        error_status = write_read('SYST:ERR?')
        if 'No' in error_status:
            return '**COMMAND EXECUTED**'
        else:
            return error_status
    return output
   
def main():
    ''' 
    Continuous user prompt  until exit string 
    is passed in. 
    ''' 
    
    print('Welcome to the pyGalvant Terminal!\n')
    while True:
        user_input = input('galvant:> ')

        if user_input != 'exit':
            print(write_read(user_input))
               
        else:
            print('Exiting pyGalvant')
            port.close()
            return 
main()




