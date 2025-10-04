#This code detects only humans when 'h' is pressed, else detects nothing 👇🏻👇🏻

import cv2
from ultralytics import YOLO

model=YOLO("yolov8n.pt")
vid = cv2.VideoCapture(0)

detect_human = False

while True:
    ret, frame= vid.read()
    if not ret:
        break


    cv2.putText(frame, "Human Detection ON" if detect_human else "Human Detection OFF", (10,30) , cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2)


    if detect_human:
        results = model.predict(frame, conf=0.5)

        for r in results:
            boxes_detected = r.boxes
            for box in boxes_detected:
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                cls= int(box.cls[0])

                if cls!=0:  #class=0 means detecting only humans, else displays no label for rest
                    continue

                class_name = model.names[cls]

                cv2.rectangle(frame, (x1,y1),(x2,y2),(0,0,255),2) #BGR, Red box chosen
                cv2.putText(frame, f"{class_name}, {confidence:.2f}", (x1,y1-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("AI Surveillance Bot", frame)

    key = cv2.waitKey(1) & 0xFF

    if key== ord('h'):   #for TOGGLE b/w human detection ON/OFF
        detect_human = not detect_human

    elif key == ord('q'):  #for QUIT
        break


vid.release()
cv2.destroyAllWindows()
