import cv2
import time
import multiprocessing as mp
import threading

from playsound import playsound

def Play_Music(song_path):
    playsound(song_path)

def Show_Image(img_path):
    img = cv2.imread(img_path)
    cv2.imshow('img', img) 

    cv2.waitKey(0)
    # cv2.destroyAllWindows()

print("process test")
if __name__ == "__main__":
    p1 = mp.process(target=Play_Music, args=("song1.mid",))
    p2 = mp.process(target=Show_Image, args=("img1.jpg",))
    p1.start()
    p2.start()

    a = input("y or n : ")
    if(a == "y"):
        p1.terminate()
        print('stop p1 process')
        p1.join()

        p2.terminate()
        print('stop p2 process')
        p2.join()

    p1 = mp.process(target=Play_Music, args=("song2.mid",))
    p1.start()

    p2 = mp.process(target=Show_Image, args=("img2.jpg",))
    p2.start()