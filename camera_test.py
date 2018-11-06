import cv2
import numpy as np
from matplotlib import pyplot

cap = cv2.VideoCapture(-1)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        continue

    b,g,r = cv2.split(frame)
    frame = cv2.merge([r,g,b])
    pyplot.imshow(frame)
    print("imshow fuck")
    
    key = cv2.waitKey(0) & 0XFF
    if key == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
