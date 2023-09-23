from ultralytics import YOLO
import os
import cv2



class Detect:
    def __init__(self):
        self.path=os.path.dirname(__file__)
        self.path=self.path+''
        os.chdir(self.path)
        self.arr=[[],[],[],[]]
        self.model = YOLO("train.onnx")
        self.video_path = "test2.mp4"
        self.cap=cv2.VideoCapture(self.video_path)
        
        
        
    def detect(self):
        num=0
        while self.cap.isOpened():
            success, frame = self.cap.read()
            num=(num+1)%4
            if success and num==0:
                arr_re=[[],[],[],[]]
                result = self.model.track(frame,persist=True)
                plot=result[0].plot()
                
                for box in result[0].boxes:
                    if result[0].boxes.id!=None:
                        ids=box.id.int().cpu().tolist()
                        num=box.cls[0].cpu().detach().numpy().tolist()
                        box=box.xywh
                        x=box[0][0].cpu().detach().numpy().tolist()
                        y=box[0][1].cpu().detach().numpy().tolist()
                        w=box[0][2].cpu().detach().numpy().tolist()
                        line = [x,y,w,ids]
                        if num==0:
                            arr_re[0].append(line)
                        elif num==1:
                            arr_re[1].append(line)
                        elif num==2:
                            arr_re[2].append(line)
                        elif num==3:
                            arr_re[3].append(line)
                
                self.arr=arr_re

                cv2.imshow("Video", plot)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                
                
                
    def get_arr(self):
        return self.arr