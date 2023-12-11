import picamera
from time import sleep
camera= picamera.PiCamera()
camera.resolution= (1024, 768)
camera.brightness=60
camera.start_preview()
camera.annotate_text= 'harsh bhai'
camera.capture('harsh.jpeg')
camera.stop_previwe()