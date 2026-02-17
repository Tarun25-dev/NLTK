import nltk
from nltk.tokenize import word_tokenize
text = "i love coding"
tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)

# [('i', 'NN'), ('love', 'VBP'), ('coding', 'VBG')]

# | Tag | Meaning         |
# | --- | --------------- |
# | NN  | Noun            |
# | NNP | Proper Noun     |
# | VB  | Verb            |
# | VBG | Verb (ing form) |
# | JJ  | Adjective       |
# | RB  | Adverb          |

