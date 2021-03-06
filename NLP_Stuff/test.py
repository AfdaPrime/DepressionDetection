# %%
from keras.models import Model
from keras.layers import Input, Dense, Embedding, LSTM, GlobalMaxPooling1D
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import re
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


# %%
initial = pd.read_csv(
    'D:/newCode/Machine Learning/DepressionDetection/tweet_senti.csv', encoding='latin-1')
# df.head()

# %%

data = {

    "intention": initial.iloc[:, 0],
    "tweet": initial.iloc[:, 5]

}

df = pd.DataFrame(data)


for i, row in df.iterrows():

    if (df.at[i, 'intention'] != 0):
        df.at[i, 'intention'] = 1


df['intention'].value_counts()

# %%


def text_cleaning(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)     # removing @mentions
    text = re.sub(r'@[A-Za-zA-Z0-9]+', '', text)  # removing @mentions
    text = re.sub(r'@[A-Za-z]+', '', text)        # removing @mentions
    text = re.sub(r'@[-)]+', '', text)            # removing @mentions
    text = re.sub(r'#', '', text)                # removing '#' sign
    text = re.sub(r'RT[\s]+', '', text)           # removing RT
    text = re.sub(r'https?\/\/\S+', '', text)     # removing the hyper link
    text = re.sub(r'&[a-z;]+', '', text)          # removing '&gt;'

    return text


# %%
df['tweet'] = df['tweet'].apply(text_cleaning)
df.head()

# %%

x_train, x_test, y_train, y_test = train_test_split(
    df['tweet'].values, df['intention'].values, test_size=0.30)



# %%
print("twitt:", x_train[0])
print("sentiment:", y_train[0])

# %%

max_vocab = 20000000
tokenizer = Tokenizer(num_words=max_vocab)
tokenizer.fit_on_texts(x_train)

# %%
wordidx = tokenizer.word_index
V = len(wordidx)
print('The size of the database vocab is: ', V)

# %%
# converting tran and test sentences into sequences
train_seq = tokenizer.texts_to_sequences(x_train)
test_seq = tokenizer.texts_to_sequences(x_test)

print('Training sequence: ', train_seq[0])
print('Testing sequence: ', test_seq[0])

# %%
# padding the sequences to get equal length sequence because its conventional to use same size sequences
# padding the traing sequence
pad_train = pad_sequences(train_seq,maxlen=200)
T = pad_train.shape[1]
print('The length of training sequence is: ', T)

# %%
pad_test = pad_sequences(test_seq, maxlen=T)
print('The length of testing sequence is: ', pad_test.shape[1])

# %%
# building the model


D = 20  # dimension embedding layer
M = 15  # dimension of lstm layer

i = Input(shape=(T, ))
# V+1 because the indexing of the words in vocab (V) start from 1 not 0
x = Embedding(V+1, D)(i)
x = LSTM(M, return_sequences=True)(x)
x = GlobalMaxPooling1D()(x)
x = Dense(32, activation='relu')(x)
x = Dense(1, activation='sigmoid')(x)

model = Model(i, x)

# %%
model.compile(optimizer='adam', loss='BinaryCrossentropy',
              metrics=['accuracy'])
# model.summary()
# %%
r = model.fit(pad_train, y_train, validation_data=(pad_test, y_test), epochs=2)

tf.keras.utils.plot_model(model = r ,to_file='model.png')
#%%
# Evaluating the model
# plotting the loss and validation loss of the model
plt.plot(r.history['loss'], label='loss')
plt.plot(r.history['val_loss'], label='val_loss')
plt.legend()
#%%
# plotting the accuracy and validation accuracy of the model
plt.plot(r.history['accuracy'], label='accuracy')
plt.plot(r.history['val_accuracy'], label='val_accuracy')
plt.legend()

# %%
# Predicting the sentiment of any text


def predict_sentiment(text):
    # preprocessing the given text
    text_seq = tokenizer.texts_to_sequences(text)
    text_pad = pad_sequences(text_seq, maxlen=T)

    # predicting the class
    predicted_sentiment = model.predict(text_pad).round()

    print(model.predict(text_pad))

    if predicted_sentiment == 1.0:
        return(print('It is a positive sentiment'))
    else:
        return(print('It is a negative sentiment'))


# %%
text = ['hahahahahaha funny cute']
predict_sentiment(text)
# %%%%
x = ['no one cares about me. i will die alone']
predict_sentiment(x) 
# %%
# saving the model for future purpose
# path = './model.h5'
# model.save(path )

# %%
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
# %%
