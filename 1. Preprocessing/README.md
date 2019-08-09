## 1. 형태소 분석
형태소 분석은 형태소, 어근, 접두사/접미사, 품사 등 다양한 언어적 속성의 구조를 파악하는 것입니다.
품사 태깅은 형태소의 뜻과 문맥을 고려해 형태소에 태그를 달아주는 것을 말합니다.
태그의 가짓수는 형태소 분석기마다 다릅니다.(9~56개)  
ex) 가방에 들어가신다 -> 가방/NNG + 에/JKM + 들어가/VV + 시/EPH + ㄴ다/EFN

KoNLPy에서 5개의 형태소 분석기(Kkma, Komoran, Hannanum, Okt, Mecab)를 이용할 수 있습니다.  
단, Windows에서는 Mecab을 이용할 수 없습니다.

## 2. [설치](http://konlpy.org/ko/v0.5.1/install)

## 3. 형태소 분석기

### 3-1. 한나눔(Hannanum)

~~~
from konlpy.tag import Hannanum

hannanum = Hannanum()

# 형태소
print(hannanum.morphs('웃으면 복이 옵니다'))
# 형태소 후보군
print(hannanum.analyze('웃으면 복이 옵니다'))
# 명사
print(hannanum.nouns('웃으면 복이 옵니다'))
# 품사(ntags = 9 or 22)
print(hannanum.pos('웃으면 복이 옵니다.'))
~~~

### 3-2. 꼬꼬마(Kkma)

~~~
from konlpy.tag import Kkma

kkma = Kkma()

# 형태소
print(kkma.morphs('이 또한 지나가리라'))

# 명사
print(kkma.nouns('이 또한 지나가리라'))

# 품사
print(kkma.pos('이 또한 지나가리라'))

# 문장 발견
print(kkma.sentences('이 또한 지나가리라'))
~~~

### 3-3. 코모란(Komoran)

~~~
from konlpy.tag import Komoran

dicpath = "D://koreannlp/dic.txt"
komoran = Komoran(userdic=dicpath)

# 형태소
print(komoran.morphs('코모란도 오픈소스가 되었습니다'))

# 명사
print(komoran.nouns('코모란도 오픈소스가 되었습니다'))

# 품사
print(komoran.pos('코모란도 오픈소스가 되었습니다'))
~~~

### 3-4. Mecab

~~~
#Mecab() is not supported on Windows
from konlpy.tag import Mecab

mecab = Mecab(dicpath='usr/local/lib/mecab/mecab-ko-dic')

# 형태소
print(mecab.morphs('Mecab은 여러 형태소 분석기들 가운데 가장 빠른 속도를 자랑합니다'))

# 명사
print(mecab.morphs('Mecab은 여러 형태소 분석기들 가운데 가장 빠른 속도를 자랑합니다'))

# 품사
print(mecab.pos('Mecab은 여러 형태소 분석기들 가운데 가장 빠른 속도를 자랑합니다'))
~~~

### 3-5. Okt

~~~
# Twitter() has been changed to Okt() since v0.5.0
from konlpy.tag import Okt

okt = Okt()

# 형태소
print(okt.morphs('Twitter가 Okt로 새롭게 단장했습니다'))

# 명사
print(okt.nouns('Twitter가 Okt로 새롭게 단장했습니다'))

# 구(phrase) 추출
print(okt.phrases('Twitter가 Okt로 새롭게 단장했습니다'))

# 품사
"""
norm=True이면 token을 normalize한다
stem=True이면 token의 stem을 출력한다
join=True이면 형태소와 품사 태그의 set을 return한다
"""
print(okt.pos('Twitter가 Okt로 새롭게 단장했습니다'))
print(okt.pos('Twitter가 Okt로 새롭게 단장했습니다', norm=True))
print(okt.pos('Twitter가 Okt로 새롭게 단장했습니다', stem=True))
print(okt.pos('Twitter가 Okt로 새롭게 단장했습니다', join=True))
~~~

## 4 - Byte-pair Tokenizer

WordPiece 기반 Tokenizer에서 가장 많이 쓰이는 방법은 데이터 압축 기법인 호프만 코딩을 사용하는 것입니다.
[호프만 코딩](https://ndb796.tistory.com/18)은 특정 문자열의 반복이 빈번하게 일어나는 경우, 하나의 subword unit으로 인식하여 압축하는 기법입니다.

이러한 아이디어를 차용한 tokenizer가 Bpe tokenizer 입니다.

Bpe-Tokenizer는 기존 Komoran이나 세종 등 다른 Corpus에서 품사, 명사, 용언 체언 등 미리 정의 되어있는 단어를 기반으로 tokenize를 하는 것이 아닌,
갖고있는 데이터 기준으로, tokenize 합니다.

따라서 기존의 형태소 분석기처럼 해당 토큰의 형태소가 어떤 품사에 속하는 지는 인지는 알수 없지만 데이터에 기반해 만들어 내므로, 해당 도메인에 맞는 토큰을 가질 수 있습니다.

~~~

## 먼저 학습 시킬 Corpus의 경로를 불러옵니다.
corpus="C:/Users/Jimmy Hong/PycharmProjects/QA/Bpe/KorQuAD_train.csv"
squad=pd.read_csv(corpus)
contexts=set(squad['context'])


# 이후에 tokenize할 데이터셋을 불러옵니다.
sent = '이 형태소 분석기는 기존 단어사전에 있는 단어로 구성하여 분리하는 게 아닌 데이터에 기반한 방법입니다.' \
       '학습시키는 데이터에 따라 형태소가 다르게  될 수 있습니다.'


# 만들어 낼 subword unit 갯수
bpe=BytePairEncoder(n_iters=500)


tokens=bpe.tokenize(sent)

bpe.units

tokens.split(" ")

#tokens=['이_ 형 태 소_ 분 석 기는_ 기 존 _ 단 어 사 전에_ 있는_ 단 어 로_ 구 성 하여_ 분 리 하는_ 게_ 아 닌 _ 데 이 터 에_ 기 반 한_ 방 법 입 니 다.
# 학 습 시키 는_ 데 이 터 에_ 따라_ 형 태 소 가_ 다 르 게_ 될_ 수_ 있 습 니 다._']


# 저장된 단어의 corpus를 저장합니다
bpe.save("./vocab.txt")


# 저장된 단어의 corpus를 불러옵니다.
bpe.load("./vocab.txt")

~~~

#### References

https://ndb796.tistory.com/18
