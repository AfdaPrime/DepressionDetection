# %%
import os
from keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle

# %%
path = os.path.join('./NLP_Stuff', 'model.h5')
model = tf.keras.models.load_model(path)

path = os.path.join('./NLP_Stuff', 'tokenizer.pkl')
with open(path, 'rb') as f:
    tokenizer = pickle.load(f)
# %%


def predict_sentiment(text):
    # preprocessing the given text
    text_seq = tokenizer.texts_to_sequences(text)
    text_pad = pad_sequences(text_seq, maxlen=200)

    # predicting the class
    return model.predict(text_pad)
