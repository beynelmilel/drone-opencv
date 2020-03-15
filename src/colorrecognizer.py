import cv2 as cv
import numpy as np

class ColorRecognizer:
    def __init__(self, data, lowerb, upperb):
        self.lowerb = lowerb
        self.upperb = upperb
        self.data = data
    # Deprecated
    # Should not be used.
    def detect(self):
        mask = cv.inRange(self.data,self.lowerb,self.upperb)
        self.out = cv.bitwise_and(self.data, self.data, mask=mask)
    def whereIsIt(self):
        height = self.data.shape[0]
        width = self.data.shape[1]
        one_height = round(height/3)
        two_height = one_height*2
        one_width = round(width/3)
        two_width = one_width*2
        print(width,height)
        for h in range(0,height):
            for w in range(0,width):
                if h in range(0,one_height):
                    if w in range(0,one_width): #First Box
                        pass
                    elif w in range(one_width,two_height): #Second Box
                        pass
                    else: #Third Box
                        pass
                elif h in range(one_height,two_height):
                    if w in range(0,one_width): #Fourth Box
                        pass
                    elif w in range(one_width,two_width): #Fifth Box
                        pass
                    else: #Sixth Box
                        pass
                elif h in range(two_height, height):
                    if w in range(0,one_width): #Seventh Box
                        pass
                    elif w in range(one_width,two_width): #Eighth Box
                        pass
                    else: # Ninth Box
                        pass
    def showres(self):
        cv.imshow("result",self.out)
        cv.waitKey(0)