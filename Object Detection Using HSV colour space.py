import cv2
import numpy as np

cap = cv2.VideoCapture(0)


cv2.namedWindow("Bars")
cv2.createTrackbar("LH", "Bars",   0, 255, lambda m:m)
cv2.createTrackbar("LS", "Bars",   0, 255, lambda m:m)
cv2.createTrackbar("LV", "Bars",   0, 255, lambda m:m)
cv2.createTrackbar("UH", "Bars", 128, 255, lambda m:m)
cv2.createTrackbar("US", "Bars", 128, 255, lambda m:m)
cv2.createTrackbar("UV", "Bars", 128, 255, lambda m:m)


while cap.isOpened():

    Done, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    if Done:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lh = cv2.getTrackbarPos("LH", "Bars")
        ls = cv2.getTrackbarPos("LS", "Bars")
        lv = cv2.getTrackbarPos("LV", "Bars")
        uh = cv2.getTrackbarPos("UH", "Bars")
        us = cv2.getTrackbarPos("US", "Bars")
        uv = cv2.getTrackbarPos("UV", "Bars")
    
        Lowers = np.array([lh, ls, lv])
        Uppers = np.array([uh, us, uv])
    
        mask = cv2.inRange(hsv_frame, Lowers, Uppers)
        
        target = cv2.bitwise_and(frame, frame, mask = mask)
        
        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("Result", target)
        
        if cv2.waitKey(1) == ord("q"):
            break
    
cap.release()
cv2.destroyAllWindows()