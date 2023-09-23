from detect_he import Detect
import threading
import time
import math

be_arr=[]
tracking=None
data=Detect()

def re_data():
    data.detect()
    
data_thread=threading.Thread(target=re_data)
data_thread.daemon=True
data_thread.start()

def per_move(arr,dis_kb):
    for pe_ax,pe_ay,pe_aw,pe_aids in arr[3]:
        for pe_bx,pe_by,pe_bw,pe_bids in be_arr[3]:
            if pe_aids==pe_bids:
                dis_pe=math.sqrt((pe_ax-pe_bx)**2+(pe_ay-pe_by)**2)
                if dis_kb*0.7<dis_pe and dis_pe<dis_kb*1.3: 
                    for he_ax,he_ay,he_aw,he_aids in arr[2]:
                        for he_bx,he_by,he_bw,he_bids in be_arr[2]:
                            if he_aids==he_bids:
                                dis_he=math.sqrt((he_ax-he_bx)**2+(he_ay-he_by)**2)
                                if dis_kb*0.7<dis_he and dis_he<dis_kb*1.3:
                                    return True
    return False

while 1:
    af_arr=data.get_arr()
    if tracking!=None:
        for kb_ax,kb_ay,kb_aw,ids in af_arr[1]: 
            if tracking==ids:
                print(kb_ax,kb_ay,ids)
                time.sleep(0.3)
                continue
    for kb_ax,kb_ay,kb_aw,kb_aids in af_arr[1]:
        for kb_bx, kb_by,kb_bw,kb_bids in be_arr[1]:
            if kb_aids==kb_bids:
                dis_kb=math.sqrt((kb_ax-kb_bx)**2+(kb_ay-kb_by)**2) 
                if dis_kb>kb_aw/20:
                    if per_move(af_arr,dis_kb):
                        tracking=kb_aids 
                        print(kb_ax,kb_ay,kb_aids)               
    be_arr=af_arr
    time.sleep(0.3)
    
    
