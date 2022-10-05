#%%
import cv2
import numpy as np

dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

for i in range(4):
    markerImage = np.zeros((20, 20), dtype=np.uint8)
    markerImage = cv2.aruco.drawMarker(dictionary, i, 20, markerImage, 1)

    save_name = "aruco_marker_" + str(i) + ".png"
    cv2.imwrite(save_name, markerImage)

# %%
