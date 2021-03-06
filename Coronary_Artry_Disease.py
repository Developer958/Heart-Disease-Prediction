#Problem Coronary_artry
Coronary artry infection is the development of plaque in the corridors that supply oxygen-rich blood to your heart. Plaque causes a limiting or blockage that could bring about a heart attack. Side effects incorporate chest torment or inconvenience and windedness.

#Import Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from matplotlib.ticker import StrMethodFormatter
from sklearn.feature_selection import SelectKBest, chi2
from pandas.plotting import andrews_curves
from scipy import stats

"""#Add Sql Database"""

db = sqlite3.connect('heart_disease.db')
data_frame = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/heart.csv')
dbt = db.cursor()
dbt.execute('DROP TABLE IF EXISTS Heart_Disease')
data_frame.to_sql('Heart_Disease', db, if_exists='append', index=False)

"""#Import Dataset from Sql Database"""

db = sqlite3.connect("heart_disease.db")
qry = """

SELECT * FROM Heart_Disease

"""
df = pd.read_sql_query(qry, db)
df.head()

"""#Data Preprocessing"""

df.isna().sum()

df = df.rename(columns={"sex":"gender"})
df = df.rename(columns={"cp":"Chest_Pain"})
df = df.rename(columns={"chol":"cholestrol"})
df = df.rename(columns={"target":"coronary_artry"})
df.reset_index() 
df.head()

df.shape

df.info()

df['coronary_artry'].value_counts().index

"""#Data Analysis"""

plt.figure(figsize=(10,8))
corr_df = df.corr()
sns.heatmap(corr_df,annot=True)

sns.countplot(x='coronary_artry',data=df,palette=['green','red'])
plt.xlabel('Heart Disease')
plt.legend(['Not Affected','Affected'])
plt.title('')
plt.show()

cross_s_t=pd.crosstab(df.gender,df.coronary_artry)
cross_s_t.plot(kind='bar')
plt.title('Heart Disease by Gender ')
plt.show()

cross_s_t=pd.crosstab(df.Chest_Pain,df.coronary_artry)
cross_s_t.plot(kind='bar')
plt.title('Heart Disease by Chest pain')
plt.show()

categorical_val = []
continous_val = []
for column in df.columns:
    if len(df[column].unique()) <= 10:
        categorical_val.append(column)
        print(f"{column} : {df[column].unique()}")
    else:
        continous_val.append(column)

data=df
plt.figure(figsize=(15, 15))

for i, column in enumerate(categorical_val, 1):
    plt.subplot(3, 3, i)
    data[data["coronary_artry"] == 0][column].hist(bins=35, color='green', label='Have Heart Disease = NO',alpha=0.6)
    data[data["coronary_artry"] == 1][column].hist(bins=35, color='red', label='Have Heart Disease = YES',alpha=0.6)
    plt.legend()
    plt.xlabel(column)

x = df.iloc[:,0:13]
y = df.iloc[:,-1]

BestFeature = SelectKBest(score_func=chi2, k=13)
fit = BestFeature.fit(x, y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(x.columns)
featureScores= pd.concat([dfcolumns,dfscores], axis=1)
featureScores.columns = ['Column','Score']
featureScores

"""#Feature Extraction"""

categorical_val = []
continous_val = []
for column in df.columns:
    if len(df[column].unique()) <= 10:
        categorical_val.append(column)
        print(f"{column} : {df[column].unique()}")
    else:
        continous_val.append(column)

X = data.drop(columns='coronary_artry', axis = 1)
Y = data['coronary_artry']

X

Y
