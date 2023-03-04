import learn as learn
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

hd = pd.read_csv("heartdisease.txt", sep=" ", header=None)
hd_type=pd.read_csv("heartdisease-type.txt",sep=" ", header=None)
print(hd.shape)
print(hd_type)
columns = ["a1n",
"a2s",
"a3s",
"a4n",
"a5n",
"a6s",
"a7s",
"a8n",
"a9s",
"a10n",
"a11s",
"a12n",
"a13s",
"dec"]

hd.columns=columns
print(hd)
print(hd.describe())
print(hd.dtypes)

for x in columns:
    print(x, pd.unique(hd[x]))
    i=0
    for y in pd.unique(hd[x]):
        i= i+1
    print(i)

df = pd.DataFrame(hd)
missing_percentage = 0.1
num_missing_values = int(missing_percentage * df.shape[0])
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a1n'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a2s'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a3s'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a4n'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a5n'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a6s'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a7s'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a8n'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a9s'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a10n'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a11s'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a12n'] = "?"
missing_index = np.random.choice(df.index, num_missing_values, replace=False)
df.loc[missing_index, 'a13s'] = "?"
print(df)

df.replace(to_replace='?', value=np.nan, inplace=True)
print(df.isna().sum())
num_imputer = SimpleImputer(strategy='mean')
df[['a1n', 'a4n', 'a5n', 'a8n', 'a10n', 'a12n']] = num_imputer.fit_transform(df[['a1n', 'a4n', 'a5n', 'a8n', 'a10n', 'a12n']])


cat_imputer = SimpleImputer(strategy='most_frequent')
df[['a2s', 'a3s', 'a6s','a7s', 'a9s', 'a11s', 'a13s']] = cat_imputer.fit_transform(df[['a2s', 'a3s', 'a6s','a7s', 'a9s', 'a11s', 'a13s']])

print(df)
print(df.isna().sum())

scaler = MinMaxScaler(feature_range=(-1, 1))
dfn1 = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(dfn1)

scaler = MinMaxScaler(feature_range=(0, 1))
dfn2 = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(dfn2)

scaler = MinMaxScaler(feature_range=(-10, 10))
dfn3 = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(dfn3)

scaler = StandardScaler()
df['a1ns'] = scaler.fit_transform(df[['a1n']])
df['a1ns'].describe()
df['a1ns2'] = (df['a1n'] - df['a1n'].mean())/df['a1n'].std()
print(df['a1ns2'].describe())

cm = pd.read_csv("Churn_Modelling.csv")
print(cm)
dummy = pd.get_dummies(cm['Geography'])
cm = pd.concat([cm, dummy], axis=1)
print(dummy)
print(cm)
cm = cm.drop("France", axis=1)
print(cm)