import cv2
import numpy as np
import glob
import random


# Loading YOLO
# This training weight is obtained by using ImageLable to generate weights and annotate pictures to prepare for training
net = cv2.dnn.readNet("yolov3_training_last.weights","yolov3_testing.cfg")

# Custom Object
classes=["Bottles"]

#Image Path
images_path = glob.glob("")
