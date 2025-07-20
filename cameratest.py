import cv2

cap = cv2.VideoCapture(1)  

while True:
    success, frame = cap.read()
    if not success:
        print("Gagal membuka kamera")
        break

    cv2.imshow("Test Kamera", frame)
    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()
