import cv2
import numpy as np
from matplotlib import pyplot as plt
if __name__ == '__main__':
    img_rgb = cv2.imread('find_waldo_1.jpeg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('waldo_1.png',0)
    # saves the width and height of the template into 'w' and 'h'
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    # finding the values where it exceeds the threshold
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #draw rectangle on places where it exceeds threshold
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

    cv2.imwrite('found_waldo_1.png',img_rgb)