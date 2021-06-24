from occvutil import changedH,changedS,changedV

#色相・彩度・明度変換
def convertframe(frame):
    return changedH(frame, -100)
    #return changedS(frame, 1.5, 20)
    #return changedV(frame, 1.5, 20)


    #changedS 彩度変換
    #changedV 明度変換 