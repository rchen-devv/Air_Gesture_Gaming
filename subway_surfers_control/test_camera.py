import cv2 

cap = cv2.VideoCapture(0)

while True: 
    success, frame = cap.read()
    if not success:
        break
    cv2.imshow("Webcam Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()  # Close all OpenCV windows