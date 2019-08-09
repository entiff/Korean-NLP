# tf-idf.py

from DTM import DTM
import numpy as np


def tf_idf(sentences):
    dtm = DTM(sentences)
    for i in range(len(dtm)):
        for j in range(i):
            if dtm.iloc[i, j] != 0:
                tf = 1
            else:
                tf = 0
            idf = np.log(sum(dtm[dtm.columns[j]]) + 1e-5/len(dtm))
            dtm.iloc[i, j] = tf * idf
    return dtm
