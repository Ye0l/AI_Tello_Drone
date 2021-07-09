import cv2
from djitellopy import tello

tello = tello.Tello()
tello.connect()
battery_level = tello.get_battery()
print(battery_level)
tello.streamon()

w, h = 360, 240
range = 20
center_p = [(w//2 - range, w//2 + range), (h//2 - range, h//2 + range)]
fbRange = [6200, 6800]
fb = 0
ud = 0
yaw = 0
no_target = False
takeOff = False

def findFace(img):
    img = cv2.resize(img, (360,240))
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 2)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy),10,(0,255,0), 6)
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)
        # print(myFaceListC)
    if len(myFaceListArea) != 0:
        i= myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]

while True:
    img = tello.get_frame_read().frame

    img, info = findFace(img)
    cv2.imshow('frame',img)
    key = cv2.waitKey(1000//30) & 0xFF
    if key == ord('q'):
        break
    if key == ord('l'):
        takeOff = False
        print('land')
        tello.land()
    if key == ord('t'):
        takeOff = True
        print('takeoff')
        tello.takeoff()

    if takeOff:
        if info[1] > fbRange[0] and info[1] < fbRange[1]:
            fb = 0
        elif info[1] > fbRange[1]:
            fb = -20
        elif info[1] < fbRange[0] and info[1] != 0:
            fb = 20
        if info[0][0] == 0:
            tello.send_rc_control(0, 0, 0, 0)
            print(f'sendrc ({0},{0},{0},{0})')
            continue

        if center_p[1][1] - info[0][1] < 0:
            ud = -20
        elif center_p[1][0] - info[0][1] > 0:
            ud = 20
        else: ud = 0

        if center_p[0][1] - info[0][0] < 0:
            yaw = 20
        elif center_p[0][0] - info[0][0] > 0:
            yaw = -20
        else:
            yaw = 0

        print(f'sendrc ({0},{fb},{ud},{yaw})')
        tello.send_rc_control(0, fb, ud, yaw)


tello.streamoff()
# Release everything if job is finished
# cap.release()
# out.release()
cv2.destroyAllWindows()