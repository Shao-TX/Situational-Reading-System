# %%
import cv2
import json
import time
import numpy as np
import multiprocessing as mp

from utils.toAruco import To_Aruco
from utils.generate_music import Play_Music
from utils.generate_image import Show_Image

try:
    from utils.toArduino import Control_Arduino, Reset_Arduino
except:
    pass

def stop_process(p1, p2):
    p1.terminate()
    p1.join()
    print('stop p1 process')
    p2.terminate()
    p2.join()
    print('stop p2 process')

# %%
device_state = [0, 0, 0, 0]
last_page_id = None
process_cnt = False
timer = 0

# %%
if __name__ == "__main__":
    Reset_Arduino()
    cap = cv2.VideoCapture(0)

    while (True):
        # 擷取影像
        ret, frame = cap.read()

        frame, markerCorners, markerIds, rejectedCandidates= To_Aruco(frame)

        # print(timer)
        print(markerIds)

        if not isinstance(markerIds, np.ndarray):
            pass
        elif len(markerIds) != 1:
            print("More than one marker detected.")
        else:
            page_id = int(markerIds[0][0])
            if(timer==0 or page_id != last_page_id):
                last_page_id = page_id
                print("Page : ", page_id)

                with open('books/books.json') as f:
                    data = json.load(f)
                    page = "page" + str(page_id)
                    image_path = data[page]['image']
                    music_path = data[page]['music']
                    device_state = data[page]['device']

                # 避免第一次進入沒有進程
                if(process_cnt != False): stop_process(p1, p2)

                # 執行新的進程
                p1 = mp.Process(target=Play_Music, args=(music_path,))
                p1.start()
                p2 = mp.Process(target=Show_Image, args=(image_path,))
                p2.start()
                process_cnt = True

            timer = 150 # 5 Second : Because opencv is 30 fps => 150 = 30*5

        if(timer>0) :
            timer -= 1
            if(timer==0):
                print("Device Off")
                device_state = [0] * 4
            
                stop_process(p1, p2)

        Control_Arduino(device_state)

        # 顯示圖片
        cv2.aruco.drawDetectedMarkers(frame, markerCorners, markerIds)
        cv2.imshow('live', frame)

        # 按下 q 鍵離開迴圈
        if cv2.waitKey(1) == ord('q'): 
            stop_process(p1, p2)
            break

    # 釋放該攝影機裝置
    cap.release()
    cv2.destroyAllWindows()

    Reset_Arduino()