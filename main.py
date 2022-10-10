# %%
import cv2
import numpy as np
import time

from utils.toArduino import Control_Arduino, Reset_Arduino
from utils.img2aruco import To_Aruco

# %%
device_state = [0, 0, 0, 0]
timer = 0

# %%
if __name__ == "__main__":
    Reset_Arduino()
    cap = cv2.VideoCapture(0)

    while (True):
        # 擷取影像
        ret, frame = cap.read()

        frame, markerCorners, markerIds, rejectedCandidates= To_Aruco(frame)


        if markerIds != None:
            device_id = int(markerIds[0][0])
            print(device_id)

            device_state = [0]*4 # [0, 0, 0, 0]
            device_state[device_id] = 1
           
        else :
            print("None")
            device_state = [0] * 4

        Control_Arduino(device_state)

        # 顯示圖片
        cv2.aruco.drawDetectedMarkers(frame, markerCorners, markerIds)
        cv2.imshow('live', frame)

        # 按下 q 鍵離開迴圈
        if cv2.waitKey(1) == ord('q'):
            break

    # 釋放該攝影機裝置
    cap.release()
    cv2.destroyAllWindows()

    Reset_Arduino()