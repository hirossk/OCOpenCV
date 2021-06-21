import cv2
import os
import numpy as np

capture = cv2.VideoCapture(0)


while(True):
    ret, frame = capture.read()
    window1 = (800, 600)
    cimg = cv2.resize(frame,window1)
#img = capture.read()
    cimg = cv2.medianBlur(cimg,5)
    cimg = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
    #cimg = cv2.cvtColor(cimg,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT, 
        dp=1.0, minDist=10, param1=80, param2=95)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()