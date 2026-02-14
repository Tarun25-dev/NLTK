from nltk import sent_tokenize
text = """Artificial Intelligence (AI) is transforming the world. 
From healthcare to finance, AI systems are making tasks faster and more accurate. 
Machine Learning, a subset of AI, allows computers to learn from data and improve over time. 
Natural Language Processing (NLP) helps machines understand human language and communicate effectively. 
With AI technologies advancing rapidly, the possibilities are endless.
"""
tokens = sent_tokenize(text)
print(tokens)

# ['Artificial Intelligence (AI) is transforming the world.', 'From healthcare to finance, AI systems are making tasks faster and more accurate.', 'Machine Learning, a subset of AI, allows computers to learn from data and improve over time.', 'Natural Language Processing (NLP) helps machines understand human language and communicate effectively.', 'With AI technologies advancing rapidly, the possibilities are endless.']
# Overview:
#     I understand basic NLP preprocessing and tokenization using NLTK.