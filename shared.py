import multiprocessing

height, width = 720, 1280  # Задайте размеры изображения
sleep_time = 0.1

ws_receive_lock = multiprocessing.Lock()
ws_push_lock = multiprocessing.Lock()
frame_lock = multiprocessing.Lock()