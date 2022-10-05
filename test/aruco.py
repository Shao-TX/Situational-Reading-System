# %%
import cv2
import numpy as np

# %%
# Create Dictionary of Aruco
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# Initialize the detector parameters using default values
parameters = cv2.aruco.DetectorParameters_create()

#%%
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while (True):
        # 擷取影像
        ret, frame = cap.read()

        # 調整圖片大小
        frame = cv2.resize(frame, None, fx=0.7, fy=0.7,
                           interpolation=cv2.INTER_CUBIC)

        # 彩色轉灰階
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the markers in the image
        markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(
            gray, dictionary, parameters=parameters)

        print(markerIds)

        cv2.aruco.drawDetectedMarkers(frame, markerCorners, markerIds)

        # 顯示圖片
        cv2.imshow('live', frame)
        #cv2.imshow('live', gray)

        # 按下 q 鍵離開迴圈
        if cv2.waitKey(1) == ord('q'):
            break

    # 釋放該攝影機裝置
    cap.release()
    cv2.destroyAllWindows()
