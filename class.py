import cv2
import numpy as np
import matplotlib.pyplot as plt
def main():
    img = cv2.imread("images/lenna.jpeg",0)
    nr , nc = img.shape[:2]
    cv2.imshow("asd", img)
    #histogram(nr , nc)
def histogram(nr,nc):
    i = 0
    j = 0
    hist = np.zeros([256])
    for i in nr:
        for j in nc:
            x = img[i][j]
            hist[x] = hist[x] + 1
    plt.plot(hist)
    plt.xlim([0,256])
main()