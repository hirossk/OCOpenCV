import cv2
import numpy as np
5# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)
print(capture)
while(True):
    ret, frame = capture.read()
    # resize the window
    window1 = (800, 600)
    window2 = (800, 600)
    window3 = (800, 600)
    frame1 = cv2.resize(frame,window1)
    frame2 = cv2.resize(frame,window2)
    frame3 = cv2.resize(frame,window3)
    
    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    lower_color = np.array([20, 50, 50])
    upper_color = np.array([255, 255, 255])

    img_mask = cv2.inRange(hsv, lower_color, upper_color)
    img_color = cv2.bitwise_and(frame2, frame2, mask=img_mask)
    edges = cv2.Canny(frame1,100,200)
    cv2.imshow('Edges',edges)
    cv2.imshow('Masks',img_color)
    cv2.imshow('Origin', frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()