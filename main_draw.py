import cv2
import numpy as np
import time

import shared

WINDOW_TITLE = 'video'

def init_draw(frame):
    img = np.zeros((shared.height, shared.width, 3), dtype=np.uint8)

    # Отображение изображения на экране
    cv2.imshow(WINDOW_TITLE, img)
    cv2.waitKey(1)

    while True:
        if len(frame) == 0:
            time.sleep(1)
            continue
        
        with shared.frame_lock:
            cv2.imshow(WINDOW_TITLE, np.array(frame))
        cv2.waitKey(1)  # Ждем короткое время для обновления