#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


img_array = cv2.imread("training/0/Training_3908.jpg")


# In[3]:


img_array.shape #rgb


# In[4]:


print(img_array)


# In[5]:


plt.imshow(img_array) #BGR


# In[6]:


Datadirectory ="Training/" #training dataset


# In[7]:


Classes = ["0","1","2","3","4","5","6"] #list of classes = exact name of the folders


# In[8]:


for category in Classes:
    path = os.path.join(Datadirectory, category)
    for img in os.listdir(path):
        plt.imshow(cv2.cvtColor(img_array,cv2.COLOR_BGR2RGB))
        plt.show()
        break
    break


# In[9]:


img_size = 224 
new_array = cv2.resize(img_array,(img_size,img_size))
plt.imshow(cv2.cvtColor(new_array,cv2.COLOR_BGR2RGB))
plt.show()


# In[10]:


new_array.shape


# In[11]:


training_Data = [] ## data

def create_training_Data():
    for category in Classes:
        path = os.path.join(Datadirectory,category)
        class_num = Classes.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img))
                new_array = cv2.resize(img_array,(img_size,img_size))
                training_Data.append([new_array,class_num])
            except Exception as e:
                pass


# In[12]:


create_training_Data()


# In[13]:


print(len(training_Data))


# In[14]:


import random

random.shuffle(training_Data)


# In[15]:


X = [] # data/feature
y = [] # label

for features,label in training_Data:
    X.append(features)
    y.append(label)
    
X = np.array(X).reshape(-1, img_size, img_size, 3) # converting it to 4 dimensions


# In[16]:


X.shape


# In[18]:


# normalize the data
X = X/255.0;  


# In[19]:


type(y)


# In[20]:


y[0]


# In[21]:


Y = np.array(y)


# In[22]:


Y.shape


# # deep learning model for training

# In[23]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# In[24]:


model = tf.keras.applications.MobileNetV2() # pre-trained Model


# In[25]:


model.summary()


# # Transfer learning - Tuning, weights will start from last check point

# In[26]:


base_input = model.layers[0].input


# In[27]:


base_output = model.layers[-2].output


# In[28]:


base_output


# In[29]:


final_output = layers.Dense(128)(base_output)
final_output = layers.Activation('relu')(final_output)
final_output = layers.Dense(64)(final_output)
final_output = layers.Activation('relu')(final_output)
final_output = layers.Dense(7,activation = 'softmax')(final_output)


# In[30]:


final_output


# In[31]:


new_model = keras.Model(inputs = base_input, outputs = final_output)


# In[32]:


new_model.summary()


# In[33]:


new_model.compile(loss = "sparse_categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])


# In[34]:


new_model.fit(X,Y, epochs = 15) # training 


# In[36]:


new_model.save('Final_model_64p35.h5')


# In[37]:


new_model = tf.keras.models.load_model('Final_model_64p35.h5')


# In[38]:


frame = cv2.imread("happy-boy.jpg")


# In[39]:


frame.shape


# In[40]:


plt.imshow(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))


# # we need face detection algorithm (gray images)

# In[41]:


faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# In[42]:


gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


# In[43]:


gray.shape


# In[44]:


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


# In[45]:


plt.imshow(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))


# In[46]:


plt.imshow(cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB))


# In[47]:


final_image = cv2.resize(face_roi,(224,224))
final_image = np.expand_dims(final_image,axis =0) ## neeed four dimensions
final_image = final_image/255.0 ## normalizing


# In[48]:


Predictions = new_model.predict(final_image)


# In[49]:


Predictions[0]


# In[50]:


np.argmax(Predictions)


# # VIDEO DEMO

# In[ ]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import cv2
import matplotlib.pyplot as plt
import numpy as np
path = "haarcascade_frontface_default.xml"
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

rectangle_bgr = (255,255,255)

img = np.zeros((500,500))

text = "Some text in a box!"

