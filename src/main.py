import multiprocessing

from modules.ws import init_ws
from modules.manager import init_manager
from modules.main_draw import init_draw
from modules.video import init_video

from features.calibration_feaature import init_calibration
from features.processing_featrue import init_processing
    

if __name__ == "__main__":
    manager = multiprocessing.Manager()

    ws_receive_stack = manager.list()       # Сообщения полученные из модуля WS
    ws_push_stack = manager.list()          # Сообщения для передачи модулю WS
    video_frame = manager.list()            # Кадр полученный с камеры/видео
    frame = manager.list()                  # Кадр для отрисовки в главном потоке

    ws_process = multiprocessing.Process(target=init_ws, args=(ws_receive_stack,))
    manager_process = multiprocessing.Process(target=init_manager, args=(ws_receive_stack,))
    video_process = multiprocessing.Process(target=init_video, args=(video_frame,))
    processing_process = multiprocessing.Process(target=init_processing, args=(video_frame, frame))
    # calibration_process = multiprocessing.Process(target=init_calibration, args=(ws_receive_stack, frame))

    # ws_process.start()
    # manager_process.start()
    # calibration_process.start()
    video_process.start()

    processing_process.start()
    
    init_draw(frame)
    
    # ws_process.kill()
    # manager_process.kill()
    # calibration_process.kill()
    video_process.kill()