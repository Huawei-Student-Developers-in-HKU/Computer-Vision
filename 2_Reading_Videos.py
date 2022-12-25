# OpenCV kütüphanesini içe aktarıyoruz
import cv2 as cv

# Bilgisayar kamerasına bağlanarak cap değişkenine atıyoruz
cap = cv.VideoCapture(0) # kamera indeksi, eğer birden fazla kamera var ise 0,1,... şeklinde devam eder

# Kameradan gelecek görüntüleri (frame) okumak için döngü açıyoruz
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv.imshow("Kamera", frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()