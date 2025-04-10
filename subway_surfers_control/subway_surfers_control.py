import cv2 
import mediapipe as mp 
import pyautogui

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: 
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]

        if right_wrist.y < right_shoulder.y: 
            pyautogui.press("up")

        if left_wrist.y < right_shoulder.y:
            pyautogui.press("down")


    cv2.imshow('Subway Surfers Control', frame)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

    cap.release()
    cap.destroyAllWindows()
    