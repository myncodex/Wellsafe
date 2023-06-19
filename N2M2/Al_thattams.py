import cv2
import serial



# Load the video or image from the source
source = cv2.VideoCapture('video.mp4')

# Create a background subtractor object
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

def check_person_detected(frame):
    # Apply background subtraction
    fg_mask = bg_subtractor.apply(frame)

    # Apply morphological operations to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)

        # Filter out small contours
        if area > 1000:
            return True

    return False


# Configure the serial port
port = "COM5"  # Replace with the correct port for your Arduino
baudrate = 9600  # Set the baudrate to match your Arduino program

# Create a serial object
ser = serial.Serial(port, baudrate)

# Read and print data from Arduino
def status():

    a=[]
    # Read a line of data from Arduino
    line = ser.readline().decode().rstrip()
    
    # Print the received data
    
    a=list(line.split('    '))
    print(a)


