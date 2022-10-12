import cv2

def Show_Image(img_path):
    img = cv2.imread(img_path)
    cv2.imshow('img', img) 
    cv2.waitKey(0)