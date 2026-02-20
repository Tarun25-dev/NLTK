import nltk
import string 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

texts = [

# ---------------- POSITIVE (75) ----------------

"I love this movie",
"This film is amazing",
"What a wonderful experience",
"The acting was brilliant",
"I enjoyed the entire show",
"The story was very interesting",
"Amazing performance by the actor",
"This product works perfectly",
"I am very happy with the service",
"It was a delightful evening",
"The design looks beautiful",
"The food was delicious",
"I highly recommend this place",
"The experience was unforgettable",
"Such a positive vibe",
"I really liked the storyline",
"The customer service was excellent",
"The quality exceeded expectations",
"Everything was handled professionally",
"I feel happy using this app",
"The update improved performance",
"The packaging was neat",
"I appreciate the fast delivery",
"The support team was helpful",
"It works better than expected",
"This is a fantastic app",
"The service was quick and polite",
"I am satisfied with the results",
"The quality is impressive",
"It works smoothly",
"The interface is simple and clean",
"I feel great about this purchase",
"This was a smart decision",
"Completely satisfied with the product",
"It works as promised",
"I am impressed by the quality",
"The event was well organized",
"The music was enjoyable",
"The experience was smooth",
"I loved the atmosphere",
"The hotel stay was comfortable",
"The teacher explained clearly",
"The team did a great job",
"The presentation was excellent",
"I feel confident using this tool",
"The book was inspiring",
"The training session was useful",
"The product is reliable",
"The app runs fast",
"The design is modern",
"I had a pleasant time",
"The movie was entertaining",
"The staff was friendly",
"The service exceeded expectations",
"The performance was outstanding",
"I enjoyed the performance",
"The environment was peaceful",
"The course was informative",
"I liked the features",
"The camera quality is great",
"The battery life is good",
"The software is easy to use",
"The experience was amazing",
"The workshop was helpful",
"The delivery was on time",
"The results are impressive",
"The food tasted amazing",
"The movie was fun to watch",
"The product quality is excellent",
"The support was responsive",
"The design is attractive",
"I feel very satisfied",
"It was worth the money",
"I truly enjoyed it",
"This is one of the best experiences",

# ---------------- NEGATIVE (75) ----------------

"I hate this movie",
"This film is terrible",
"What a waste of time",
"The acting was awful",
"I regret watching this show",
"The story was boring",
"Worst performance ever",
"This product is useless",
"I am very disappointed",
"It was a horrible experience",
"The design looks cheap",
"The food was tasteless",
"I do not recommend this place",
"The experience was frustrating",
"Such a negative vibe",
"I did not like the storyline",
"The customer service was rude",
"The quality was below expectations",
"Everything was poorly managed",
"I feel unhappy using this app",
"The update made it worse",
"The packaging was damaged",
"The delivery was very late",
"The support team was unhelpful",
"It works worse than expected",
"This is a terrible app",
"The service was slow",
"I am unhappy with the results",
"The quality is very poor",
"It stopped working suddenly",
"The interface is confusing",
"I feel cheated",
"This was a bad decision",
"Completely disappointed with the product",
"It does not work as promised",
"I am not impressed",
"The event was badly organized",
"The music was annoying",
"The experience was stressful",
"I disliked the atmosphere",
"The hotel stay was uncomfortable",
"The teacher was unclear",
"The team did a poor job",
"The presentation was boring",
"I feel frustrated using this tool",
"The book was dull",
"The training session was useless",
"The product is unreliable",
"The app crashes often",
"The design is outdated",
"I had a terrible time",
"The movie was disappointing",
"The staff was unfriendly",
"The service was unacceptable",
"The performance was disappointing",
"I did not enjoy the performance",
"The environment was noisy",
"The course was confusing",
"I disliked the features",
"The camera quality is bad",
"The battery drains quickly",
"The software is difficult to use",
"The experience was awful",
"The workshop was unhelpful",
"The delivery was delayed",
"The results are disappointing",
"The food tasted bad",
"The movie was boring to watch",
"The product quality is poor",
"The support was slow",
"The design is unattractive",
"I feel very disappointed",
"It was not worth the money",
"I truly disliked it",
"This is one of the worst experiences"
]

labels = [1]*75 + [0]*75#1 refers to positive and 0 refers to negative
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words("english") # this variable stores all the stop words
def preprocess(text):
    text = text.lower()
    for ch in string.punctuation: # one by one punctuation goes into ch variable
        text = text.replace(ch,"")
    tokens = word_tokenize(text)
    tokens =[lemmatizer.lemmatize(word) for word in tokens if word not in stop_words] # list comprehension       
    return " ".join(tokens)

# clean all the text
cleaned_text =[preprocess(text) for text in texts]

# convert to numbers 
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(cleaned_text)

# split data
x_train,x_test,y_train,y_test = train_test_split(x,labels,test_size=0.2,random_state=42)

# | Variable | Meaning                      |
# | -------- | ---------------------------- |
# | x_train  | Features used to train model |
# | x_test   | Features used to test model  |
# | y_train  | Correct answers for training |
# | y_test   | Correct answers for testing  |

# x = Features (input data)

# In our case:
# It is the Bag of Words matrix
# Each row = one document
# Each column = word frequency
# labels = Output (target) [0,1]

# x → What model sees

# labels → What model should predict

# What is test_size=0.2?

# Means:

# 80% data → Training

# 20% data → Testing

# What is random_state=42?

# It controls randomness.

# Why?
# Because data is shuffled before splitting.

# Using 42 ensures:
# Same split every time you run code.

# (42 is just a common number — any number works.)

# train model
model = MultinomialNB() # create model 
model.fit(x_train,y_train)

# The model learns:

# Which words are common in positive?
# Which words are common in negative?

# prredict 
predictions = model.predict(x_test)
# Model sees unseen test data (x_test)
# It predicts labels
print("Accuracy:",accuracy_score(y_test,predictions))
# This compares:

# Real answers → y_test
# Predicted answers → predictions

# remember one thing if you have more data to train model you got accurate answers.
new_text = input("Enter text: ")
new_text_cleaned = [preprocess(text) for text in new_text]
new_text_vector = vectorizer.transform(new_text_cleaned)

prediction = model.predict(new_text_vector)

if prediction[0] == 1:
    print("Positive Sentiment")
else:
    print("Negative Sentiment")