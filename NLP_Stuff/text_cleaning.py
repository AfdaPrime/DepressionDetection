import re
from sklearn.feature_extraction.text import TfidfVectorizer


def text_cleaning(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)     # removing @mentions
    text = re.sub(r'@[A-Za-zA-Z0-9]+', '', text)  # removing @mentions
    text = re.sub(r'@[A-Za-z]+', '', text)        # removing @mentions
    text = re.sub(r'@[-)]+', '', text)            # removing @mentions
    text = re.sub(r'#', '', text)                # removing '#' sign
    text = re.sub(r'RT[\s]+', '', text)           # removing RT
    text = re.sub(r'https?\/\/\S+', '', text)     # removing the hyper link
    text = re.sub(r'&[a-z;]+', '', text)          # removing '&gt;'
    text = re.sub(r'[\\n]+', '', text)

    return text
