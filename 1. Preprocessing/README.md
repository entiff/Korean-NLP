# 1. [형태소 분석] 
# 2. [설치]
# 3. [형태소 분석기]
# 4. [BP tokenizer] 
# 5. [불용어 처리] 
# 6. [정규 표현식] 

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

## 4. Byte-pair Tokenizer

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

## 5. 불용어 처리(Stop Word)

- 데이터에서 유의미한 단어 토큰만을 선별하기 위해 의미가 없다고 판단되는 단어 토큰을 제거하는 작업입니다. 주로 한국어에서는 관사, 전치사, 조사, 접속사 등이 이에 해당합니다. 

- 불용어를 통해 잘못된 키워드 추출을 방지할 수 있습니다. 문서 내의 단어 빈도 수가 높을 경우, 이를 "키워드"로 판단되는 경우가 많지만, 해당 문서의 정보를 정확히 표현하지 못하기 때문에 일반적으로 불용어로 간주합니다.

  예) '그', '지금', '때', '이제'

  

### 5-1. 영어 데이터에서의 불용어 처리

---

#### 1). NLTK

nltk에서 불용어를 불러오기 위해 nltk.download()를 실행해야 합니다. 

~~~ nltk를 사용하여 불용어 제거하기
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
~~~

#### 2). 불용어 제거

~~~ 영어 데이터 불용어 제거
# nltk에서 제공하는 영어 불용어 확인
print(stopwords.words('english')[:10])

# 불용어 제거
example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example)

result = [w for w in word_tokens if w not in stop_words]
print(word_tokens)
print(result)
~~~



### 5-2. 한국어 데이터에서의 불용어 처리

---

#### 1). 단어 리스트 생성하여 불용어 처리

사용자가 임의의 단어 배열, 또는 특정 단어를 선정하여 불용어로 처리할 수 있습니다.

~~~ 한국어 데이터 단어 리스트 불용어 처리
example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "아무거나 아무렇게나 어찌하든지 같다 비슷하다 예컨대 이럴정도로 하면 아니거든"
stop_words = stop_words.split(' ')

word_tokens = word_tokenize(example)
result = [w for w in word_tokens if w not in stop_words]
print(word_tokens)
print(result)
~~~



#### 2). 형태소 분석기 사용하여 불용어 처리

형태소 분석을 통해 추출된 값을 키워드(가용어)로 사용하여, 이외의 단어를 불용어로 처리할 수 있습니다. 

~~~ 한국어 데이터 형태소분석기 불용어 처리
from konlpy.tag import *
komoran = Komoran()

example = "안녕하세요. 국내 최초 빅데이터 연합 동아리 BOAZ입니다. 머신러닝 및 딥러닝, 데이터 분석에 관심있는 모든 분들의 관심 부탁드립니다. 감사합니다."
nouns = komoran.nouns(example)
print(nouns)
~~~



## 6. 정규표현식

---

관사, 전치사, 조사, 접속사와 같은 특정 형태소의 단어를 불용어로 처리하는 경우 이외에도, 특수문자, 숫자, 불용패턴이 존재하는 경우 정규표현식을 사용합니다.

python에서는 정규표현식 라이브러리(re)를 사용하여 데이터 정제 작업을 수행할 수 있습니다.

