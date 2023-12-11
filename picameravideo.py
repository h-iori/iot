import picamera
from time import sleep
camera= picamera.PiCamera()
camera.start_recording('harsh.h264')
camera.wait_recording(10)
camera.stop_recording()
camera.close()
print("successfully recorded")