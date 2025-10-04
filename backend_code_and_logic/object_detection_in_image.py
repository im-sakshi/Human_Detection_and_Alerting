#Detects objects within an image

import cv2
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Use raw string properly (escape all backslashes)
img_path = "AI Powered Defence Surveillance Bot/college.jpg"

# Use OpenCV to read image
img = cv2.imread(img_path)

# Validate image is read correctly
if img is None:
    print("Failed to load image. Check path again.")
    exit()

# Run detection
results = model(img)

# Plot results with bounding boxes
annotated_frame = results[0].plot()

# Resize the annotated image for better display
resized_img = cv2.resize(annotated_frame, (1280, 720))

# Show the output image
cv2.imshow("Detection", resized_img)

# Save the output image
#cv2.imwrite("detected_output.jpg", annotated_frame)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()