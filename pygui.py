#!/usr/bin/env python
import PySimpleGUI as sg
import cv2
import numpy as np

def main():

    sg.theme('Black')

    # efine the window layout
    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Record',key='Record2', size=(10, 1), font='Helvetica 14'),
               sg.Button('Edge', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Helvetica 14'),
               sg.Button('Exit', size=(10, 1), font='Helvetica 14'), ],
              [sg.Button('Record',key='Record', size=(10, 1), font='Helvetica 14'),
               sg.Button('Edge', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Helvetica 14'),
               sg.Button('Exit', size=(10, 1), font='Helvetica 14'), ]]

    # ウィンドウの表示
    window = sg.Window('画像処理・認識プログラム',
                       layout, location=(200, 200))

    # 入力を待ってループする
    cap = cv2.VideoCapture(0)
    recording = False
    edge = False

    while True:
        event, values = window.read(timeout=20)
        print(event)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return
        elif event == 'Record':
            recording = not recording

        elif event == 'Stop':
            recording = False
            img = np.full((1, 1), 0)
            # this is faster, shorter and needs less includes
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['image'].update(data=imgbytes)
        elif event == 'Edge':
            edge = not edge
        if recording:
            ret, frame = cap.read()
            if edge == True:
                frame = cv2.Canny(frame,100,200)
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
            window['image'].update(data=imgbytes)


main()