tip: [이 곳](https://regex101.com)에서 정규표현식을 실행해 볼 수 있습니다.

### 6-1. 정규표현식 기초

#### 1) 특수 문자

​	.  : 한 개의 임의의 문자 (\n은 제외)

​	$ : 앞의 문자로 문자열이 끝난다.

​	| : "또는"을 의미한다.

​	[ ] : 문자 클래스

​	[-] : 범위

​	[^] : 반대

#### 2) 자주 사용하는 문자 클래스

​	 \\: 역슬래쉬 문자 자체 '\'를 의미
​	\d: 숫자와 매치, [0-9]와 동일
​	\D: 숫자가 아닌 것과 매치, [ ^0-9]와 동일
​	\s: whitespace 문자와 매치, [ \t\n\r\f\v]와 동일. (맨 앞의 빈칸은 공백문자를 의미한다.)
​	\S: whitespace 문자가 아닌 것과 매치, [ ^ \t\n\r\f\v]와 동일
​	\w: 문자와 숫자와 매치, [a-zA-Z0-9_]와 동일
​	\W: 문자와 숫자가 아닌 문자와 매치, [^ a-zA-Z0-9_]와 동일

#### 3) 반복 문자

​	*: * 바로 앞에 있는 문자가 0부터 무한대로 반복 가능 {0,}와 동일. (반복 0회부터 가능)

​	+: 최소 1번 이상 반복될 때 사용{1,} 와 동일 (반복 1회부터 가능)

​	?: 있어도 되고 없어도 되는 것을 의미 {0,1}와 동일

​	{m}: m번 반복 가능

​	{m,n}: m번부터 n번까지 반복 가능 (m또는 n 생략 가능, 생략 시 이상 또는 이하를 의미합니다.)

### 6-2. 정규표현식 re모듈 함수

re 모듈은 python에서 제공하는 정규표현식 모듈입니다. re.compile을 통해 정규표현식을 컴파일 할 수 있으며, 컴파일된 패턴 객체를 사용하여 문자열 검색을 수행할 수 있습니다.

#### 1) compile()

정규표현식을 컴파일하는 함수로, 패턴이 빈번한 경우 미리 컴파일한 이후 사용하면 속도와 편의성에서 유리합니다.

~~~ compile
import re
p = re.compile('[가-힣]+')
~~~

#### 2) match()

문자열의 처음부터 정규식과 매치되는지 조사할 때 사용합니다.

~~~ match
m = p.match('자연어처리')
print(m)

m = p.match('nlp 자연어처리 123')
print(m)

m = p.match(# 이곳에 텍스트를 입력해보면 match되는지 확인할 수 있습니다. )
if m:
	print("match found: ", m.group())
else:
	print("no match")
~~~

#### 3) search()

문자열 전체를 검색하여 정규식과 매치되는지 조사할 때 사용합니다.

~~~ search
m = p.search("자연어처리")
print(m)

m = p.search("nlp 자연어처리 123")
print(m)
~~~

#### 4) findall()

정규식과 매치되는 모든 문자열(substring)을 리스트로 출력합니다.p

~~~ findall
m = p.findall("한국어 자연어처리 튜토리얼 입니다")
print(m)
~~~

#### 5) finditer()

정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려줍니다.

~~~ finditer
m = p.finditer("한국어 자연어처리 튜토리얼 입니다")
print(m)
for n in m:
	print(n)
# findall과 동일하지만 그 결과로 반복 가능한 객체를 반환합니다.
~~~

#### 6) split()

입력된 정규 표현식을 기준으로 문자열들을 분리하여 리스트로 출력합니다.

~~~ split
## 위와 같이 compile을 통해 패턴을 지정해두고 함수를 거친 match 객체에 메서드를 사용할 수 있고, 이와 같이 compile을 사용하지 않고 해당 매서드에 패턴을 바로 입력받아 사용할 수 있습니다.

example = "우리+같이+자연어처리+공부를+합시다"
result = re.split("\+", example)
print(result)
~~~

#### 7) sub()

정규표현식 패턴과 일치하는 문자열을 찾아 다른 문자열로 대체합니다.

~~~ sub
result = re.sub('[^가-힣]','/','nlp 자연어처리 123')
print(result)
~~~

### 6-3. match 객체

match와 search 메서드를 수행한 결과로 반환되는 match 객체의 메서드를 사용할 수 있습니다.

~~~ match
m_match = p.match("자연어처리")
m_search = p.search("nlp 자연어처리 123")

# group(): 매치된 문자열을 반환
print(m_match.group())
print(m_search.group())

# start(): 매치된 문자열의 시작 위치를 반환
print(m_match.start())
print(m_search.start())

# end(): 매치된 문자열의 끝 위치를 반환
print(m_match.end())
print(m_search.end())

# span(): 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환
print(m_match.span())
print(m_search.span())
~~~

### 6-4. 예제

~~~ example
text = '''안녕하세요    저희는  국내최초 빅데이터 연합동아리 BOAZ 입니다. 한국어 자연어처리(Korean Natural Language Processing) 튜토리얼을 만들기 위해 공부하고 있습니다.    BOAZ 이메일 주소는 boazbigdata@naver.com 이고, 대표 번호는 010-1234-5678 입니다.
올해 19/07/13에 제 10회 컨퍼런스를 진행했습니다. 이에 관한 영상은 공개하고 있으니, 많은 관심 부탁드립니다. 감사합니다!!'''

text_split = re.split('\s+', text)
print(text_split)

text_find = re.findall('\d+', text)
print(text_find)

text_find2 = re.findall('[A-Z]', text)
print(text_find2)

text_find3 = re.findall('[가-힣]{4}', ' ', text)
print(text_find3)

text_sub = re.sub('[^가-힣 ]', ' ', text)
print(text_sub)
~~~

### 6-5. 자주 쓰이는 정규식

1) 전자우편 주소
[a-z0-9_+.-]+@([a-z0-9-]+\.)+[a-z0-9]{2,4}

2) url
(file|gopher|news|nntp|telnet|https?|ftps?|sftp):\/\/([a-z0-9-]+\.)+[a-z0-9]{2,4}.*$

3) HTML 태그
\<(/?[ ^\>]+)\ >

4) 전화 번호
(\d{3}).*(\d{3}).*(\d{4})

5) 날짜
\d{1,2}\/\d{1,2}\/\d{2,4}

6) jpg, gif 또는 png 확장자를 가진 그림 파일명
([ ^\s]+(?=\.(jpg|gif|png))\.\2)

7) 1부터 50 사이의 번호(1과 50 포함)
[1-9]{1}$|^[1-4]{1}[0-9]{1}$|^50$ 

8) 16 진수로 된 색깔 번호
#?([A-Fa-f0-9]){3}(([A-Fa-f0-9]){3})?

~~~ regex
number = re.compile('(\d{3}).*(\d{3}).*(\d{4})')
result = number.search(text)
print(result.group())

email = re.compile('[a-zA-Z0-9_+.-]+@([a-z0-9-]+\.)+[a-z0-9]{2,4}')
result2 = email.search(text)
print(result2.group())

date = re.compile('\d{1,2}\/\d{1,2}\/\d{2,4}')
result3 = date.search(text)
print(result3.group())
~~~

