# OpenCV kütüphanesini içe aktarıyoruz
import cv2 as cv

"""
imread  :: param1: içe aktarılacak resim
imshow  :: param1: resimin gösterileceği pencere adı, param2: gösterilecek resim
imwrite :: param1: resimin kaydedileceği dizin, param2: kayıt eilecek resim
"""

# Dizinde bulunan resimi içe aktarıyrouz.
img = cv.imread("test.jpg")

# İçe aktardığımız resimi ekranda gösteriyoruz
cv.imshow("Pencere Adı", img)
cv.waitKey(0) #pencere hemen açılıp kapanmasın diye kodu bekletiyoruz

cv.imwrite("dizin/save.jpg", img)
cv.destroyAllWindows()