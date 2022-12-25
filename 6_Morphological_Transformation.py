import cv2 as cv
import numpy as np

"""
#1 EREZYON
- ön plandaki nesnenin sınırlarını aşıdırır

#2 GENİŞLEME
- erezyonun tam tersidir
- görüntüdeki beya bölgeyş arttırır

#3 AÇMA
- Erezyon + Genişleme'dir
- Gürültünün giderilmesinde faydalıdır

#4 Kapatma
- Genişleme + Erezyon'dur
- Ön plandaki nesnenin içindeki küçük delikleri
kaparmak için kullanışlıdır

#5 Morfolojik Gradyan
- bir görüntünün genişlemesi ve erezyonu arasındki
farktır
"""

img = cv.imread("image/base.py")
kernel = np.ones((5,5),np.uint8)

#1
erosion = cv.erode(img,kernel,iterations = 1)
cv.imshow("EROSION", erosion)
#2
dilation = cv.dilate(img,kernel,iterations = 1)
cv.imshow("DILATION", dilation)
#5
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow("GRADIENT", gradient)

#3
img = cv.imrad("images/open.jpg", 0)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow("OPENING", opening)

#4
img = cv.imrad("images/close.jpg", 0)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow("CLOSING", closing)


cv.waitKey(0)
cv.destroyAllwindows()