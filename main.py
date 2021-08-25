import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter
from translate import Translator

url = 'https://flask-user.readthedocs.io/en/latest/'
url = 'https://lengish.com/texts/text-1.html'

response = requests.get(url).content
soup = BeautifulSoup(response, "html.parser")
words = nltk.tokenize.word_tokenize(soup.get_text())
lemm = nltk.stem.WordNetLemmatizer()
words = Counter([lemm.lemmatize(word.lower()) for word in words if word.isalpha() and len(word) > 2])
print(words)
print(len(words))

translator = Translator(from_lang="english",to_lang="russian")
cast = sorted([(word, cou) for word, cou in words.items()], key=lambda item: item[1], reverse=True)
print(*cast, sep='\n')