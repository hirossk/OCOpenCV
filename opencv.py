import os
import cv2
import numpy as np
from occvutil import cvtextdraw,changedH,changedS,changedV
from convert import convertframe

def main():
    # VideoCapture オブジェクトを取得します
    capture = cv2.VideoCapture(0)

    casceade_path = os.path.join(
        cv2.data.haarcascades, "haarcascade_frontalface_alt.xml"
    )

    cascade = cv2.CascadeClassifier(casceade_path)

    print(capture)
    while(True):
        ret, frame = capture.read()
        # resize the window
        window = (800, 600)
        frame1 = cv2.resize(frame,window)
        frame2 = cv2.resize(frame,window)
        frame3 = cv2.resize(frame,window)
        frame4 = cv2.resize(frame,window)

        face_list = cascade.detectMultiScale(frame)

        color=(0, 0, 255)

        #顔認識ができたかどうか確認
        if len(face_list) > 0 :
            #できたとき
            for face in face_list :
                x, y, w, h = face 
                cv2.rectangle(frame3, (x,y), (x+w*2, y+h*2), color, thickness=2) 
        else:  
            #できなかったとき
            text = "顔が認識できませんでした。"
            x, y = 180,280
            fontPIL = "meiryo.ttc" # メイリオ
            size = 40
            colorBGR = (255,0,0) # cv2.putText()と同じく、BGRの順で定義

            frame3 = cvtextdraw(img = frame3,
                            text = text,
                            org = (x,y),
                            fontFace = fontPIL,
                            fontScale = size,
                            color = colorBGR)
        
        #色の濃さ
        #hsv = cv2.cvtColor(frame4, cv2.COLOR_BGR2HSV)
        gry = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        #lower_color = np.array([100, 0, 0])
        #upper_color = np.array([120, 255, 255])

        #ORB
        detector = cv2.ORB_create()
        keypoints = detector.detect(gry)

        #img_mask = cv2.inRange(hsv, lower_color, upper_color)
        #filter = cv2.bitwise_and(frame4, frame4, mask=img_mask)

        #エッジ強調
        edges = cv2.Canny(gry,100,200)

        #色を変換する
        frame1 = convertframe(frame1)


        cv2.imshow('Edges',edges)
        #cv2.imshow('Masks',gry)
        cv2.imshow('gray',gry)
        cv2.imshow('Changed H',frame1)
        frame3 = cv2.drawKeypoints(frame3,keypoints,None)
        cv2.imshow('Face pick', frame3)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
