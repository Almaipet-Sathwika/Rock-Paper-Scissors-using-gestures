from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import mediapipe as mp
import random
import base64

app = Flask(__name__)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

def detect_gesture(landmarks):
    finger_tips = [8, 12, 16, 20]
    finger_states = []
    for tip in finger_tips:
        finger_states.append(landmarks[tip].y < landmarks[tip - 2].y)

    if not any(finger_states):
        return "rock"
    elif all(finger_states):
        return "paper"
    elif finger_states[0] and finger_states[1] and not finger_states[2] and not finger_states[3]:
        return "scissors"
    return "none"

def get_winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "win"
    return "lose"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    data = request.get_json()
    image_data = data['image'].split(",")[1]
    decoded = base64.b64decode(image_data)
    nparr = np.frombuffer(decoded, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture = "none"
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = hand_landmarks.landmark
            gesture = detect_gesture(lm_list)

    if gesture != "none":
        computer = random.choice(["rock", "paper", "scissors"])
        result = get_winner(gesture, computer)
    else:
        computer = "none"
        result = "none"

    return jsonify({
        "player": gesture,
        "computer": computer,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)
