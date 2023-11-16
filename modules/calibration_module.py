import cv2
import time
import numpy as np

import shared

def init_calibration(ws_receive_stack, frame):
    while True:
        time.sleep(shared.sleep_time)

        with shared.ws_receive_lock:
            coords = list(filter(lambda c: c['type'] == 'coordinates', ws_receive_stack))
            ws_receive_stack[:] = list(filter(lambda c: c['type'] != 'coordinates', ws_receive_stack))

        if len(coords) == 0:
            continue

        data = coords[-1]        
        points = np.array(data["data"], dtype=np.int32)

        # Отрисовка прямоугольника
        color = (0, 255, 0)  # Зеленый прямоугольник
        thickness = 2  # Толщина линии
        is_closed = True  # Замкнутый контур

        # Вычерчивание прямоугольника
        img = np.zeros((shared.height, shared.width, 3), dtype=np.uint8)
        cv2.polylines(img, [points], isClosed=is_closed, color=color, thickness=thickness)

        with shared.frame_lock:
            frame[:] = img

                