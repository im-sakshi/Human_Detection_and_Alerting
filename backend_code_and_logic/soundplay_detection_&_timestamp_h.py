#Plays sound/alert whenever a person is detected in webcam feed, also displays the Timestamp

from playsound import playsound
import threading
import cv2
from ultralytics import YOLO
import datetime as dt

sound_path = "warning.mp3"

model=YOLO("yolov8n.pt")
vid= cv2.VideoCapture(0)


def play_alert():
    try:
        playsound(sound_path)
    except Exception as e:
        print("Sound error:", e)


while True:
    ret, frame= vid.read()
    if not ret:
        break

    results= model.predict(frame, conf=0.5)

    for r in results:
        box_detected = r.boxes
        for box in box_detected:
            x1,y1,x2,y2= map(int, box.xyxy[0])
            confidence= float(box.conf[0])
            cls=int(box.cls[0])

            if cls==0: #for humanz
                class_name = model.names[cls]
                cv2.rectangle(frame, (x1,y1),(x2,y2),(0,0,255),2)
                cv2.putText(frame, f"{class_name}, {confidence:.2f}", (x1,y1-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0), 2)

                # Plays alert sound 
                threading.Thread(target=play_alert, daemon=True).start()

                timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[Alert] Human detected at {timestamp} - Confidence: {confidence *100:.2f}%")

                #Saving timestamp in a log file
                with open("log.txt", "a") as log_file:
                    log_file.write(f"[ALERT] Human detected at {timestamp} — Confidence: {confidence * 100:.2f}%\n")


    cv2.imshow("AI Surveillance Bot", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
