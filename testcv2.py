from ultralytics import YOLO

import cv2
import os

path=os.path.dirname(__file__)
path=path+''
os.chdir(path)

model = YOLO("train.onnx")
video_path = "vid1.mp4"
cap=cv2.VideoCapture(video_path)

while cap.isOpened():
   success,frame =cap.read()
   if success:
      result = model.track(frame,persist=True,conf=0.3)
      if result[0].boxes.id!=None:
         for tid in result[0].boxes:
            print(track_ids = tid.id.int().cpu().tolist())
      plot=result[0].plot()
      cv2.imshow("Video", plot)
      if cv2.waitKey(1) & 0xFF == ord("q"):
         break