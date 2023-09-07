from detect_he import Detect
import threading
import time
import math

be_kb = []
be_nonhelmet = []
be_person = []

af_kb = []
af_nonhelmet = []
af_person = []

data=Detect()

def re_data():
    data.detect()
    
def per_move(af_nonhelmet,af_person,distance):
    for pe_ax,pe_ay,pe_aw in af_person:
        arr_pe=[]
        for pe_bx,pe_by,pe_bw in be_person:
            dis_pe=math.sqrt((pe_ax-pe_bx)**2+(pe_ay-pe_by)**2)
            arr_pe.append(dis_pe)
        if len(arr_pe)==0:
            continue
        else:
            arr_pe.sort()
            if distance*0.7<arr_pe[0] and arr_pe[0]<distance*1.3: 
                for he_ax,he_ay,he_aw in af_nonhelmet:
                    arr_he=[]
                    for he_bx,he_by,he_bw in be_nonhelmet:
                        dis_he=math.sqrt((he_ax-he_bx)**2+(he_ay-he_by)**2)
                        arr_he.append(dis_he)
                    if len(arr_pe)==0:
                        continue
                    else:
                        arr_he.sort()
                        if distance*0.7<arr_pe[0] and arr_pe[0]<distance*1.3:
                            return True
    return False
                            
                            
data_thread=threading.Thread(target=re_data)
data_thread.daemon=True
data_thread.start()

while 1:
    af_kb, af_nonhelmet,af_person= data.re()
    
    
    for kb_ax,kb_ay,kb_aw in af_kb:
        arr=[]
        for kb_bx, kb_by,kb_bw in be_kb:
            dis=math.sqrt((kb_ax-kb_bx)**2+(kb_ay-kb_by)**2)
            arr.append([dis,kb_ax,kb_ay])
        if len(arr)==0:
           continue
        else:
            arr.sort(key=lambda x:x[0])
            if arr[0][0]>kb_aw/20:
                if per_move(af_nonhelmet,af_person,arr[0][0]):
                    print(arr[0][1],arr[0][2])
    be_kb=af_kb
    be_nonhelmet=af_nonhelmet
    be_person=af_person
    time.sleep(0.3)
    
    
