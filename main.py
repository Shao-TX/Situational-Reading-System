# %%
import cv2
import numpy as np
import time

from utils.toArduino import Control_Arduino, Reset_Arduino
from utils.toAruco import To_Aruco

# %%
device_state = [0, 0, 0, 0]
last_device_id = None
timer = 0

# %%
if __name__ == "__main__":
    Reset_Arduino()
    cap = cv2.VideoCapture(0)

    while (True):
        # 擷取影像
        ret, frame = cap.read()

        frame, markerCorners, markerIds, rejectedCandidates= To_Aruco(frame)

        print(timer)

        if markerIds != None:
            device_id = int(markerIds[0][0])
            if(timer==0 or device_id != last_device_id):
                print(type(device_id))
                last_device_id = device_id
                print("Device On : ", device_id)

                device_state = [0]*4 # [0, 0, 0, 0]
                device_state[device_id] = 1

            timer = 150 # 5 Second : Because opencv is 30 fps => 150 = 30*5

        elif(timer>0) :
            timer -= 1
            if(timer==0):
                print("Device Off")
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