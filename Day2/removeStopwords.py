from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text = "tarun is becoming an ai engineer"
tokens = word_tokenize(text)
stop_words = stopwords.words("english") # this gives all english stopwords if you want to see print(stop_words)
filtered_words = [] # empty list for storing after removing stopwords.

for word in tokens:
    if word not in stop_words:
        filtered_words.append(word)

print(filtered_words) # ['tarun', 'becoming', 'ai', 'engineer']

# Overview :
# I can clean and preprocess text using NLTK including stopword removal and tokenization.