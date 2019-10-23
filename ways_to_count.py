# demonstrates ways to count unique words in Python
from collections import Counter

import nltk
from sklearn.feature_extraction.text import CountVectorizer as CV

text = 'ah list of ah words'
t = text.split()
c = Counter(t)
# get unique words
c.keys()

fd = nltk.FreqDist(t)
# unique words
fd.keys()
# you can plot the distribution easily
fd.plot()
# get words that occur at least a certain number of times
more_than_once = [(f, c) for f, c in fd.items() if c > 1]

# this method is more useful for multiple documents
vec = CV()
res = vec.fit_transform([text])
# same result as counter/FreqDist here
vec.vocabulary_
# get unique words
vec.vocabulary_.keys()