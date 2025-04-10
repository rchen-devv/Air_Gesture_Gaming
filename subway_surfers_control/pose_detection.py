import cv2 
import mediapipe as mp

mp_pose = mp.solutions.pose # Access the pose detecction module
pose = mp_pose.Pose()
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read a frame from the webcam
    success, frame = cap.read()
    if not success:
        continue
    # Convert the frame to RGB from BGR
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame and get the pose landmarks
    results = pose.process(frame_rgb)
    # if pose landmarks are detected, draw them on the frame
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Pose Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

