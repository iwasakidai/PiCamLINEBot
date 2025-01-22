from picamera2 import Picamera2, Preview
import time

def capture_photo(file_path = "photo.jpg"):
    """
    Raspberry Piに設置のカメラで撮影して画像データのパスを返す

    Args:
        filename: 撮影データの保存パス
    Returns:
        None
    """
    picam2 = Picamera2()
    camera_config = picam2.create_still_configuration()
    picam2.configure(camera_config)
    picam2.start_preview(Preview.NULL)

    picam2.start()
    time.sleep(2)
    picam2.capture_file(file_path)
    picam2.close()

    return
