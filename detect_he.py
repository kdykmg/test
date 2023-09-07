from ultralytics import YOLO
import os
import cv2


class Detect:
    def __init__(self):
        self.path=os.path.dirname(__file__)
        self.path=self.path+''
        os.chdir(self.path)
        
        self.re_helmet = []
        self.re_kb = []
        self.re_nonhelmet = []
        self.re_person = []
        self.model = YOLO("yolov8n.yaml")
        self.model = YOLO("train.pt")
        self.video_path = "test2.mp4"
        self.cap=cv2.VideoCapture(self.video_path)
        
        
        
    def detect(self):
        
        while self.cap.isOpened():
            success, frame = self.cap.read()
            if success:
                arr_helmet = []
                arr_kb = []
                arr_nonhelmet = []
                arr_person = []
                
                result = self.model(frame,conf=0.3)
                plot=result[0].plot()
                
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
                
                self.re_helmet = arr_helmet
                self.re_kb = arr_kb
                self.re_nonhelmet = arr_nonhelmet
                self.re_person = arr_person
                cv2.imshow("Video", plot)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                
                
                
    def re(self):
        return self.re_kb, self.re_nonhelmet, self.re_person