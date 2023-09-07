from ultralytics import YOLO
import cv2
import os
import urllib

model = YOLO("./pretrained/yolov8s.pt")
os.makedirs('data', exist_ok=True)
urllib.request.urlretrieve("https://ultralytics.com/images/bus.jpg", 'data/bus.jpg')