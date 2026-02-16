from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemma = WordNetLemmatizer() # created an object using class called wordnetlemmatizer and we use lemmatize method later from this object.
text = "playing better studies"
words = word_tokenize(text) # returns list
tokens = []
for word in words:
    tokens.append(lemma.lemmatize(word)) # here there is no pos tag so by default all the words in list treated as "noun"
print(tokens) # ['playing', 'better', 'study']
# Because lemmatizer needs grammar info (POS tag) to work perfectly.
