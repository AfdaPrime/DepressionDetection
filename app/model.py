# %%
import math
import os
from keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle
import cv2
import numpy as np
import tensorflow as tf
import cv2
import os
import numpy as np
import tensorflow as tf

# %%
path = os.path.join('./NLP_Stuff', 'model.h5')
model = tf.keras.models.load_model(path)

path = os.path.join('./NLP_Stuff', 'tokenizer.pkl')
with open(path, 'rb') as f:
    tokenizer = pickle.load(f)

path = os.path.join('./emotions', 'Final_model_64p35.h5')
new_model = tf.keras.models.load_model(path)


# %%

def predict_sentiment(text):
    # preprocessing the given text
    text_seq = tokenizer.texts_to_sequences(text)
    text_pad = pad_sequences(text_seq, maxlen=200)

    # predicting the class
    return model.predict(text_pad)

# %%


# actual predict facial
def predict_image():

    # image recognition
    # image recognition jump start
    path = os.path.join('./emotions', 'happy-boy.jpg')
    frame = cv2.imread(path)
    faceCascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    for x, y, w, h in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # BGR
        facess = faceCascade.detectMultiScale(roi_gray)
        if len(facess) == 0:
            print("Face not detected")
        else:
            for(ex, ey, ew, eh) in facess:
                face_roi = roi_color[ey: ey+eh, ex:ex + ew]
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    i = 0

    total = 0

    passed = False

    while i <= 50:
        i += 1

        ret, frame = cap.read()
        faceCascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)
        for x, y, w, h in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            facess = faceCascade.detectMultiScale(roi_gray)
            print(facess)

            if len(facess) == 0:
                print("Face not detected")
                i -= 1
            else:
                for(ex, ey, ew, eh) in facess:
                    face_roi = roi_color[ey: ey+eh, ex:ex + ew]
        final_image = cv2.resize(face_roi, (224, 224))
        final_image = np.expand_dims(final_image, axis=0)
        final_image = final_image/255.0

        Predictions = new_model.predict(final_image)

        total += np.argmax(Predictions)

        if(passed):
            break

    total /= 50

    total = math.floor(total)

    cap.release()
    cv2.destroyAllWindows()

    if (total == 0):
        status = "Angry"
        print(status)

        path = os.path.join('./image', 'Angry.png')
        with open(path, 'rb') as file:
            blob_data = file.read()

    elif (total == 1):
        status = "Disgust"
        print(status)

        path = os.path.join('./image', 'Disgust.png')
        with open(path, 'rb') as file:
            blob_data = file.read()

    elif (total == 2):
        status = "Fear"
        print(status)

        path = os.path.join('./image', 'Fear.png')
        with open(path, 'rb') as file:
            blob_data = file.read()

    elif (total == 3):
        status = "Happy"
        print(status)

        path = os.path.join('./image', 'Happy.png')
        with open(path, 'rb') as file:
            blob_data = file.read()

    elif (total == 4):
        status = "Sad"
        print(status)

        path = os.path.join('./image', 'Sad.png')
        with open(path, 'rb') as file:
            blob_data = file.read()

    elif (total == 5):
        status = "Surpise"
        print(status)

        path = os.path.join('./image', 'Surpise.png')
        with open(path, 'rb') as file:
            blob_data = file.read()

    else:
        status = "Neutral"
        print(status)

        path = os.path.join('./image', 'Neutral.png')
        with open(path, 'rb') as file:
            blob_data = file.read()

    return blob_data