(text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
 
text_offset_x = 10
text_offset_y = img.shape[0] - 25
box_coords = ((text_offset_x, text_offset_y),(text_offset_x + text_width + 2, text_offset_y - text_height -2))
cv2.rectangle(img, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
cv2.putText(img, text, (text_offset_x, text_offset_y), font, fontScale=font_scale, color=(0,0,0), thickness =1)

cap = cv2.VideoCapture(1)
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
                                            
    font = cv2.FONT_HERSHEY_SIMPLEX
                                            
    Predictions = new_model.predict(final_image)
                                            
    font_scale = 1.5
    font = cv2.FONT_HERSHEY_PLAIN
                                            
                                            
    if (np.argmax(Predictions)==0):
        status = "Angry"     
        
        x1,y1,w1,h1 = 0,0,175,75
        cv2.rectangle(frame,(x1,x1), (x1 +w1, y1+h1),(0,0,0), -1)                                
        cv2.putText(frame,status,(x1 + int(w1/10), y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)                                 
        cv2.putText(frame,status,(100,150), font, 3,(0,0,255),2,cv2.LINE_4)       
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,0,225))  
                                            
    elif (np.argmax(Predictions)==1):
        status = "Disgust"    
        
        x1,y1,w1,h1 = 0,0,175,75
        cv2.rectangle(frame,(x1,x1), (x1 +w1, y1+h1),(0,0,0), -1)                                
        cv2.putText(frame,status,(x1 + int(w1/10), y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)                                 
        cv2.putText(frame,status,(100,150), font, 3,(0,0,255),2,cv2.LINE_4)       
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,0,225))                                      
                                            
    elif (np.argmax(Predictions)==2):
        status = "Fear"  
        
        x1,y1,w1,h1 = 0,0,175,75
        cv2.rectangle(frame,(x1,x1), (x1 +w1, y1+h1),(0,0,0), -1)                                
        cv2.putText(frame,status,(x1 + int(w1/10), y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)                                 
        cv2.putText(frame,status,(100,150), font, 3,(0,0,255),2,cv2.LINE_4)       
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,0,225))                                     
                                            
    elif (np.argmax(Predictions)==3):
        status = "Happy"    
        
        x1,y1,w1,h1 = 0,0,175,75
        cv2.rectangle(frame,(x1,x1), (x1 +w1, y1+h1),(0,0,0), -1)                                
        cv2.putText(frame,status,(x1 + int(w1/10), y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)                                 
        cv2.putText(frame,status,(100,150), font, 3,(0,0,255),2,cv2.LINE_4)       
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,0,225))                                     
                                            
    elif (np.argmax(Predictions)==4):
        status = "Sad"   
        
        x1,y1,w1,h1 = 0,0,175,75
        cv2.rectangle(frame,(x1,x1), (x1 +w1, y1+h1),(0,0,0), -1)                                
        cv2.putText(frame,status,(x1 + int(w1/10), y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)                                 
        cv2.putText(frame,status,(100,150), font, 3,(0,0,255),2,cv2.LINE_4)       
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,0,225))        
                                            
    elif (np.argmax(Predictions)==5):
        status = "Surpise"    
            
        x1,y1,w1,h1 = 0,0,175,75
        cv2.rectangle(frame,(x1,x1),(x1 +w1, y1+h1),(0,0,0), -1)                                
        cv2.putText(frame,status,(x1 + int(w1/10), y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)                                 
        cv2.putText(frame,status,(100,150), font, 3,(0,0,255),2,cv2.LINE_4)       
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,0,225))                                   
                                            
    else:
        status = "Neutral"    
            
        x1,y1,w1,h1 = 0,0,175,75
        cv2.rectangle(frame,(x1,x1), (x1 +w1, y1+h1),(0,0,0), -1)                                
        cv2.putText(frame,status,(x1 + int(w1/10), y1 + int(h1/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)                                 
        cv2.putText(frame,status,(100,150), font, 3,(0,0,255),2,cv2.LINE_4)       
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,0,225))                                  
                                            
    cv2.imshow('Face Emotion Recognition',frame)
                                            
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break                            
                                            
cap.release()                                            
cv2.destroyAllWindows()                                            


# In[ ]:





# In[ ]:




