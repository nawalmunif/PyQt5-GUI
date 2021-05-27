import cv2

def resize(img,scale_percentage):
    width = int(img.shape[1]*scale_percentage)
    height = int(img.shape[0]*scale_percentage)
    dimension = (height, width)
    resized = cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)
    cv2.imwrite('resized.jpg',resized)

img = cv2.imread('img_1.png')
resize(img,0.15)