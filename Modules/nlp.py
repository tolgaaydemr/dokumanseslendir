from nltk import word_tokenize
from nltk.corpus import stopwords
from TurkishStemmer import TurkishStemmer


def tokenize(text):
    wordstoken = (word_tokenize(text))
    stopWords = set(stopwords.words('turkish'))
    filtered_sentence = [w for w in wordstoken if not w in stopWords]
    filtered_sentence = []
    for w in wordstoken:
        if w not in stopWords:
            filtered_sentence.append(w)
    stemmer = TurkishStemmer()
    stemmerText = []
    for i in filtered_sentence:
        s = stemmer.stem(i)
        stemmerText.append(s)
    return stemmerText
