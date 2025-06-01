import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 480)

cv2.createTrackbar("Black_H_Min", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("Black_S_Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Black_V_Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Black_H_Max", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("Black_S_Max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Black_V_Max", "Trackbars", 50, 255, nothing)

cv2.createTrackbar("White_H_Min", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("White_S_Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("White_V_Min", "Trackbars", 200, 255, nothing)
cv2.createTrackbar("White_H_Max", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("White_S_Max", "Trackbars", 30, 255, nothing)
cv2.createTrackbar("White_V_Max", "Trackbars", 255, 255, nothing)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture frame.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    bh_min = cv2.getTrackbarPos("Black_H_Min", "Trackbars")
    bs_min = cv2.getTrackbarPos("Black_S_Min", "Trackbars")
    bv_min = cv2.getTrackbarPos("Black_V_Min", "Trackbars")
    bh_max = cv2.getTrackbarPos("Black_H_Max", "Trackbars")
    bs_max = cv2.getTrackbarPos("Black_S_Max", "Trackbars")
    bv_max = cv2.getTrackbarPos("Black_V_Max", "Trackbars")

    wh_min = cv2.getTrackbarPos("White_H_Min", "Trackbars")
    ws_min = cv2.getTrackbarPos("White_S_Min", "Trackbars")
    wv_min = cv2.getTrackbarPos("White_V_Min", "Trackbars")
    wh_max = cv2.getTrackbarPos("White_H_Max", "Trackbars")
    ws_max = cv2.getTrackbarPos("White_S_Max", "Trackbars")
    wv_max = cv2.getTrackbarPos("White_V_Max", "Trackbars")

    lower_black = np.array([bh_min, bs_min, bv_min])
    upper_black = np.array([bh_max, bs_max, bv_max])
    lower_white = np.array([wh_min, ws_min, wv_min])
    upper_white = np.array([wh_max, ws_max, wv_max])

    mask_black = cv2.inRange(hsv, lower_black, upper_black)
    mask_white = cv2.inRange(hsv, lower_white, upper_white)

    mask_bw = cv2.bitwise_or(mask_black, mask_white)
    mask_colored = cv2.bitwise_not(mask_bw)

    contours, _ = cv2.findContours(mask_colored, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    coords = None
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            center_x = x + w // 2
            center_y = y + h // 2
            coords = (center_x, center_y)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), 7, (255, 67, 0), -1)
            break

    frame_center = (frame.shape[1] // 2, frame.shape[0] // 2)

    if coords is not None:
        diff_x = coords[0] - frame_center[0]
        diff_y = coords[1] - frame_center[1]
        surface = (x + w) * (y + h)
        if surface > 20000:
            print("mrigell")
        else:
            print("moch mrigel")

        if diff_x < 0:
            print("left:")#, diff_x)
        else:
            print("right:")#, diff_x)
        difference_x = diff_x + 320

        # data_to_send = f"{difference_x},{surface}\n"
        # ser.write(data_to_send.encode())
        # print(f"Sent: {data_to_send.strip()}")

    cv2.imshow('Frame', frame)
    cv2.imshow('Colored Mask', mask_colored)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
