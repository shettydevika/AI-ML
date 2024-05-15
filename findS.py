import pandas as pd
df=pd.read_csv('EnjoySport.csv')
#df=df.drop(['slno'], axis=1)
column_length=df.shape[1]
df.head()

================================================

h=['0'] * (column_length-1)
hp=[]
hn=[]

================================================

for training_example in df.values:
    if training_example[-1]!= 'no':
        hp.append(list(training_example))
    else:
        hn.append(list(training_example))

=================================================

for  i in range(len(hp)):
    for j in range (column_length-1):
        if (h[j] == '0'):
            h[j]=hp[i][j]
        if (h[j]!=hp[i][j]):
            h[j]='?'
        else:
            h[j]=hp[i][j]

=====================================================

print(f'Positive Hypothesis:\n{hp}')
print(f'Negavtive Hypothesis:\n{hn}')
print(f'Maximally Specific Hypothesis:\n{h}')

====================================================
'''OUTPUT
Positive Hypothesis:
[['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'], ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'], ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']]
Negavtive Hypothesis:
[['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no']]
Maximally Specific Hypothesis:
['sunny', 'warm', '?', 'strong', '?', '?']'''
