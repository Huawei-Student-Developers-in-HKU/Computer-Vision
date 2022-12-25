import cv2 as cv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

img = cv.imread("images/sudoku.jpg", 0)
img = cv.medianBlur(img, 5)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

"""
Simple Thresholdingden Farkı Ne?
Simple Thresholding tüm pikseller üzerinde aynı eşik değer ile işlem yapılıyor. Adaptive Thresholding de ise küçük bir
bölgedeki bir pikselin eşiği alınıyor, gruplandırma oluyor.

Parametreler
- kaynak resim
- max value
- adaptive threshold methodu (ADAPTIVE_THRESH_MEAN_C, ADAPTIVE_THRESH_GAUSSIAN_C)
- kullanılacak thresh methodu (THRESH_BINARY)
- küçük bölgelerin eni
- küçük bölgelerin boyu
"""


img = cv.resize(img, (500,500))

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11,2)

cv.imshow("0", img)
cv.imshow("1", th2)
cv.imshow("2", th3)
cv.waitKey(0)

#Sonuçlar
#titles = ['Original Image', 'Global Thresholding (v = 127)',
#            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
#images = [img, th1, th2, th3]
#for i in range(4):
#    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()