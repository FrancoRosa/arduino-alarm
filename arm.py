import serial
port = 'COM10'
ser = serial.Serial(port = port, rtscts = True, dsrdtr=True)  # open serial port
ser.write(b'arm\n')     # write a string
ser.close()             # close port