# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
X = np.array([1, 3, 4, 6, 7])  # years of exp
Y = np.array([15, 35, 45, 65, 75])  # salary

sns.scatterplot(x=X, y=Y)
plt.show()


# %%
def make_prediction(X, Y, w, b):
    m = X.shape[0]
    pred_list = np.zeros((m,))
    for i in range(m):
        pred_list[i] = w * X[i] + b
    return pred_list


# %%
prediction = make_prediction(X, Y, 10, 5)
print(prediction)
sns.scatterplot(x=X, y=Y)
plt.plot(X, prediction)


# %%
def compute_cost(X, Y, w, b):
    m = X.shape[0]  # number of data points
    cost = 0.0
    for i in range(m):
        pred = w * X[i] + b
        error = pred - Y[i]
        error_squared = error**2
        cost = cost + error_squared

    cost = cost / m
    return cost

w = 0.0
b = 0.0

prediction = make_prediction(X, Y, 10, 5)
print(prediction)
sns.scatterplot(x=X, y=Y)
plt.plot(X, prediction)
plt.title(f"cose {compute_cost(X, Y, 0, 0)}, for w = {w, b}")
