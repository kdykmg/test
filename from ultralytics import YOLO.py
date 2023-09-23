from openvino.runtime import Core
import os
from typing import Tuple
from ultralytics.yolo.utils import ops
import torch
import numpy as np
import cv2

path=os.path.dirname(__file__)
path=path+'/train_openvino_model/train.xml'



core = Core()
net = core.read_model(model=path)
model=core.compile_model(model=net,device_name='CPU')



import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('ttt.jpg')

# 이미지 크기 및 모델 입력 크기 설정 (YOLOv4 기준)
model_input_width = 416
model_input_height = 416

# 이미지 크기 조정 및 모델 입력 크기에 맞게 정규화
resized_image = cv2.resize(image, (model_input_width, model_input_height))
input_blob = resized_image.astype(np.float32) / 255.0
input_blob = np.expand_dims(input_blob, axis=0)  # 배치 차원 추가 (NCHW 형식을 사용하는 경우)



# 모델 추론
output = model.infer({input_blob})

# 출력 형식 변환
output_blob = output['output_blob_name']  # 모델의 출력 블롭 이름을 지정해야 합니다.

# YOLO 객체 감지 후처리
def post_process(output_blob, confidence_threshold=0.5, iou_threshold=0.4):
    # 여기에 객체 감지 후처리 로직을 추가하세요.
    pass

detected_objects = post_process(output_blob)

# 감지된 객체 정보 출력
for obj in detected_objects:
    class_id, confidence, x, y, w, h = obj
    class_label = labels[class_id]
    print(f'Class: {class_label}, Confidence: {confidence:.2f}, Bounding Box: ({x}, {y}, {w}, {h})')
