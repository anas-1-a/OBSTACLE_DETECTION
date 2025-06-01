import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()
while True :
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break
    cv2.imshow(" live", frame) # show the frame   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # press q to quit
cap.release()
cv2.destroyAllWindows()
