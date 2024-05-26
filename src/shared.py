import multiprocessing

height, width = 1080, 1920  # Задайте размеры изображения
sleep_time = 0.1

ws_receive_lock = multiprocessing.Lock()
ws_push_lock = multiprocessing.Lock()
frame_lock = multiprocessing.Lock()
video_frame_lock = multiprocessing.Lock()