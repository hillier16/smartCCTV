import cv2
import datetime

#set start time with format
start = datetime.datetime.now()
nowDatetime = start.strftime('%Y-%m-%d_%H:%M')

#create video object
cap = cv2.VideoCapture(-1)
if(cap.isOpened()!=True):
    cap = cv2.VideoCapture(0)

#set Codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#create VideoWriter object to save video
out = cv2.VideoWriter(nowDatetime+'.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('CCTV', frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
