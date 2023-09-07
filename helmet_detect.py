from ultralytics import YOLO
import os
import cv2

path=os.path.dirname(__file__)
path=path+''
os.chdir(path)

re_helmet = []
re_kb = []
re_nonhelmet = []
re_person = []

model = YOLO("yolov8n.yaml")
model = YOLO("train.pt")
    
video_path = "https://youtu.be/LnmZ1nNFBiQ"
cap = cv2.VideoCapture(video_path)


def detect():
while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        arr_helmet = []
        arr_kb = []
        arr_nonhelmet = []
        arr_person = []
        
        result = model(frame,conf=0.3)
        plot=result[0].plot()
        boxes=result[0].boxes
        
        for box in result[0].boxes:
            num=box.cls[0].cpu().detach().numpy().tolist()
            box=box.xywh
            x=box[0][0].cpu().detach().numpy().tolist()
            y=box[0][1].cpu().detach().numpy().tolist()
            w=box[0][2].cpu().detach().numpy().tolist()
            line = [x,y,w]
            if num==0:
                arr_helmet.append(line)
            elif num==1:
                arr_kb.append(line)
            elif num==2:
                arr_nonhelmet.append(line)
            elif num==3:
                arr_person.append(line)
        
        re_helmet = arr_helmet
        re_kb = arr_kb
        re_nonhelmet = arr_nonhelmet
        re_person = arr_person
        cv2.imshow("", result)


def get_data():
    return re_helmet, re_kb, re_nonhelmet, re_person