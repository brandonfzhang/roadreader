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

model = load_model('model.h5')

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

gate_value = 30     # less then the normal, will act
forward_speed = 90
bw.speed = forward_speed

vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
    image = cv2.resize(frame, (28, 28))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    prediction = np.argmax(model.predict(image)[0], axis=1)
    label = "No Sign"
    
    if stopSign > noSign:
        label = "Stop Sign"
        proba = stopSign
        
    label = "{}".format(label)
    frame = cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if prediction == 1: #format stop sign output to be 1
        fw.forward()
        bw.forward()
    else:
        fw.stop()
        bw.stop()
    
    if key == ord("q"):
        break;

cv2.destroyAllWindows()
vs.stop()
fw.stop()
bw.stop()