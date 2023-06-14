import cv2
import os
from keras.models import load_model


def predict(img):
  labels_list = ['T-shirt/top', 'Trouser','Dress','Shirt']
  model = load_model(os.path.join("app\models",'fashion_classifier_4_label.hdf5'))
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img = cv2.resize(img, (28,28))
  img = img.reshape(-1,28,28,1)
  prediction = model.predict(img)
  result = labels_list[prediction[0].argmax(axis=-1)]
  return result
  