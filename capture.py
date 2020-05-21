# https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
# https://stackoverflow.com/questions/41586429/opencv-saving-images-to-a-particular-folder-of-choice
# https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file

import cv2
import os 
import time

def pixelate(path,imgName):
    input = cv2.imread(os.path.join(path,imgName))
    height, width = input.shape[:2]

    # Desired "pixelated" size
    w, h = (100, 100)

    # Resize input to "pixelated" size
    temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

    # Initialize output image
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    # cv2.imshow('Input', input)
    cv2.imshow('Output', output)
    t = time.time()
    path = r"C:\Users\Ananya\projects\Pixelate\pixelated"
    img_name = "opencv_pixelated_{}{}.png".format(img_counter,t) 
    cv2.imwrite(os.path.join(path,img_name), output)


    cv2.waitKey(0)

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        t = time.time()
        img_name = "opencv_frame_{}{}.png".format(img_counter,t) 
        path = r"C:\Users\Ananya\projects\Pixelate\images"
        cv2.imwrite(os.path.join(path,img_name), frame)
        
        print("{} written!".format(img_name))
        img_counter += 1
        pixelate(path,img_name)

cam.release()

cv2.destroyAllWindows()


