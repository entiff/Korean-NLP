# tf-idf.py
from BagofWords import BagOfWords
import pandas as pd


def tf_idf(sentences):
    model = BagOfWords(sentences)

    doc_freq = []
    for i in range(len(sentences)):
        doc_freq.append(list(model.word_count(sentences[i])))

    words = []
    for i in range(len(model.idx2word)):
        word = model.idx2word[i]
        words.append(word)

    return pd.DataFrame(doc_freq, columns=words)
