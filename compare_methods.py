from timeit import timeit

setup = "from collections import Counter; text = 'ah list of ah words'; t = text.split()"

# around 0.04
timeit('Counter(t)', setup=setup, number=10000)

setup = "import nltk; text = 'ah list of ah words'; t = text.split()"

# around 0.07
timeit('nltk.FreqDist(t)', setup=setup, number=10000)

setup = """from sklearn.feature_extraction.text import CountVectorizer as CV;
vec = CV();
text = ['ah list of ah words']
"""

# around 5.5s
timeit('vec.fit_transform(text)', setup=setup, number=10000)