from ultralytics import YOLO
import os

path=os.path.dirname(__file__)
path=path+''
os.chdir(path)
model=YOLO('yolov8n.pt')
model=YOLO('train.pt')

model.export(format='onnx',half=True,imgsz=(640,640))