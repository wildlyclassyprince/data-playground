'''
A predictive model of tweets by US politicians.
'''

# The suspects ...
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

TWEETS = pd.read_csv('senators.csv', encoding='ISO-8859-1',
                     usecols=['text', 'user'])
assert TWEETS.user.unique().shape[0] > 2

VECTORIZER = CountVectorizer(analyzer='word', lowercase=False)

FEATURES = VECTORIZER.fit_transform(TWEETS.text)

FEATURES_ND = FEATURES.toarray()

DATA_LABELS = TWEETS.user

X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(FEATURES_ND,
                                                    DATA_LABELS,
                                                    random_state=1234)
LOG_MODEL = LogisticRegression()
LOG_MODEL = LOG_MODEL.fit(X_TRAIN, Y_TRAIN)
Y_PRED = LOG_MODEL.predict(X_TEST)

TOKEN = random.randint(0, len(X_TEST)-7)
for i in range(TOKEN, TOKEN+7):
    print('Who said it: {}'.format(Y_PRED[0]))
    ind = FEATURES_ND.tolist().index(X_TEST[i].tolist())
    print('What did they say: {}\n'.format(TWEETS.text[ind].strip()))

print('Accuracy: {}%'.format(accuracy_score(Y_TEST, Y_PRED)*100))
