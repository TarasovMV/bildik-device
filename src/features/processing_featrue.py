import cv2
import numpy as np

from helpers.video_handling import video_handle

def init_processing(video_frame, frame):
    video_handle(video_frame, frame, processing)

def processing(frame):
    # внутренняя поверхность
    inside_p_1 = [346, 238]
    inside_p_2 = [1580, 236]
    inside_p_3 = [1584, 848]
    inside_p_4 = [342, 848]

    # Радиус шара
    r = 15

    # Вырежем изображение
    pts_src = np.array([inside_p_1,inside_p_2,inside_p_3,inside_p_4], dtype=np.float32)
    width, height = 1120, 560 # размер результирующего изображения
    pts_dst = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
    inside_image = cv2.warpPerspective(frame, matrix, (width, height))

    # Поиск шаров
    gray = cv2.cvtColor(inside_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (13, 13), 2)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=9, param1=20, param2=20, minRadius=10, maxRadius=22)

    # Если круги найдены
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        # Рисование найденных кругов
        for (x, y, _) in circles:
            cv2.circle(inside_image, (x, y), r, (0, 255, 0), 2)

    return inside_image