import time

import shared

def init_manager(ws_receive_stack):
    while True:
        # with shared.ws_receive_lock:
            # for msg in ws_receive_stack:
                # print(msg)    
            # ws_receive_stack[:] = []

        time.sleep(1)