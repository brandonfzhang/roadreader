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
from pynput.keyboard import Key, Listener, KeyCode

current_keys = set()

def on_press(key):
    current_keys.add(key)
    #print("button is being held")

def on_release(key):
    if key in current_keys:
        current_keys.remove(key)
        #print("button is no longer being held")

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

gate_value = 30     # less then the normal, will act
forward_speed = 100
bw.speed = forward_speed

vs = VideoStream(src=0).start()
time.sleep(2.0)

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

#need constant speed of car to calculate distance and such

while True:
    if KeyCode.from_char('q') in current_keys:
        break;
    
    classify = 0
    if KeyCode.from_char('1') in current_keys:
        classify = 1
        
    if KeyCode.from_char('w') in current_keys:
        bw.backward()
    elif KeyCode.from_char('s') in current_keys:
        bw.forward()
    else
        bw.stop()
        
    if KeyCode.from_char('a') in current_keys:
        fw.turn(45)
    elif KeyCode.from_char('d') in current_keys:
        fw.turn(135)
    else
        fw.turn_straight()
    
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
    cv2.imshow("Frame", frame)
    
    random = randint(0,4) #1 in 5 chance to be added to the test dataset instead of training
    if random == 0:
        filename = ('/home/pi/roadreader/tests/' + str(classify) + '/' + str(datetime.datetime.now()) + '.png')
    else:
        filename = ('/home/pi/roadreader/training/' + str(classify) + '/' + str(datetime.datetime.now()) + '.png')
    
    cv2.imwrite(filename, frame)

cv2.destroyAllWindows()
vs.stop()
#bw.stop()
