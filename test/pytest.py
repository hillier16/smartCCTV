import cv2
import new
import os
from apscheduler.schedulers.background import BackgroundScheduler
import logging
logging.basicConfig()


cap = cv2.VideoCapture(-1)
if(cap.isOpened()!=True):
    cv2.VideoCapture(0)
    print("Camera disconneted")
    quit()
    
sched = BackgroundScheduler()
sched.start()
sched.add_job(new.Video_Start, 'interval', minutes=1, id="test_1", args=[cap])

while True:
    try:
        continue
    except KeyboardInterrupt:
        quit()
        
cap.release()
cv2.destroyAllWindows()


