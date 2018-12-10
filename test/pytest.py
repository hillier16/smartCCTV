import cv2
import new
import boto3
import serial
from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
import logging

logging.basicConfig()

s3 = boto3.client('s3', region_name = 'ap-northeast-2')
check = False
cmd = 'temp'

ser = serial.Serial(
	port = '/dev/ttyACM0',
	baudrate=9600,
)

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('ssmartcctv-mobilehub-1578044338-HighSoundLog')

print('START CONNECTING WITH ARDUINO')

ser.write(cmd.encode())
content = ser.readline()

def upload_video():
    name = new.videoname
    if name == "":
        return
    print ("Upload time", name)
    bucket_name = 'smartcctv'
    if name[17] == '1':
        key = name[:15]+'0'
        putResponse = s3.put_object(Bucket=bucket_name, Key = key+'/')
    upload = s3.upload_file(name, bucket_name, key+'/'+name)
    global check
    if check:
        new_key = name[:10]
        print("new_key", new_key)
        s3.upload_file(name, 'ssmartcctv-deployments-mobilehub-1578044338', new_key+'/'+name)
        check = False
    if upload:
        os.remove("/home/pi/Smart_CCTV/test/"+name+".avi")

cap = cv2.VideoCapture(-1)
cap.set(cv2.CAP_PROP_FRAME_COUNT, 60)


if(cap.isOpened()!=True):
    cv2.VideoCapture(0)
    print("Camera disconneted")
    quit()
    
sched = BackgroundScheduler()
sched.start()
#sched.add_job(new.Video_Start, 'cron', minute='0,10,20,30,40,50', second = '0', id="test_1", args=[cap])
#sched.add_job(upload_video, 'cron', minute='9,19,29,39,49,59', second = '59', id="test_2")
sched.add_job(new.Video_Start, 'cron', second = '10', id = "test_1", args=[cap])
sched.add_job(upload_video, 'cron', second = '8', id = "test_2")

while True:
    global check
    try:
        decibel = ser.readline()
        t_decibel = decibel[0:2]
        now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        before = now[:15]
        arrange = before + '0:00'


        if t_decibel != '':
            if t_decibel > '65':
                check = True
                table.put_item(
                    Item = {
                        'decibel' : int(t_decibel, base=10),
                        'time' : now,
                        'video_time' : arrange
                        }
                    )
        continue
    except KeyboardInterrupt:
        quit()
        
cap.release()
cv2.destroyAllWindows()


