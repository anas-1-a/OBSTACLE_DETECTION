import cv2
import numpy as np
import serial
cap = cv2.VideoCapture(0)
ser = serial.Serial('COM4', 9600) # choose the COM

while True :
        value to sen to arduino= 320
        data_to_send = f"{value to sen to arduino}\n"
        ser.write(data_to_send.encode())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
