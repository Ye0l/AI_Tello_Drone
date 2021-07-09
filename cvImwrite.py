import cv2

img_path = "./mountain.jpeg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
title = 'IMG'

x, y = 100, 100

cv2.moveWindow(title, x, y)
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.imshow(title, img)

while True:
    key = cv2.waitKey(0) & 0xFF
    if key == ord('s'):
        cv2.imwrite('output_gray.jpeg', img)
    if key == ord('r'):
        # cv2.imshow(title, cv2.resize(img, (img.shape[1]*2, img.shape[0]*2)))
        cv2.resizeWindow(title, 20,20)
    if key == ord('q'):
        break

cv2.destroyAllWindows()