import cv2

# Create Dictionary of Aruco
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# Initialize the detector parameters using default values
parameters = cv2.aruco.DetectorParameters_create()

def To_Aruco(frame):

    # 調整圖片大小
    frame = cv2.resize(frame, None, fx=0.7, fy=0.7,
                        interpolation=cv2.INTER_CUBIC)

    # 彩色轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the markers in the image
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(
        gray, dictionary, parameters=parameters)

    return frame, markerCorners, markerIds, rejectedCandidates