import cv2 
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
cap = cv2.videoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Pose Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

