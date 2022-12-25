import cv2 as cv

img = cv.imread("images/test.jpg")
print("Resimin boyutu :: ", img.size)
print(img.shape)
cv.imshow("IMG", img)

resized_img = cv.resize(img, (500,500))
"""
param1: boyu değiştirlecek resim
param2: (yeni_en, yeni_boy)
"""
print("Resimin boyutu :: ", resized_img.size)
print(resized_img.shape)
cv.imshow("RESIZED IMG", resized_img)

#                 y1  y2  x1  x2
cropped_img = img[10:200, 50:300]
print("Resimin boyutu :: ", cropped_img.size)
print(cropped_img.shape)
cv.imshow("CROPPED IMG", cropped_img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print("Resimin boyutu :: ", gray.size)
print(gray.shape)
cv.imshow("GRAY IMG", gray)

cv.waitKey(0)
cv.destroyAllWindows()