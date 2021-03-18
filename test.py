import tensorflow as tf
import keras
import cv2
import os
import numpy as np
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_virtual_device_configuration(gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
    except RuntimeError as e:
        print(e)

model = keras.models.load_model("D:\Hardik\SGP\model-test1.h5")

cam = cv2.VideoCapture(0)

word_dict = {0:'One',1:'Ten',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)

    cv2.rectangle(frame, (320, 10), (620, 320), (0, 255, 0), 1)
    roi = frame[10:320, 320:620]

    cv2.imshow("Frame", frame)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gaussblur = cv2.GaussianBlur(gray, (5, 5), 2)
    smallthres = cv2.adaptiveThreshold(gaussblur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 2.8)
    ret, final_image = cv2.threshold(smallthres, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    final_image = cv2.resize(final_image, (300, 300))
    cv2.imshow("BW", final_image)
    final_image = cv2.resize(final_image, (128,128))


    final_image = np.reshape(final_image, (1, final_image.shape[0], final_image.shape[1], 1))
    pred = model.predict(final_image)
    print(word_dict[np.argmax(pred)])
    cv2.putText(frame,word_dict[np.argmax(pred)], (10,50), cv2.FONT_HERSHEY_PLAIN, 1, (0 , 255, 0), 1)
    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()







