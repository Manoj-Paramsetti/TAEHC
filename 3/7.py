import pandas as pd
import numpy as np
import re

data = pd.read_csv("/content/tweets1.csv")
data
def remove_pattern(input_txt, pattern):
  r = re.findall(pattern,input_txt)
  for i in r:
    input_txt = re.sub(i,'',input_txt)
  return input_txt
print(data)

data['new'] = np.vectorize(remove_pattern)(data ['text'],"@[\w]*")
print(data)

data['new'] = data['new'].str.replace("[^a-zA-Z#]"," ")
print(data)

data['new'] = data['new'].apply(lambda x:' '.join([w for w in x.split() if len(w) > 3]))
print (data)

tokenized_tweet = data['new'].apply (lambda x:x.split())
print (tokenized_tweet.head())

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
tokenized_tweet = tokenized_tweet.apply(lambda x:[stemmer.stem(i) for i in x])
print (tokenized_tweet.head())
