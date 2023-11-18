import multiprocessing

from ws import init_ws
from manager import init_manager
from main_draw import init_draw
from modules.calibration_module import init_calibration
    

if __name__ == "__main__":
    manager = multiprocessing.Manager()

    ws_receive_stack = manager.list()
    ws_push_stack = manager.list()
    frame = manager.list()

    ws_process = multiprocessing.Process(target=init_ws, args=(ws_receive_stack,))
    manager_process = multiprocessing.Process(target=init_manager, args=(ws_receive_stack,))
    calibration_process = multiprocessing.Process(target=init_calibration, args=(ws_receive_stack, frame))
    camera_process = multiprocessing.Process(target=init_ws)

    # ws_process.start()
    # manager_process.start()
    # calibration_process.start()
    # camera_process.start()
    
    init_draw(frame)
    
    ws_process.kill()
    manager_process.kill()
    calibration_process.kill()