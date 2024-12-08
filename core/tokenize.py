import nltk

# nltk.download('punkt')
# nltk.download('punkt_tab')

def tokenize(text):
    sentences = nltk.sent_tokenize(text)
    return sentences