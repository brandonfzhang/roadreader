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
import datetime

#model = load_model('model.h5')

vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
    #image = cv2.resize(frame, (28, 28))
    #image = image.astype("float") / 255.0
    #image = img_to_array(image)
    #image = np.expand_dims(image, axis=0)
    
    #(noSign, stopSign) = model.predict(image)[0]
    label = "No Sign"
    #proba = noSign
    proba = 0.5
    
    #if stopSign > noSign:
    #    label = "Stop Sign"
    #    proba = stopSign
    #label = "{}: {:.2f}%".format(label, proba*100)
    #frame = cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    
    if key == ord("s"):
        filename = ('/home/pi/roadreader/dataset/' + str(datetime.datetime.now()) + '.png')
        cv2.imwrite(filename, frame)
    elif key == ord("q"):
        break;

cv2.destroyAllWindows()
vs.stop()