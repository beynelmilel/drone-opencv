import cv2 as cv
import numpy as np
from enum import Enum

class ColorRecognizer:
    """
    A class helps to clarify where the intended data (color) is most.

    Attributes:
    -----------
        Box (Enum): generally used to give results of operation (such as where color more belongs if it is in 1st Box it returns 1)...
        data (numpy.ndarray): Image data (Mat in C++)
        lowerb (numpy.ndarray): Lower boundary of the intended data (color) in BGR (Blue-Green-Red) order
        upperb (numpy.ndarray): Upper boundary of the intended data (color) in BGR (Blue-Green-Red) order
        out (numpy.ndarray): Image data (Mat in C++)
    """

    class Box(Enum):
        UpLeft=1
        Up=2
        UpRight=3
        Right=4
        Center=5
        Left=6
        DownLeft=7
        Down=8
        DownRight=9
    def __init__(self, data, lowerb, upperb):
        """
        Initialize the member values.

        Arguments:
        ----------
            data (numpy.ndarray): Image data (Mat in C++)
            lowerb (numpy.ndarray): Lower boundary color in BGR (Blue-Green-Red) order
            upperb (numpy.ndarray): Upper boundary color in BGR (Blue-Green-Red) order
        """
        self.lowerb = lowerb
        self.upperb = upperb
        self.data = data
    def detect(self):
        """
        ``Deprecated``. Should not be used.
        """
        mask = cv.inRange(self.data,self.lowerb,self.upperb)
        self.out = cv.bitwise_and(self.data, self.data, mask=mask)
    def checkBoundaries(self,data):
        """
        Checks if the data is in the range of ``lowerb`` (lower boundaries) and ``upperb`` (upper boundaries).

        Arguments:
        ----------
            data (numpy.ndarray): Color in "BGR" (BLUE-GREEN-RED) order.
        Returns:
        --------
            bool: True if it is in boundaries otherwise False.
        """
        pass
    def whereIsIt(self):
        """
        Splits data (image) in 9 parts. Then counts if that part has data in given boundaries. Returns the part (box) which has the most intended data.

        Returns:
        --------
            Box (Enum): Returns which box has more intended data (color basically).
        """
        height = self.data.shape[0]
        width = self.data.shape[1]
        one_height = round(height/3)
        two_height = one_height*2
        one_width = round(width/3)
        two_width = one_width*2
        first_box = 0
        second_box = 0
        third_box = 0
        fourth_box = 0
        fifth_box = 0
        sixth_box = 0
        seventh_box = 0
        eighth_box = 0
        ninth_box = 0
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
        """
        ``Deprecated``. Shows the image in a window and waits for key stroke.
        """
        cv.imshow("result",self.out)
        cv.waitKey(0)