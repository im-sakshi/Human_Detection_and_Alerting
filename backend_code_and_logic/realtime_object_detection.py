#Detects objects in the webcam feed (based on COCO dataset used by YOLOv8)

import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        break

    results = model.predict(frame, conf=0.5) 

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0]) 
            conf = float(box.conf[0])              
            cls = int(box.cls[0])                  

            class_name = model.names[cls]
            # if class_name is None:
            #     class_name = "Unknown"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)    
            
            cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)     

    cv2.imshow('AI Surveillance Bot', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
