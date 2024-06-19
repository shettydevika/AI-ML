import pandas as pd
msg=pd.read_csv('naivetext.csv',names=['message','label'])
print('The dimensions of the dataset',msg.shape)

msg['labelnum']=msg.label.map({'pos':1,'neg':0})
X=msg.message
y=msg.labelnum
print(X)
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y)
print('\n The total number of Training data:',y_train.shape)
print('\n The total number of Test data:',y_test.shape)

from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
x_train_dtm=count_vect.fit_transform(x_train)
x_test_dtm=count_vect.transform(x_test)
print('\n The words or tokens in the text documents\n')
print(count_vect.get_feature_names())

df=pd.DataFrame(x_train_dtm.toarray(),columns=count_vect.get_feature_names())
from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB().fit(x_train_dtm,y_train)
predicted=clf.predict(x_test_dtm)

from sklearn import metrics
print('\n Accuracy of classifier is',metrics.accuracy_score(y_test,predicted))
print('\nConfusion matrix')
print(metrics.confusion_matrix(y_test,predicted))
print('\n The value of precision', metrics.precision_score(y_test,predicted))
print('\n The value of recall', metrics.recall_score(y_test,predicted))

'''
Output
The dimensions of the dataset (18, 2)
0                      I love this sandwich
1                  This is an amazing place
2        I feel very good about these beers
3                      This is my best work
4                      What an awesome view
5             I do not like this restaurant
6                  I am tired of this stuff
7                    I can't deal with this
8                      He is my sworn enemy
9                       My boss is horrible
10                 This is an awesome place
11    I do not like the taste of this juice
12                          I love to dance
13        I am sick and tired of this place
14                     What a great holiday
15           That is a bad locality to stay
16           We will have good fun tomorrow
17         I went to my enemy's house today
Name: message, dtype: object
0     1
1     1
2     1
3     1
4     1
5     0
6     0
7     0
8     0
9     0
10    1
11    0
12    1
13    0
14    1
15    0
16    1
17    0
Name: labelnum, dtype: int64

 The total number of Training data: (13,)

 The total number of Test data: (5,)

 The words or tokens in the text documents

['about', 'am', 'and', 'bad', 'beers', 'best', 'boss', 'can', 'dance', 'deal', 'do', 'enemy', 'feel', 'fun', 'good', 'great', 'have', 'holiday', 'horrible', 'house', 'is', 'like', 'locality', 'love', 'my', 'not', 'of', 'place', 'restaurant', 'sandwich', 'sick', 'stay', 'stuff', 'that', 'these', 'this', 'tired', 'to', 'today', 'tomorrow', 'very', 'we', 'went', 'what', 'will', 'with', 'work']

 Accuracy of classifier is 0.6

Confusion matrix
[[2 0]
 [2 1]]

 The value of precision 1.0

 The value of recall 0.3333333333333333

'''
