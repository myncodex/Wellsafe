
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import cv2
import serial



# Load the video or image from the source
source = cv2.VideoCapture('video.mp4')

# Create a background subtractor object
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

def person(frame):
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
port = "COM7"  # Replace with the correct port for your Arduino
baudrate = 9600  # Set the baudrate to match your Arduino program

# Create a serial object
ser = serial.Serial(port, baudrate)

# Read and print data from Arduino


def openwindow():
    path_to_script ="C:/Users/User/Desktop/N2M2/new.py"
    subprocess.run(["python", path_to_script])

def motorup():
    data = "f"
    ser.write(data.encode())

def motordown():
    data = "b"
    ser.write(data.encode())

def servoup():
    data = "u"
    ser.write(data.encode())

def servodown():
    data = "d"
    ser.write(data.encode())

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\N2M2\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    362.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    71.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    199.0,
    377.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    215.0,
    445.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    215.0,
    506.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    187.0,
    568.0,
    image=image_image_6
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: openwindow(),
    relief="flat"
)
button_1.place(
    x=748.0,
    y=344.0,
    width=200.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: motorup(),
    relief="flat"
)
button_2.place(
    x=748.0,
    y=441.0,
    width=200.0,
    height=65.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: motordown(),
    relief="flat"
)
button_3.place(
    x=997.0,
    y=441.0,
    width=200.0,
    height=65.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: servoup(),
    relief="flat"
)
button_4.place(
    x=748.0,
    y=538.0,
    width=200.0,
    height=65.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: servodown(),
    relief="flat"
)
button_5.place(
    x=997.0,
    y=538.0,
    width=200.0,
    height=65.0
)

text1=canvas.create_text(
    308.0,
    360.0,
    anchor="nw",
    text="Checking",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

text2=canvas.create_text(
    370.0,
    430.0,
    anchor="nw",
    text="Checking",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

text3=canvas.create_text(
    344.0,
    492.0,
    anchor="nw",
    text="Checking",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

text4=canvas.create_text(
    289.0,
    553.0,
    anchor="nw",
    text="Checking",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

def status():

    a=[]
    # Read a line of data from Arduino
    line = ser.readline().decode().rstrip()
    
    # Print the received data
    
    a=list(line.split('    '))
    canvas.itemconfig(text2, text=a[1][3:]+'ppm')
    canvas.itemconfig(text3, text=a[2][2:]+'degC')
    canvas.itemconfig(text4, text=a[3][2:]+'RH')

def camstatus():
    ret, frame = source.read()
    person_detected = person(frame)
    if person_detected:
        canvas.itemconfig(text1, text='Movement Detected')
    else:
        canvas.itemconfig(text1, text='Movement not Detected')

window.after(1000,status)
window.after(3000,camstatus)
window.resizable(False, False)
window.title("WellSafe")
window.mainloop()
