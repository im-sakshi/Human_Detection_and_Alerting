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

#whenever the model detects objects, it returns results which include bounding boxes, class id (like 0=human, 1= bicycle, 2 = car, 3=motorbike), and confidence scores.

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box corners
            conf = float(box.conf[0])              # Confidence
            cls = int(box.cls[0])                  # Class index

            # if cls!=0:  #class=0 means detecting only humans, else displays no label for rest
                # continue

            class_name = model.names[cls]
            # if class_name is None:
            #     class_name = "Unknown"

            # Draws box and labels it
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)    #(0,255,0) is the color of the box, 2 is the thickness of the box
            #Draws the class name and confidence above the box
            cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  #if I put cls instead of class_name, it will print the class id like 0, 1, 2 etc.   

            #conf::2 means 2 decimal places, so it will print like 0.99, 0.98 etc., (x1,y1-10) means the text will be above box, 0.6= font size, (0,255,0)= color of the text, 2= thickness of the text


    # Display live video
    cv2.imshow('AI Surveillance Bot', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
