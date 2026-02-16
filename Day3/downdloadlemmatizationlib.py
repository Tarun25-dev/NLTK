import nltk 
nltk.download("wordnet")
nltk.download("omw-1.4")
# NLTK needs external datasets to work with lemmatization.
nltk.download('averaged_perceptron_tagger') #this is used for pos_tag() provides this module.
nltk.download('punkt')
# Download tokenizer data
nltk.download('averaged_perceptron_tagger_eng')