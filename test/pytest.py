import cv2
import new
import boto3
import os
from apscheduler.schedulers.background import BackgroundScheduler
import logging
logging.basicConfig()


s3 = boto3.client('s3', region_name = 'ap-northeast-2')

def upload_video():
    if new.videoname == "":
        return
    print new.videoname
    bucket_name = 'smartcctv'
    s3.upload_file(new.videoname, bucket_name, new.videoname)
    


cap = cv2.VideoCapture(-1)
cap.set(cv2.CAP_PROP_FRAME_COUNT, 60)


if(cap.isOpened()!=True):
    cv2.VideoCapture(0)
    print("Camera disconneted")
    quit()
    
sched = BackgroundScheduler()
sched.start()
sched.add_job(new.Video_Start, 'cron', second='10', id="test_1", args=[cap])
sched.add_job(upload_video, 'cron', second='9', id="test_2")

while True:
    try:
        continue
    except KeyboardInterrupt:
        quit()
        
cap.release()
cv2.destroyAllWindows()


