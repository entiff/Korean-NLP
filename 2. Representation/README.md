## 2. TF-IDF(Term Frequency-Inverse Document Frequency)

TF-IDF는 단어의 빈도와 '역 문서 빈도'라는 방법을 사용하여 DTM내의 각 단어들마다 중요 정도를 가중치로 주는 방법입니다. DTM을 만든 이후, TF-IDF가중치를 주는 방법으로 사용됩니다.

TF-IDF는 문서의 유사도를 구하는 작업, 검색 시스템에서 검색 결과의 중요도를 정하는 작업, 문서 내에서 특정 단어의 중요도를 구하는 작업 등에 쓰일 수 있습니다.

TF-IDF란 TF\*IDF를 의미하며, 문서를 d, 단어를 t, 문서의 총 개수를 n이라고 표현할 때 TF, DF, IDF는 각각 아래와 같이 정의 할 수 있습니다.

### (1) tf(d,t) : 특정 문서 d에서의 특정 단어 t의 등장 횟수.

### (2) df(t) : 특정 단어 t가 등장한 문서의 수.

### (3) idf(d, t) : df(t)에 반비례하는 수.

idf(d,t)=log(n/(1+df(t)))

TF-IDF는 모든 문서에서 자주 등장하는 단어는 중요도가 낮다고 판단하며, 특정 문서에서만 자주 등장하는 단어는 중요도가 높다고 판단합니다. TF-IDF 값이 낮으면 중요도가 낮은 것이며, TF-IDF 값이 크면 중요도가 큰 것입니다. 즉, the나 a와 같이 불용어의 경우에는 모든 문서에 자주 등장하기 마련이기 때문에 자연스럽게 불용어의 TF-IDF의 값은 다른 단어의 TF-IDF에 비해서 낮아지게 됩니다.

```python
sentences = [
    '밥을 맛있게 먹고 싶어요',
    '공부를 하고 싶어요',
    'NLP NLP NLP 잘하고 싶어요'
]
```

```python
from sklearn.feature_extraction.text import CountVectorizer

vector = CountVectorizer()

print(vector.fit_transform(sentences).toarray())

print(vector.vocabulary_)
```
```python
[[0 0 1 1 1 1 0 0]
 [0 1 0 0 0 1 0 1]
 [3 0 0 0 0 1 1 0]]
{'밥을': 4, '맛있게': 2, '먹고': 3, '싶어요': 5, '공부를': 1, '하고': 7, 'nlp': 0, '잘하고': 6}
```

![image.png](https://github.com/shwksl101/Korean-NLP-tutorial/images/tf_idf_image1.png?raw=True)

```python
import numpy as np

def idf(dft,n):
    return np.log(n/(1+dft))
```

```python
arr = vector.fit_transform(sentences).toarray()
```

```
array([[0, 0, 1, 1, 1, 1, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 1],
       [3, 0, 0, 0, 0, 1, 1, 0]], dtype=int64)
```

```python
for i in arr:
    for j in range(len(i)):
        if i[j]!=0:
            dft_arr[j]+=1
```

```python
print(arr)
```

```python
array([[0, 0, 1, 1, 1, 1, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 1],
       [3, 0, 0, 0, 0, 1, 1, 0]], dtype=int64)
```

```python
dft_arr= np.zeros(len(vector.vocabulary_))
print(dft_arr)
```

```
array([0., 0., 0., 0., 0., 0., 0., 0.])
```

```python
idf_arr= np.log(3/(dft_arr+1))
print(idf_arr)
```

```
array([ 0.40546511,  0.40546511,  0.40546511,  0.40546511,  0.40546511,
       -0.28768207,  0.40546511,  0.40546511])
```

```python
tf_idf_arr = arr * idf_arr

print(tf_idf_arr)
```

```
array([[ 0.        ,  0.        ,  0.40546511,  0.40546511,  0.40546511,
        -0.28768207,  0.        ,  0.        ],
       [ 0.        ,  0.40546511,  0.        ,  0.        ,  0.        ,
        -0.28768207,  0.        ,  0.40546511],
       [ 1.21639532,  0.        ,  0.        ,  0.        ,  0.        ,
        -0.28768207,  0.40546511,  0.        ]])
```

```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidfv = TfidfVectorizer().fit(sentences)
print(tfidfv.transform(sentences).toarray())
print(tfidfv.vocabulary_)
```

```python
[[0.         0.         0.54645401 0.54645401 0.54645401 0.32274454
  0.         0.        ]
 [0.         0.65249088 0.         0.         0.         0.38537163
  0.         0.65249088]
 [0.93255764 0.         0.         0.         0.         0.18359452
  0.31085255 0.        ]]
{'밥을': 4, '맛있게': 2, '먹고': 3, '싶어요': 5, '공부를': 1, '하고': 7, 'nlp': 0, '잘하고': 6}
```
