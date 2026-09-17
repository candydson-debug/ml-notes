#多因子原理搞懂
#回来直接做笔记了
import numpy as np
import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt

data = pd.read_csv("house_price.csv")
print(data.head())

X = data.drop(["price"],axis=1)
y = data.loc[:,"price"]

from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
lr_model.fit(X,y)

y_predict = lr_model.predict(X)
from sklearn.metrics import mean_squared_error,r2_score
MSE = mean_squared_error(y,y_predict)
R2 = r2_score(y,y_predict)

print(MSE,R2)

print("截距:", lr_model.intercept_)
for name, coef in zip(X.columns, lr_model.coef_):
    print(f"{name}: {coef}")