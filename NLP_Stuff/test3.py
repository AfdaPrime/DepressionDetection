# %%

from sklearn.metrics import classification_report
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

from keras.preprocessing.text import Tokenizer

from sklearn.model_selection import train_test_split
import re

import pandas as pd

import pickle

# %%
# loading the dataset
initial = pd.read_csv(
    'D:/newCode/Machine Learning/DepressionDetection/tweet_senti.csv', encoding='latin-1')
initial.head()

# %%
# add the only intention and tweet
data = {

    "intention": initial.iloc[:, 0],
    "tweet": initial.iloc[:, 5]

}

df = pd.DataFrame(data)


for i, row in df.iterrows():

    if (df.at[i, 'intention'] != 0):
        df.at[i, 'intention'] = 1


df.head()

# %%
df['intention'].value_counts()

# %%
# Preprocessing function to clean up the dataset


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
# Cleaning the data
df['tweet'] = df['tweet'].apply(text_cleaning)
df.head()

# %%

tfidf = TfidfVectorizer(
    max_features=20000000, ngram_range=(1, 3), analyzer='char')
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

pkl_filename = "twitter_NLP_svm.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(clf, file)

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
x = 'I am so single'
x = text_cleaning(x)
vec = tfidf.transform([x])
clf.predict(vec)
# %%
x = 'I am so HAPPY. i fell so alive'
x = text_cleaning(x)
vec = tfidf.transform([x])
clf.predict(vec)
# %%
