import cv2
import numpy as np
import time

import shared

WINDOW_TITLE = 'video'

def init_draw(frame):
    cv2.namedWindow(WINDOW_TITLE, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(WINDOW_TITLE,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    img = np.zeros((shared.height, shared.width, 3), dtype=np.uint8)
    background_color = (255, 255, 255)  # Здесь установлен зеленый цвет

    # Заполнение фона цветом
    image_filled = img.copy()
    image_filled[:, :] = background_color

    # Отображение изображения на экране
    cv2.imshow(WINDOW_TITLE, image_filled)
    cv2.waitKey(1)

    while True:
        if len(frame) == 0:
            time.sleep(1)
            continue
        
        with shared.frame_lock:
            cv2.imshow(WINDOW_TITLE, np.array(frame))
        cv2.waitKey(1)  # Ждем короткое время для обновления
