import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
from sklearn.linear_model import SGDClassifier
import sklearn.metrics
from os import listdir
import pymorphy2
from sklearn import cross_validation

# Кроссвалидацию
# Pipeline
# Кластеризация


CLEAN = '/home/max/PycharmProjects/FULL_DATA/CLEAN_DATA/'
MARK = '/home/max/PycharmProjects/FULL_DATA/MARKS_DATA/'
WORD = '/home/max/PycharmProjects/FULL_DATA/WORDS_DATA/'
ALL_DATA = sorted([int(i.split('.')[0]) for i in listdir(CLEAN)])
WORD_DATA = sorted([int(i.split('.')[0]) for i in listdir(WORD)])
AllowedWords = '[а-я]+'

data = []
wordNormal = pymorphy2.MorphAnalyzer()
interesting, boring = [], []
marked = []
unmarked = []
markedD = []
unmarkedD = []

vectorizer = TfidfVectorizer()
metric = sklearn.metrics.roc_auc_score
cls = SGDClassifier(loss='log', alpha=0.00001, penalty='elasticnet', n_iter=10, n_jobs=-1)


def clean_by_words():
    for i in ALL_DATA:
        with open(CLEAN + str(i) + '.txt', 'r') as file:
            text = file.read()
        try:
            open(WORD + str(i) + '.txt', 'r').read()
        except FileNotFoundError:
            with open(WORD + str(i) + '.txt', 'w') as wordfile:
                data.append('')
                for word in re.findall(AllowedWords, text.lower()):
                    normal = wordNormal.normal_forms(word)[0]
                    wordfile.write(normal + ' ')
                    data[-1] += normal + ' '


def check():
    for i in WORD_DATA:
        text = open(WORD + str(i) + '.txt', 'r').read()
        try:
            with open(MARK + str(i) + '.txt', 'r') as mark:
                if mark.read() == '1':
                    interesting.append(i)
            marked.append(i)
            markedD.append(text)
        except:
            unmarked.append(i)
            unmarkedD.append(text)
    data = markedD + unmarkedD
    X = vectorizer.fit_transform(data)
    Y_train = numpy.array([1 if t in interesting else 0 for t in marked])
    X_train = X[:len(markedD), :]
    X_test = X[len(markedD):, :]
    return [X_train, Y_train, X_test]


def make_an(X_train, Y_train, X_test):
    cls.fit(X_train, Y_train)
    every = [[unmarked[i[0]], cls.predict_proba(i[1])[0][1]] for i in enumerate(X_test)]
    sor_every = sorted(every, key=lambda i: i[1])
    return sor_every


def get_score(X_train, Y_train):
    score = cross_validation.cross_val_score(cls, X_train, Y_train, cv=5)
    print("Accuracy: %0.2f (+/- %0.2f)" % (score.mean(), score.std() * 2))
    # 0.95
# a = check()
# make_an(a[0],a[1],a[2])
# get_score(a[0], a[1])
