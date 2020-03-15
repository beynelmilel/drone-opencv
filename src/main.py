import cv2 as cv
import numpy as np
from colorrecognizer import ColorRecognizer as cr

### Testing
media = cv.imread("media/bluebox.png")
#print(type(media))
# BGR: BLUE, GREEN, RED
clr = cr(media, np.array([60,14,14]), np.array([180,70,70]))
#clr.detect()
clr.whereIsIt()
#clr.showres()