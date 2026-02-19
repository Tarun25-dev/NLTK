# Try this:

# documents = [
#     "AI is powerful",
#     "Machine learning is powerful",
#     "AI and machine learning"
# ]

# Generate:

# Vocabulary
# BoW matrix

from sklearn.feature_extraction.text import CountVectorizer
documents = [
    "AI is powerful",
    "Machine learning is powerful",
    "AI and machine learning"
]
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(documents)

print("Vocabulary: ",vectorizer.get_feature_names_out()) # get_feature_names_out() get the vocabulary from vectorizer.
print("BoW Matrix: \n",x.toarray()) # here x contains (row, column) → value that we convert to array for better understanding 
