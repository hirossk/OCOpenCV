import os
import cv2
import numpy as np
from occvutil import cvtextdraw,changedH,changedS,changedV
from convert import convertframe

def main():
    var = 0
    # VideoCapture オブジェクトを取得します
    capture = cv2.VideoCapture(0)

    casceade_path = os.path.join(
        cv2.data.haarcascades, "haarcascade_frontalface_alt.xml"
    )

    cascade = cv2.CascadeClassifier(casceade_path)

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
            imgface = frame3
        else:  
            #できなかったとき
            text = "顔が認識できませんでした。"
            x, y = 180,280
            fontPIL = "meiryo.ttc" # メイリオ
            size = 40
            colorBGR = (255,0,0) # cv2.putText()と同じく、BGRの順で定義

            imgface = cvtextdraw(img = frame3,
                            text = text,
                            org = (x,y),
                            fontFace = fontPIL,
                            fontScale = size,
                            color = colorBGR)
        
        #カラーからモノクロへ変換
        gry = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        #エッジ強調画像の生成
        edges = cv2.Canny(gry,100,200)

        #色を変換する
        hsv = convertframe(frame1,var)

        #エッジ協調の出力
        #cv2.imshow('Edges',edges)
        #グレイ映像の出力
        #cv2.imshow('gray',gry)
        #hsv変換後の出力
        cv2.imshow('ChangedHSV',hsv)
        #顔認識の出力
        #cv2.imshow('Face pick', imgface)

        #キー入力で終了します
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
                break
        if key & 0xFF == ord('u'):
            if var < 200:
                var = var + 10
        if key & 0xFF == ord('d'):
            if var > -200:
                var = var - 10
        

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
