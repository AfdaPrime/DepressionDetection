# %%
import os
from keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from tensorflow import keras
import pickle
import cv2
import numpy as np
from keras import layers
import sys
import tensorflow as tf
import cv2
import os
import numpy as np

import tensorflow as tf
from tensorflow import keras
from keras import layers
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

#%%


def predict_image():
    # image recognition
    # image recognition jump start
    path = os.path.join('./emotions', 'happy-boy.jpg')
    frame = cv2.imread(path)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for x,y,w,h in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) # BGR
        facess = faceCascade.detectMultiScale(roi_gray)
        if len(facess) ==0:
            print("Face not detected")
        else: 
            for(ex,ey,ew,eh) in facess:
                face_roi = roi_color[ey: ey+eh, ex:ex + ew]


    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
                                                
    while True:
        ret, frame = cap.read()
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.1,4)                                     
        for x,y,w,h  in faces: 
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w] 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            facess = faceCascade.detectMultiScale(roi_gray)
            if len(facess) == 0:
                print("Face not detected")       
                                
            else: 
                for(ex,ey,ew,eh) in facess:
                    face_roi = roi_color[ey: ey+eh, ex:ex + ew]
        final_image = cv2.resize(face_roi,(224,224))
        final_image = np.expand_dims(final_image,axis =0)
        final_image = final_image/255.0
                                                                                        
        Predictions = new_model.predict(final_image)       
                                                
        if (np.argmax(Predictions)==0):
            status = "Angry"     
            
            print(status)
            break                   
        elif (np.argmax(Predictions)==1):
            status = "Disgust"                                        
                                                
            print(status)
            break                   
        elif (np.argmax(Predictions)==2):
            status = "Fear"  
                                    
                                                
            print(status)
            break                   
        elif (np.argmax(Predictions)==3):
            status = "Happy"    
            
                                
                                                
            print(status)
            break                   
        elif (np.argmax(Predictions)==4):
            status = "Sad"   
            
    
                                                
            print(status)
            break                   
        elif (np.argmax(Predictions)==5):
            status = "Surpise"    
                                    
                                                
            print(status)
            break                   
        else:
            status = "Neutral"    
                                            
            print(status)
            break                   
                      
    cap.release()                                            
    cv2.destroyAllWindows()     