import serial

# Configure the serial port
port = "COM5"  # Replace with the correct port for your Arduino
baudrate = 9600  # Set the baudrate to match your Arduino program

# Create a serial object
ser = serial.Serial(port, baudrate)

# Read and print data from Arduino
while True:

    a=[]
    # Read a line of data from Arduino
    line = ser.readline().decode().rstrip()
    
    # Print the received data
    
    a=list(line.split('    '))
    print(a)



