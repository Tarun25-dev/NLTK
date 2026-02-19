# to do feature extraction we need to install sklearn they provides methods to do this feature extractions
# NLTK handles preprocessing.
# Sklearn handles vectorization.
from sklearn.feature_extraction.text import CountVectorizer
# feature_extraction is sub-module in sklearn used to convert text to numbers
# text is a sub-module of feature_extraction and it contains tools specifically text vectorization and NLP feature creation.
# CountVectorizer is a class in text module
# creates vocabbulary
# counts word frequency
# converts text into numerical matrix
# countVectorizar implements the Bag of Words model.
documents = ["i love java",
             "i love python"
             ]
vectorizer = CountVectorizer() # created an object using countvectorizer class so we can easily use all the methods inside that class.
x = vectorizer.fit_transform(documents) # Learn vocabulary and Convert text to matrix
print(vectorizer.get_feature_names_out()) # ['java' 'love' 'python']
print(x.toarray()) # it gives all the numerical values inside array
# [[1 1 0] 
#  [0 1 1]]

# Inside fit_transform():

# fit(documents) → reads all documents
# Creates vocabulary
# Assigns index numbers
# transform(documents) → converts to matrix

# So vocabulary is created during fit(), not during object creation.