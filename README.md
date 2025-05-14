**Rock Paper Scissors – AI-Based Hand Gesture Recognition Game**
This project is an interactive Rock-Paper-Scissors game that utilizes real-time computer vision to detect hand gestures through the webcam and allows the user to play against the computer. It integrates Flask for the backend, MediaPipe for gesture detection, and OpenCV for video frame processing.

**Features**
1. Real-time webcam video stream for gesture input
2. Hand gesture recognition using Google’s MediaPipe
3. Rock-Paper-Scissors game logic with score tracking
4.Sound effects for game outcomes (win, lose, tie)
5. Responsive and intuitive front-end interface
6. Restart and Exit game functionality

**Technology Stack**
Frontend - HTML, CSS, JS
Backend - Python , Flask
CV & ML - OpenCV, MediaPipe
Media Assets - MP# audio files, jpeg images

**Prerequisites**
Python 3.7 or higher
A functioning webcam
pip 
  - Flask
  - opencv-python
  - numpy
  - mediapipe

**Project Structure**

rock-paper-scissors-hand-gesture/
│
├── static/
│   ├── images/
│   │   └── background.jpg
│   ├── sounds/
│   │   ├── win.mp3
│   │   ├── lose.mp3
│   │   └── tie.mp3
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md

**Steps to Run the Application**

pip install -r requirements.txt
python app.py
