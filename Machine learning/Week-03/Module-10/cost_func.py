# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# %%
x = np.array([1, 3, 4, 6, 7])  # years of experience
y = np.array([15, 35, 45, 65, 75])  # salary

sns.scatterplot(x=x, y=y)
plt.xlabel("years of experience")
plt.ylabel("salary")

plt.show()

# %%
# y = mx + c
# f(x) = weights * x + bias


# prediction function
def make_prediction(x, y, w, b):
    m = x.shape[0]
    prediction_list = np.zeros((m,))
    for i in range(m):
        prediction_list[i] = w * x[i] + b
    return prediction_list


# %%
# initial test using the function
w = 10
b = 3
prediction = make_prediction(x, y, w, b)

# show in graph the initial result
sns.scatterplot(x=x, y=y)
plt.xlabel("years of experience")
plt.ylabel("salary")
plt.plot(x, prediction)
plt.legend()
plt.show()


# %%
# find the accuracy of predictive models using MSE (mean squaredd error)
def cost_calculation(x, y, w, b):
    n = x.shape[0]
    cost = 0.0
    for i in range(n):
        y_cap = w * x[i] + b
        se = pow(y[i] - y_cap, 2)
        cost += se

    cost /= n
    return cost


cost = cost_calculation(x, y, w=10, b=3)

# %%
# visualisation
sns.scatterplot(x=x, y=y, label=f"prediction: {cost}")
plt.plot(x, prediction)
plt.legend()
plt.show()

# %%
# idea of minimizing cost function
w = []
cost_history = []

for i in range(-100, 100):
    cost_i = cost_calculation(x, y, w=i, b=0)
    w.append(i)
    cost_history.append(cost_i)

plt.plot(w, cost_history)
plt.grid(visible=True)
plt.show()