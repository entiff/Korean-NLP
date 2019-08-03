"""
형태소 분석은 형태소, 어근, 접두사/접미사, 품사 등 다양한 언어적 속성의 구조를 파악하는 것이다.
품사 태깅은 형태소의 뜻과 문맥을 고려해 형태소에 태그를 달아주는 것이다.
태그의 가짓수는 형태소 분석기마다 상이하다.(9~56개)
ex) 가방에 들어가신다 -> 가방/NNG + 에/JKM + 들어가/VV + 시/EPH + ㄴ다/EFN

KoNLPy에서 5개의 형태소 분석기(Kkma, Komoran, Hannanum, Okt, Mecab)를 이용할 수 있다.
"""
# 설치 방법
# https://konlpy.org/ko/v0.5.1/install

# 한나눔
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

# 꼬꼬마
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

# 코모란
from konlpy.tag import Komoran

dicpath = "D://koreannlp/dic.txt"
komoran = Komoran(userdic=dicpath)

# 형태소
print(komoran.morphs('코모란도 오픈소스가 되었습니다'))

# 명사
print(komoran.nouns('코모란도 오픈소스가 되었습니다'))

# 품사
print(komoran.pos('코모란도 오픈소스가 되었습니다'))


# Mecab (Mecab() is not supported on Windows)

from konlpy.tag import Mecab

mecab = Mecab(dicpath='usr/local/lib/mecab/mecab-ko-dic')

# 형태소
print(mecab.morphs('Mecab은 여러 형태소 분석기들 가운데 가장 빠른 속도를 자랑합니다'))

# 명사
print(mecab.morphs('Mecab은 여러 형태소 분석기들 가운데 가장 빠른 속도를 자랑합니다'))

# 품사
print(mecab.pos('Mecab은 여러 형태소 분석기들 가운데 가장 빠른 속도를 자랑합니다'))


# Okt (Twitter() has been changed to Okt() since v0.5.0)

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
