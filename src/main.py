import cv2 as cv
import numpy as np

class ColorRecognizer:
    def __init__(self, data, lowerb, upperb):
        self.lowerb = lowerb
        self.upperb = upperb
        self.data = data
    def detect(self):
        mask = cv.inRange(self.data,self.lowerb,self.upperb)
        self.out = cv.bitwise_and(self.data, self.data, mask=mask)
    def showres(self):
        cv.imshow("result",self.out)
        cv.waitKey(0)

### Testing
#media = cv.imread("media/bluebox.png")
#print(type(media))
# BGR: BLUE, GREEN, RED
#clr = ColorRecognizer(media, np.array([60,14,14]), np.array([180,70,70]))
#clr.detect()
#clr.showres()