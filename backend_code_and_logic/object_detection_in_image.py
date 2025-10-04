#Detects objects within an image

import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

img_path = ""

img = cv2.imread(img_path)

if img is None:
    print("Failed to load image. Check path again.")
    exit()

results = model(img)

annotated_frame = results[0].plot()

resized_img = cv2.resize(annotated_frame, (1280, 720))

cv2.imshow("Detection", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
