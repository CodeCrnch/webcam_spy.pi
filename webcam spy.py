import cv2
import time

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        current_time = round(time.time())
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(current_time))
        cv2.imwrite(f"webcam_image_{timestamp}.jpg", frame)

        print(f"{timestamp}: image saved")

    else:
        print("unsuccesfull")
        break

    time.sleep(60)

