import shared

def video_handle(video_frame, frame, processFn):
    last_frame_version = 0

    while True:
        # time.sleep(shared.sleep_time)

        if (len(video_frame) == 0 or last_frame_version == video_frame[0]):
            continue

        last_frame_version = video_frame[0]

        processing_frame = video_frame[1]
        processing_frame = processFn(processing_frame)

        with shared.frame_lock:
            frame[:] = processing_frame[:]