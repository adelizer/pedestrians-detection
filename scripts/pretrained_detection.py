"""
A script to run the trained VGG16 model for detection
"""

import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.applications.vgg16 import decode_predictions
from skimage.transform import resize
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import img_to_array
import cv2


class Detector(object):
    def __init__(self):
        self.model = load_model('../models/vgg16.h5')
        print(self.model.summary())

    def detect(self, image):
        image = img_to_array(image)
        # image = resize(image, (224, 224, 3))
        image = preprocess_input(image)
        y_hat = self.model.predict(np.expand_dims(image, axis=0))
        return y_hat


class CaptureCam(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_image(self):
        ret, frame = self.cap.read()
        frame = resize(frame, (224, 224, 3))
        return ret, frame

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()


def main():
    cap = CaptureCam()
    det = Detector()

    while True:
        ret, frame = cap.get_image()
        yhat = det.detect(frame)

        # label = decode_predictions(yhat)
        # label = label[0][0]
        #
        # print('%s (%.2f%%)' % (label[1], label[2] * 100))

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()