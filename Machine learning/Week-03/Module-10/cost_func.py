# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# %%
x = np.array([1, 3, 4, 6, 7, 8, 9, 11])  # years of experience
y = np.array([15, 35, 45, 65, 75, 20, 45, 56])  # salary

sns.scatterplot(x=x, y=y)
plt.xlabel("years of experience")
plt.ylabel("salary")

plt.show()

# %%
# y = mx + c
# f(x) = weights * x + bias


# prediction function
def make_prediction(x, w, b):
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

    cost /= 2 * n
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

# %%
# idea of gradient descent
# calculate gradient


def calculate_gradient(x, y, w, b):
    n = x.shape[0]
    dj_dw = 0.0
    dj_db = 0.0

    for i in range(n):
        prediction = w * x[i] + b
        error = prediction - y[i]
        dj_dw = dj_dw + error * x[i]
        dj_db = dj_db + error

    dj_dw = dj_dw / n
    dj_db = dj_db / n

    return dj_dw, dj_db


# %%
# gradient descent calculation
def gradient_descent(x, y, w_input, b_input, max_iteration, alpha=0.01):
    w = w_input
    b = b_input
    cost_memo = []

    for i in range(max_iteration):
        dj_dw, dj_db = calculate_gradient(x, y, w, b)

        # update
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        cost = cost_calculation(x, y, w, b)
        cost_memo.append(cost)

        # if i % 100 == 0:
        #     print(
        #         f"w: {w:.4f}, b: {b:.4f}, dj_dw: {dj_dw:.4f}, dj_db: {dj_db:.4f}, cost: {cost:.4f}"
        #     )
    return w, b


# %%
w, b = gradient_descent(x, y, 10, 0, max_iteration=7000, alpha=0.01)
print(f"w:{w:.2f}, b:{b:.2f}")

sns.scatterplot(x=x, y=y)
plt.plot(w, b)
plt.show()
