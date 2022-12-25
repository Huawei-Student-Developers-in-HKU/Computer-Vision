import cv2 as cv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

img = cv.imread("sudoku.jpg", 0)

"""
Thresholding Nedir ?
Gri bir görüntüyü piksellerin 0 ile 255 olduğu ikili bir görüntüye dönüştürmeye çalımaktır. Aşağıda ki kod OpenCV
kütüphanesine bulunan farklı threshold methodlarını görselleştriyor. Kodu çalıştırarak bu 5 threashold methodunu
daha iyi inceleyebilirsiniz.

Kod Üzerinde Nasıl Çalışır ?
Bu kodda OpenCV ye ait simple thresholding methodlarını inceleyeceğiz. Simple thresholding methodları 2 çıktı döndürür.
Bunlardan ilki eşik değer ikincisi ise eşik değer uygulanmış resimdir. Thresholdin kullanmadan önce yapılması gereken
ilk şey resimleri gray scale formuna yani siyah-beyaz haline döndürmeliyiz. Sonrasında aşağıda da gördüğünüz seçenekler
arasından sizn resiminiz için en iyi çalışanı seçerek işleminize devam edebilirsiniz.

Parametreleri
- kaynak resim
- eşik değer (belirtilen değerin altında kalan pikseller 0'a yuvarlanır)
- maksimum değer (belirtilen eşiğin üstünde ise yuvarlanmasını istediğiniz piksel değeri)
- kullanılacak thresh methodu (THRESH_BINARY, THRESH_BINARY_INV, THRESH_TRUNC, THRESH_TOZERO, THRESH_TOZERO_INV)
"""

img = cv.resize(img, (500,500))

# Eğer piksel değerleri 127'nin altında ise siyah(0) üstünde ise beyaz (255) değerine eşitlenecek
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

#Buradaki ret değişkeni

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(1,6,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()