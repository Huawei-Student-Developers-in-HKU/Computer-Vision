import cv2 as cv
import matplotlib.pyplot as plt

"""
Histogramı, bir görüntünün yoğunluk dağılımı hakkında size genel bir fikir veren bir grafik veya çizim olarak düşünebilirsiniz.
X ekseninde piksel değerleri (0 ila 255 arasında değişen, her zaman değil) ve Y ekseninde görüntüde karşılık gelen piksel sayısına
sahip bir çizimdir.
"""

img = cv.imread("images/red_and_blue.png")

vis = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.figure(), plt.imshow(vis)

hist = cv.calcHist([img],[0],None,[256],[0,256])
plt.figure(), plt.plot(hist)

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.figure(), plt.plot(histr, color=col), plt.xlim([0,256])

plt.show()