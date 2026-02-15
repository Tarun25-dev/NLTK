import string 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Machine Learning is AMAZING, and NLP is powerful!!!"

# convert lowercase
text = text.lower()

# remove puncuations
for ch in string.punctuation:
    text = text.replace(ch,"")

# removing stopwords

unfiltered_words=word_tokenize(text)
stop_words = stopwords.words("english")
filtered_words = []
for word in unfiltered_words:
    if word not in stop_words:
        filtered_words.append(word)
print(filtered_words) # ['machine', 'learning', 'amazing', 'nlp', 'powerful']