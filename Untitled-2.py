import numpy as np
import pandas as pd
import matplotlib
data = pd.read_csv("generated_data.csv")
print(data.head())

#a = [i for i in range(10)]
#print(a)

x = data.loc[:,"x"]
y = data.loc[:,"y"]
print(x,y)

from matplotlib import pyplot as plt
fig1 = plt.figure(figsize=(5,5))
plt.scatter(x,y)
plt.show()
#设置线性回归模型

from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
#lr_model.fit(x,y)#不接受一维，修改维度

#方法一
x = np.array(x)
y = np.array(y)
x = x.reshape(-1,1)
y = y.reshape(-1,1)
lr_model.fit(x,y)

y_predict = lr_model.predict(x)
print(y_predict)

y_1 = lr_model.predict([[3.5]])
print(y_1)

a = lr_model.coef_
b = lr_model.intercept_
print(a,b)

from sklearn.metrics import mean_squared_error,r2_score
MSE = mean_squared_error(y,y_predict)
R2 = r2_score(y,y_predict)

print(MSE,R2)
#MSE的数值很大，看不出东西，但是R2的0.9472871355942545接近1可以说明效果不错

plt.figure()
plt.scatter(y,y_predict)
plt.show()