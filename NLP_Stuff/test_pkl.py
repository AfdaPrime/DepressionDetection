#%%
import pickle
# import test3
from sklearn.metrics import classification_report
import text_cleaning as tc

#%%
with open('twitter_NLP_svm.pkl','rb') as file:
    clf = pickle.load(file)

# print(classification_report(test3.y_test, test3.y_pred))
# %%
x = 'I am so HAPPY. i fell so alive'
x = tc.text_cleaning(x)
vec = tc.tfidf.transform([x])
clf.predict(vec)
# %%
