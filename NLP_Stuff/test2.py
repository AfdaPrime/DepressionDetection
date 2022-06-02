# %%
from sklearn.metrics import classification_report
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
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

# %%
df = pd.read_csv(
    'D:/newCode/Machine Learning/DepressionDetection/tweet_senti.csv', encoding='latin-1')
df.head()

# %%
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

# %%
tfidf = TfidfVectorizer(
    max_features=20000, ngram_range=(1, 3), analyzer='char')
# %%
X = tfidf.fit_transform(df['tweet'])
Y = df['intention']
# %%
X.shape
# %%
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0)
# %%
clf = LinearSVC()
clf.fit(x_train, y_train)
# %%
y_pred = clf.predict(x_test)
# %%
print(classification_report(y_test, y_pred))
# %%
x = 'no one cares about me. i will die alone'
x = text_cleaning(x)
vec = tfidf.transform([x])
clf.predict(vec)
# %%
x = 'today i am so happy. thank a lot'
x = text_cleaning(x)
vec = tfidf.transform([x])
clf.predict(vec)
# %%
x = 'It is sometimes a way for people to escape pain or suffering'
x = text_cleaning(x)
vec = tfidf.transform([x])
clf.predict(vec)
# %%
