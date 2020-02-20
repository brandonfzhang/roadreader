import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import h5py
import imutils
from imutils.video import VideoStream
import cv2
from threading import Thread
import time
from picar import front_wheels
from picar import back_wheels
from picar import ADC
import time
import picar

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

gate_value = 30     # less then the normal, will act
forward_speed = 100
bw.speed = forward_speed

vs = VideoStream(src=0).start()
time.sleep(2.0)

#need constant speed of car to calculate distance and such

initial = time.time()

#print("start")
while time.time() <= initial+10:
    fw.turn_straight()
    bw.backward()
    
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
    frame = cv2.resize(frame, (28, 28))
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    classify = 0
    #arbitrary boundaries, we need to calculate them once we know the car's constant speed
    if time.time() >= initial+5 and time.time() <= initial+7:
        classify = 1
    filename = ('/home/pi/roadreader/dataset/' + classify + ' ' + str(datetime.datetime.now()) + '.png')
    cv2.imwrite(filename, frame)
    
    if key == ord("q"):
        break;

cv2.destroyAllWindows()
vs.stop()
bw.stop()