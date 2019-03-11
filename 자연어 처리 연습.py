import pandas as pd #for data storing
from bs4 import BeautifulSoup #for removing html tag
import re #regular expression
import nltk
from nltk.corpus import stopwords #for removing stopwords
from nltk.stem.snowball import SnowballStemmer #for making word to stem
from nltk.stem import WordNetLemmatizer #음소표기법. 단어의 보조 정리 또는 사전 형식에 의해 식별되는 단일 항목으로 분석 될 수 있도록 굴절 된 형태의 단어를 그룹화하는 과정. ex) 평소보다 두 배로 많이 먹어서 배가 아프다. <- '배'라는 단어가 다른 뜻으로 쓰임

def review_to_words( raw_review) :
    #1.html 태그 제거
    review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
    #2. 정규식을 이용해서 영문자가 아닌 문자는 공백으로 전환
    letters_only = re.sub('[^a-zA-Z]', ' ', review_text)
    #3. 소문자로 변환
    words = letters_only.lower().split()
    #4. 파이썬에서는 리스트보다 세트로 찾는게 훨씬 빠르다.
    # 그러므로 stopwords를 세트로 변환한다.
    stops = set(stopwords.words('english'))
    #5. stopwords(불용어) 제거
    meaningful_words = [w for w in words if not w in stops]
    #6. 어간 추출(stemming)
    stemmer = SnowballStemmer('english') #make stemmer
    stemming_words = [stemmer.stem(w) for w in meaningful_words]
    #7. 공백으로 구분된 문자열로 결합하여 결과를 반환
    return( ' '.join(stemming_words) )

train = pd.read_csv('./data/labeledTrainData.tsv', header=0, delimiter='\t', quoting=3)
test = pd.read_csv('./data/testData.tsv', header=0, delimiter = '\t', quoting = 3)
#print(train.shape)

clean_review = review_to_words(train['review'][0])
print(type(clean_review))
#print(clean_review)
