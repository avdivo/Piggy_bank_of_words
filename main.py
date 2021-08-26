import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter
from translate import Translator
import goslate

url = 'https://flask-user.readthedocs.io/en/latest/'

response = requests.get(url).content
soup = BeautifulSoup(response, "html.parser")
words = nltk.tokenize.word_tokenize(soup.get_text())
lemm = nltk.stem.WordNetLemmatizer()
words = Counter([lemm.lemmatize(word.lower()) for word in words if word.isalpha() and len(word) > 2])
print(words)
print(len(words))

gs = goslate.Goslate()
cast = sorted([(word, gs.translate(word, 'ru'), cou) for word, cou in words.items()], key=lambda item: item[1], reverse=True)
print(*cast, sep='\n')