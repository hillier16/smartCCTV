import datetime
import cv2
import time
import boto3

videoname = ""

def Video_Start(cap):
    print("Video start,,,")
    global videoname
    # timer setting
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=58)
    nowDatetime = start.strftime('%Y-%m-%d_%H:%M:%S')
    videoname = nowDatetime+'.avi'
    print(nowDatetime)
    # video save setting
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(videoname, fourcc, 6.0, (640,480))
    
    while cap.isOpened():
        ret, frame = cap.read()
        out.write(frame)
        if(datetime.datetime.now() >= end):
            out.release()
            return

    
