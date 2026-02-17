# Before we work with NER we need to downdload two models for NER
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

import nltk
from nltk.tokenize import word_tokenize
from nltk import ne_chunk # used to detect real named entities 
text = "Tarun is learning AI at Google in India."
tokens = word_tokenize(text) # ['Tarun', 'is', 'learning', 'AI', 'at', 'Google', 'in', 'India', '.']
pos_tag = nltk.pos_tag(tokens)
# [('Tarun', 'NNP'), ('is', 'VBZ'), ('learning', 'VBG'), ('AI', 'NNP'), ('at', 'IN'), ('Google', 'NNP'), ('in', 'IN'), ('India', 'NNP'), ('.', '.')]
named_entities = ne_chunk(pos_tag)
print(named_entities)

# (Tarun PERSON)
# (Google ORGANIZATION)
# (India GPE) - GPE = Geo Political Entity (country, city)
