import cv2
import mediapipe as mp
import numpy as np
from pynput.mouse import Button, Controller
import time

# Initialize mouse controller
mouse = Controller()

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Initialize MediaPipe drawing utility
mp_drawing = mp.solutions.drawing_utils

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

click_threshold = 0.15  # Adjust this value based on your preference
double_click_time = 0.5  # Time within which two clicks should happen to be considered as double click

last_click_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    # Flip the frame horizontally for self-view
    frame = cv2.flip(frame, 1)
    
    # Convert the BGR image to RGB and process it with MediaPipe Hands
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    # Draw hand landmarks on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get normalized hand coordinates
            x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
            y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            
            # Convert normalized coordinates to pixel coordinates
            h, w, c = frame.shape
            x_pixel, y_pixel = int(x * w), int(y * h)
            
            # Move the mouse
            mouse.position = (x_pixel, y_pixel)
            
            # Get thumb tip position
            thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
            thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            
            # Calculate distance between index finger tip and thumb tip
            dist = np.sqrt((x - thumb_x) * 2 + (y - thumb_y) * 2)
            
            # If distance is less than threshold, perform click action
            if dist < click_threshold:
                current_time = time.time()
                if current_time - last_click_time < double_click_time:
                    mouse.click(Button.left, 2)  # Perform double click
                else:
                    mouse.click(Button.left, 1)  # Perform single click
                
                last_click_time = current_time
    
    # Display the image
    cv2.imshow('MediaPipe Hands', frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
