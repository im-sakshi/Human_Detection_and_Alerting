import cv2
from ultralytics import YOLO
import time
import datetime as dt

import os
from twilio.rest import Client
from dotenv import load_dotenv

import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

load_dotenv()

model = YOLO("yolov8n.pt")
vid = cv2.VideoCapture(0)

last_whatsapp_time = last_email_time = 0  
whatsapp_cooldown = 60  
email_cooldown = 30     

def send_whatsapp_alert(objects):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
    target_number = os.getenv('TARGET_WHATSAPP_NUMBER')

    client = Client(account_sid, auth_token)

    object_details = ", ".join([f"{count} {obj}" for obj, count in objects.items()])
    body = body = (
    "Alert ⚠️🚨\n\n"
    f"Time: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    f"Detected: {object_details}\n\n"
    "Stay Safe.\n"
)

    message = client.messages.create(
        from_=twilio_number,
        to=target_number,
        body=body
    )

    print(f"Whatsapp alert sent: {message.sid}")


def send_email_alert(frame, objects):
    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")

    timestamp = dt.datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
    image_path = f"snapshots/intruder_{timestamp}.jpg" 
    cv2.imwrite(image_path, frame)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "ALERT ⚠️: Objects Detected by AI Surveillance Bot"

    body = f"""INTRUDER ALERT ⚠️
Objects detected by AI Surveillance Bot:
Time: {timestamp}
Detected: {', '.join([f"{count} {obj}" for obj, count in objects.items()])}

Snapshot is attached below.
"""
    msg.attach(MIMEText(body, 'plain'))

    with open(image_path, 'rb') as img_file:
        image = MIMEImage(img_file.read())
        image.add_header('Content-Disposition', 'attachment', filename=image_path)
        msg.attach(image)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("[Email sent!]")
    except Exception as e:
        print(f"[Email failed]: {e}")


while True:
    ret, frame = vid.read()
    if not ret:
        break

    results = model.predict(frame, conf=0.5)

    for r in results:
        detected_objects = {}  # Reset per frame
        box_det = r.boxes

        for box in box_det:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            cls = int(box.cls[0])
            class_name = model.names[cls]

            # Counts every detected class
            detected_objects[class_name] = detected_objects.get(class_name, 0) + 1

            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"{class_name}, {confidence:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)


        current_time = time.time()
        if detected_objects and (current_time - last_whatsapp_time > whatsapp_cooldown) and (current_time - last_email_time > email_cooldown):
            send_whatsapp_alert(detected_objects)
            send_email_alert(frame, detected_objects)
            last_whatsapp_time = last_email_time = current_time


    cv2.imshow("AI Surveillance Bot", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
