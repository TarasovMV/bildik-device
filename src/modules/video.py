import cv2 
import numpy as np
import time

import shared

def init_video(frame):
    cap = cv2.VideoCapture('src/assets/demo.mp4')
    
    if (cap.isOpened()== False): 
        print("Error opening video file") 

    time.sleep(1)

    version = 1

    while(cap.isOpened()): 
        ret, video = cap.read()
        if ret == True: 
            video = cv2.resize(video, (shared.width, shared.height))

            video = [version] + [video]
            # print(video.shape)
            with shared.video_frame_lock:
                frame[:] = video[:]

            version += 1
            time.sleep(0.033)
        else:
            break

    cap.release()