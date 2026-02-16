# Stemming - Process of cutting words roughly to base form.
# It may not produce real dictionary words.
from nltk.stem import PorterStemmer
# PorterStemmer is a stemming algorithm created by Martin Porter.
# used to reduce words to their root form (stem).
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer() # creating object from class inside that object we use method called stem for stemming.
text = "playing played plays player"
words = word_tokenize(text)
tokens = []
for word in words:
    tokens.append(stemmer.stem(word))
print(tokens) # ['play', 'play', 'play', 'player']

# Because PorterStemmer follows fixed rule-based steps, not meaning-based understanding.
# It removes common suffixes like:

# ing
# ed
# ly
# s
# ment
