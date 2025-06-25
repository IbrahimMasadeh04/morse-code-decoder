import numpy as np
import mediapipe as mp
import cv2 as cv
from utils import get_ear
import constants as c
import time

# initializing objects that related to face mesh and drawing
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

blink_start_time = None
last_blink_time = None
morse_sequence = ''
decoded_msg = ''

# capture the video
cap = cv.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        
        w, h, _ = frame.shape
        lms = result.multi_face_landmarks[0].landmark

        # calculating the EAR (Eye Aspect Ratio)

        left_eye = get_ear(lms, c.LEFT_EYE, w, h)
        right_eye = get_ear(lms, c.RIGHT_EYE, w, h)
        avg_ear = (left_eye + right_eye) / 2.0

        curr_time = time.time()

        # detect blink start and end
        if avg_ear < c.EAR_THRESHOLD:
            if blink_start_time is None:
                blink_start_time = curr_time

        else:
            if blink_start_time:
                blink_duration = curr_time - blink_start_time

                blink_start_time = None
                last_blink_time = curr_time
                
                if blink_duration < c.CLOSED_EYE_THRESHOLD:
                    morse_sequence += '.'
                else:
                    morse_sequence += '-'
        
        if morse_sequence and last_blink_time and (curr_time - last_blink_time > c.CHARACTER_GAP_THRESHOLD):
            if morse_sequence:
                decoded_char = c.MORSE_CODE.get(morse_sequence, '?')
                
                if morse_sequence == "--.--":
                    decoded_msg = decoded_msg[:-1]
                else:
                    decoded_msg += decoded_char
                morse_sequence = ''
                
                print(f'[MSG]{decoded_msg}', flush=True)
                
                last_blink_time = None

    cv.imshow('Morse Code Decoder', frame)
    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()