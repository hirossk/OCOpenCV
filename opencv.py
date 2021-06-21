import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def pil2cv(imgPIL):
    imgCV_RGB = np.array(imgPIL, dtype = np.uint8)
    imgCV_BGR = np.array(imgPIL)[:, :, ::-1]
    return imgCV_BGR

def cv2pil(imgCV):
    imgCV_RGB = imgCV[:, :, ::-1]
    imgPIL = Image.fromarray(imgCV_RGB)
    return imgPIL

def cv2_putText_1(img, text, org, fontFace, fontScale, color):
    x, y = org
    b, g, r = color
    colorRGB = (r, g, b)
    imgPIL = cv2pil(img)
    draw = ImageDraw.Draw(imgPIL)
    fontPIL = ImageFont.truetype(font = fontFace, size = fontScale)
    draw.text(xy = (x,y), text = text, fill = colorRGB, font = fontPIL)
    """
    後でここに追加する
    """
    imgCV = pil2cv(imgPIL)
    return imgCV

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
    window1 = (800, 600)
    window2 = (800, 600)
    window3 = (800, 600)
    frame1 = cv2.resize(frame,window1)
    frame2 = cv2.resize(frame,window2)
    frame3 = cv2.resize(frame,window3)

    face_list = cascade.detectMultiScale(frame)

    color=(0, 0, 255)

    if len(face_list) > 0 :
        for face in face_list :
            x, y, w, h = face 
            cv2.rectangle(frame3, (x,y), (x+w*2, y+h*2), color, thickness=2) 
    else:  
        # 独自関数で日本語テキストを描写する
        text = "顔が認識できませんでした。"
        x, y = 180,280
        fontPIL = "meiryo.ttc" # メイリオ
        size = 40
        colorBGR = (255,0,0) # cv2.putText()と同じく、BGRの順で定義

        frame3 = cv2_putText_1(img = frame3,
                        text = text,
                        org = (x,y),
                        fontFace = fontPIL,
                        fontScale = size,
                        color = colorBGR)
    
    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    gry = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    lower_color = np.array([20, 50, 50])
    upper_color = np.array([200, 200, 200])

    #ORB
    detector = cv2.ORB_create()
    keypoints = detector.detect(gry)

    img_mask = cv2.inRange(hsv, lower_color, upper_color)
    img_color = cv2.bitwise_and(frame2, frame2, mask=img_mask)
    edges = cv2.Canny(frame1,100,200)
    cv2.imshow('Edges',edges)
    #cv2.imshow('Masks',img_color)
    cv2.imshow('gray',gry)
    frame3 = cv2.drawKeypoints(frame3,keypoints,None)
    cv2.imshow('Face pick', frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

