import nltk
nltk.download("maxent_ne_chunker")
nltk.download('words')

"""
maxent_ne_chunker (Maximum Entropy Named Entity Chunker model) : 
It allows NLTK to recognize named entities(like: peoples, organizations, locations, dates, etc.)

For Example:
"Tarun lives in India and works at Google."

The chunker can identify:

Tarun → PERSON
India → GPE (Geopolitical entity)
Google → ORGANIZATION

>> It is used to decide the most probable named entity for a given chunk of text.

"""

"""
words : This downloads the NLTK words corpus, which is basically a list of english words.
>> The named entity chunker uses it to check if a word exists in English.
>> It helps the model distinguish between valid words and non-words, improving accuracy in recognizing entities.

"""