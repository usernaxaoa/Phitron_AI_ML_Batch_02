# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
X = np.array([1,3,4,6,7]) # years of exp
Y = np.array([15,35,45,65,75]) # salary

sns.scatterplot(x=X, y=Y)
plt.show()
# %%
def make_prediction(X, Y, w, b):
    """
    m = total dataset
    w = weights
    b = bias
    """
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