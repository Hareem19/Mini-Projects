import numpy as np
import cv2
import face_recognition_models
import csv
from datetime import datetime
vid_cap=cv2.VideoCapture(0)
hareem=face_recognition_models.load_image("faces/Hareem.jpeg")
hareem_enc=face_recognition_models.face_encodings(hareem)[0]