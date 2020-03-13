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
import datetime
import picar
from random import randint

picar.setup()

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
while time.time() <= initial+3.58:
    fw.turn_straight()
    bw.backward()
    
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
    #frame = cv2.resize(frame, (28, 28))
    
    key = cv2.waitKey(1) & 0xFF
    
    classify = 0
    #arbitrary boundaries, we need to calculate them once we know the car's constant speed
    if time.time() >= initial+2 and time.time() <= initial+2.5:
        classify = 1
    
    random = randint(0, 4) #1 in 6 chance to be added to the test dataset instead of training
    if random == 0:
        filename = ('/home/pi/roadreader/tests/' + str(classify) + '/' + str(datetime.datetime.now()) + '.png')
    else:
        filename = ('/home/pi/roadreader/training/' + str(classify) + '/' + str(datetime.datetime.now()) + '.png')
    
    cv2.imwrite(filename, frame)
    
    label = "{}".format(classify)
    frame = cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Frame", frame)
    
    if key == ord("q"):
        break;

cv2.destroyAllWindows()
vs.stop()
bw.stop()