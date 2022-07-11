from time import sleep 
from picamera import PiCamera 
from datetime import date, datetime 

dateTime = datetime.now()
pictureName = str(dateTime)
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
#camera warm up time 
sleep(2)
camera.rotation = 180 
camera.capture(pictureName + ".jpg")

