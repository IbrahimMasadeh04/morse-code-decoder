import numpy as np

def get_ear(lms, eye_indices, img_w, img_h):
    eye = [(int(lms[i].x * img_w), int(lms[i].y * img_h)) for i in eye_indices]

    vertical_1 = np.linalg.norm(np.array(eye[1]) - np.array(eye[5]))
    vertical_2 = np.linalg.norm(np.array(eye[2]) - np.array(eye[4]))
    horizontal = np.linalg.norm(np.array(eye[0]) - np.array(eye[3]))
    return (vertical_1 + vertical_2) / (2 * horizontal)