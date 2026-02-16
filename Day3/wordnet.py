# Wordnet : princeton university developed wordnet.
# It is a large english dictionary database that:
# Groups words into synonyms(synsets)
# stores word meanings
# stores realtionships(noun, verb, adjective)
# WordNetLemmatizer will not work.mainly used for lemmatization this class.

# Example:
# print(lemm.lemmatize("better"))          # default noun
# print(lemm.lemmatize("better", pos='a')) # adjective
# if we dont need to write to every word pos(parts of speech) instead of that we use pos_tag(tokens) in nltk.