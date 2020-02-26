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

#picar.setup()

#fw = front_wheels.Front_Wheels(db='config')
#bw = back_wheels.Back_Wheels(db='config')

#gate_value = 30     # less then the normal, will act
#forward_speed = 100
#bw.speed = forward_speed

vs = VideoStream(src=0).start()
time.sleep(2.0)

#need constant speed of car to calculate distance and such

while True:
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break;
    
    classify = 0
    if key == ord("1"):
        classify = 1
    
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
    cv2.imshow("Frame", frame)
    
    random = randint(0, 5) #1 in 6 chance to be added to the test dataset instead of training
    if random == 0:
        filename = ('/home/pi/roadreader/tests/' + str(classify) + ' ' + str(datetime.datetime.now()) + '.png')
    else:
        filename = ('/home/pi/roadreader/training/' + str(classify) + ' ' + str(datetime.datetime.now()) + '.png')
    
    cv2.imwrite(filename, frame)

cv2.destroyAllWindows()
vs.stop()
#bw.stop()
