from nltk import word_tokenize
text = "I am learning nlp"
tokens = word_tokenize(text) # it retturns all tokens in a list 
print(tokens) # ['I', 'am', 'learning', 'nlp']

# also use properties like text
tks = word_tokenize(text="i am from indian subcontinent",language="english")
print(tks)