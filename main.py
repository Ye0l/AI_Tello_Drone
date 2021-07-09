import cv2 as cv

print('opencv version: ' + cv.__version__)
imagepass = "./mountain.jpeg"
img = cv.imread(imagepass, cv.IMREAD_UNCHANGED)
height, width, channel = img.shape
title = 'image'
x, y = 100, 100

while True:
    cv.imshow(title, img)
    key = cv.waitKey(1) & 0xFF
    cv.moveWindow(title, x, y)
    if key is not 255:
        print(key)
        if key == 27: # esc
            break
        if key == ord('w'):
            y -= 10
        if key == ord('s'):
            y += 10
        if key == ord('a'):
            x -= 10
        if key == ord('d'):
            x += 10
        if key == ord('r'):
            img = cv.resize(img, (width*2, height*2))
        if key == ord('t'):
            img = cv.imread(imagepass, cv.IMREAD_UNCHANGED)
            height, width, channel = img.shape
        if key == ord('c'):
            img = cv.imread(imagepass, cv.IMREAD_COLOR)
            height, width, channel = img.shape
        if key == ord('b'):
            img = cv.imread(imagepass, cv.IMREAD_GRAYSCALE)
            height, width = img.shape
cv.destroyAllWindows()