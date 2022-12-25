import cv2 as cv

img = cv.imread("images/black.jpg")

cv.line(img,(0,0),(511,511),(255,0,0),5)
"""
param1: kaynak resim
param2: (X1,Y1)
param3: (X2,Y2)
param4: renk
param5: çizgi kalınlığı
"""

cv.reactangle(img, (10,10), (50,80), (255,255,0), 1)
"""
param1: kaynak resim
param2: (X1,Y1)
param3: (X2,Y2)
param4: renk
param5: çizgi kalınlığı (eğer "-1" ise resimin içi dolu)
"""

cv.circle(img,(447,63), 63, (0,0,255), -1)
"""
param1: kaynak resim
param2: (Cencter-X, Center-Y)
param3: yarıçap
param4: renk
param5: çizgi kalınlığı (eğer "-1" ise resimin içi dolu)
"""

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
"""
param1: kaynak resim
param2: yazılacak değer - str olmak zorunda
param3: (X,Y) - yazının sol alt köşesi
param4: font
param5: punto
param6: renk
param7: çizgi kalınlığı
param8: çizgi tipi
"""

cv.imshow("RESULT", img)
cv.waitKey(0)

cv.destroyAllWindows()