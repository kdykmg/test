from ultralytics import YOLO
import os
import cv2

path=os.path.dirname(__file__)
path=path+''
os.chdir(path)

arr_person = []
arr_kb = []
arr_helmet = []
arr_nonhelmet = []

model = YOLO("yolov8n.yaml")  # YOLO 모델 생성
model = YOLO('train_openvino_model/')  # 미리 학습된 모델 로드 

#result=model('https://img.etnews.com/photonews/2005/1305244_20200529132431_661_0001.jpg',conf=0.3)  #이미지에서 객체 검출
result=model('https://health.chosun.com/site/data/img_dir/2022/06/13/2022061300830_0.jpg',conf=0.3)

plot=result[0].plot()  #결과 시각화
boxes=result[0].boxes  #객체 정보 출력]
for box in boxes:
      print(box.xyxy.cpu().detach().numpy().tolist())  #객체의 경계 상자 좌표
      print(box.conf.cpu().detach().numpy().tolist())  #신뢰도 
      print(box.cls.cpu().detach().numpy().tolist())  #클래스 0:helmet 1:kickboard 2:nonhelmet 3:person
for box in result[0].boxes.xywh:
      x=box[0].cpu().detach().numpy().tolist()
      y=box[1].cpu().detach().numpy().tolist()
      w=box[2].cpu().detach().numpy().tolist()
      h=box[3].cpu().detach().numpy().tolist()

for box in result[0].boxes:
      num=box.cls[0].cpu().detach().numpy().tolist()
      box=box.xywh
      x=box[0][0].cpu().detach().numpy().tolist()
      y=box[0][1].cpu().detach().numpy().tolist()
      line = [x,y]
      if num==0:
            arr_helmet.append(line)
      elif num==1:
            arr_kb.append(line)
      elif num==2:
            arr_nonhelmet.append(line)
      elif num==3:
            arr_person.append(line)
            
print("0     ",arr_helmet,"1     ",arr_kb,"2     ",arr_nonhelmet,"3     ",arr_person)
      
cv2.imshow("",plot)
cv2.waitKey(0)
cv2.destroyAllWindows()
