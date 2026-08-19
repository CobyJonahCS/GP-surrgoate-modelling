import pandas as pd 
from sklearn.model_selection import train_test_split

df =  pd.read_csv("../Data/AirfoilSelfNoise.csv")

X = df.drop(columns="SSPL",axis=0)
y = df['SSPL']


X_train, X_test, y_train, y_test = train_test_split(X , y, test_size=0.3,random_state=1000)

print(X_train.shape)
print(X_test.shape)

X_train.to_csv("../Data/X_train.csv",index=False)
X_test.to_csv("../Data/X_test.csv",index=False)

y_train.to_csv("../Data/y_train.csv",index=False)
y_test.to_csv("../Data/y_test.csv",index=False)