import cv2 as cv

"""
#1 Ortalama Bulanıklaştırma
        x1 x1 x1
        x1 x1 x1
        x1 x1 x1

#2 Gauss Bulanıklaştırma
        x1 x2 x1
        x2 x4 x2
        x1 x2 x1

#3 Median Bulanıklaştırma (px -> pixel)
    px1 px2 px3
    px4 px5 px6  ==> median of px1, px2, px3, px4, px5, px6, px7, px8 and px9
    px7 px8 px9
"""

img = cv.imread("images/blur.jpg")

n1 = cv.blur(img, (3,3))
n2 = cv.blur(img, (5,5))
n3 = cv.blur(img, (7,7))

g1 = cv.GaussianBlur(img, (3,3), 0)
g2 = cv.GaussianBlur(img, (5,5), 0)
g3 = cv.GaussianBlur(img, (7,7), 0)

m1 = cv.medianBlur(img, 3)
m2 = cv.medianBlur(img, 5)
m3 = cv.medianblur(img, 7)

cv.imshow("IMG", img)

val = "m"
if val == "n":
    cv.imshow("#3", n1)
    cv.imshow("#5", n2)
    cv.imshow("#7", n3)

elif val == "g":
    cv.imshow("#3", g1)
    cv.imshow("#5", g2)
    cv.imshow("#7", g3)

elif val == "m":
    cv.imshow("#3", m1)
    cv.imshow("#5", m2)
    cv.imshow("#7", m3)

cv.waitKey(0)
cv.destroyAllWindows()