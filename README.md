**AI-Powered Human Detection & Alerting Surveillance System 🕵🏻**

An intelligent real-time surveillance system that detects humans and alerts instantly through WhatsApp and Email notifications with attached snapshots.

**Overview 🔍**

The AI-Powered Surveillance Bot is designed to strengthen perimeter and area security through real-time object and human detection.
Using advanced YOLOv8 and OpenCV, the system continuously monitors a live video feed and automatically sends email alerts with snapshots and WhatsApp notifications whenever any object or person is detected.
This project aims to serve as a smart, low-cost surveillance solution for defense and security applications.

**🧩 Features**

      ● 🧍‍♂️ Real-Time Human Detection – Detects presence using YOLOv5 and OpenCV.
      ● 📸 Automatic Snapshots – Captures and stores evidence with timestamps.
      ● 💬 Instant WhatsApp Alerts – Sends detection updates using Twilio API.
      ● 📧 Email Notifications – Delivers snapshots of intruders directly to your inbox.
      ● ⚙️ Easily Configurable – Manage credentials securely using a .env file.
      ● 💡 Future Ready – Planned GUI integration using Tkinter for improved usability. 

**🧠 Tech Stack**

              Category        |      Tools & Frameworks
      ________________________|_______________________________
      Programming             |            Python
      Computer Vision	      |            OpenCV, YOLOv8
      Notifications           |            Twilio API, smtplib
      Environment Management  |            dotenv


**🧾 How It Works**

      1. The bot uses your webcam (or an external camera) to capture real-time footage.
      2. YOLOv8 detects humans and other objects within the frame.
      3. When an object or person is identified:
        (a) A WhatsApp alert is triggered via Twilio.
        (b) An Email alert is sent with a snapshot attachment and timestamp.


**Environment Setup 👇🏻👇🏻**

      Before running, create a .env file based on the provided .env.example and fill in your credentials:

      TWILIO_ACCOUNT_SID=your_twilio_sid
      TWILIO_AUTH_TOKEN=your_twilio_auth_token
      TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
      TARGET_WHATSAPP_NUMBER=whatsapp:+91XXXXXXXXXX

      EMAIL_SENDER=your_email@gmail.com
      EMAIL_RECEIVER=receiver_email@gmail.com
      EMAIL_PASSWORD=your_app_password


**⚙️ Running the Project**

      🔵 Clone the repository
         git clone https://github.com/<your-username>/Human_Detection_and_Alerting.git

      🟡 Move into project folder
         cd Human_Detection_and_Alerting

      🔴 Install dependencies
         pip install -r requirements.txt

      🟢 Run the bot
         python main.py


**📂 Project Structure**

      Human_Detection_and_Alerting/
      │
      ├── backend_code_and_logic/       # Supporting modules and experiments
      ├── snapshots/                    # Images of detected humans
      ├── main.py                       # Main execution file
      ├── .env.example                  # Example environment configuration
      ├── .gitignore                    # Git ignore rules
      ├── yolov8n.pt                    # YOLO model weights
      ├── requirements.txt              # Enlists all the required python libraries
      └── README.md                     # Project documentation


**🌟 Future Enhancements**

      🎛️ Graphical User Interface (Tkinter-based control panel)
      🧑🏻 Face Recognition Integration (Recognising the authorized person and skipping alerts for them while still detecting and alerting unknown faces)
      ☁️ Cloud integration for remote access and centralized logging
      🔊 Real-time voice alert system

**Author 👩🏻‍💻**

      Sakshi Mishra
      AI & ML Enthusiast | Python Developer | Innovating with purpose

**🛡️ Disclaimer**

      This project is intended for educational and research purposes.
      Please ensure compliance with privacy and surveillance laws before deployment.
