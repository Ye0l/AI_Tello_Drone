import cv2
# from djitellopy import tello

# tello = tello.Tello()
# tello.connect()

# battery_level = tello.get_battery()
# print(f"Battery: {battery_level}%")
# tello.streamon()

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print(f"width: {cap.get(3)}, height: {cap.get(4)}")
    w = cap.get(3)
    h = cap.get(4)

# frame_read = cap.read()

while True:
    ret, frame = cap.read()


    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, dsize=(0,0), fx=0.7, fy=0.7)
    cv2.imshow('video', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    k = cv2.waitKey(1000//30) & 0xFF
    if k == 27:
        break
    if k == ord('b'):
        # print(f"Battery: {battery_level}%")
        pass
    if frame is None:
        break

# cap.release()
cv2.destroyAllWindows()
# tello.streamoff()