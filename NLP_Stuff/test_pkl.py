#%%
import pickle
import test3
from sklearn.metrics import classification_report

#%%
with open('twitter_NLP_svm.pkl','rb') as file:
    clf = pickle.load(file)

print(classification_report(test3.y_test, test3.y_pred))
# %%
x = 'I am so HAPPY. i fell so alive'
x = test3.text_cleaning(x)
vec = test3.tfidf.transform([x])
clf.predict(vec)
# %%
