from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet # used for conversion pos tree to wordnet pos
import nltk
lemma = WordNetLemmatizer()
text = "running runs runner easily studies flying"
words = word_tokenize(text)
pos_tags = nltk.pos_tag(words) # # Assign POS tags automatically returns list with(word,pos)

# Function to convert Treebank POS → WordNet POS
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # default to noun
tokens = []    
for word,tag in pos_tags:
    postag = get_wordnet_pos(tag)
    tokens.append(lemma.lemmatize(word,pos=postag))
print(tokens) # ['run', 'run', 'runner', 'easily', 'study', 'fly']





# | Shortcode | Full Form                              | Example/Meaning              |
# | --------- | -------------------------------------- | ---------------------------- |
# | **VBG**   | Verb, Gerund / Present Participle      | running, flying              |
# | **NNS**   | Noun, Plural                           | runs, studies                |
# | **VBP**   | Verb, Present, non-3rd person singular | runner (tagged as verb here) |
# | **RB**    | Adverb                                 | easily                       |
