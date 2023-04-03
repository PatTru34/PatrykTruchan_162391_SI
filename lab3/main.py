import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# pierwszy tydzień
# lata = np.array([2000, 2002, 2005, 2007, 2010]).reshape(-1, 1)
# bezrobocie = np.array([6.5, 7.0, 7.4, 8.2, 9.0])
#
# reg = LinearRegression().fit(lata, bezrobocie)
#
# def prognoza(y):
#     return reg.predict(np.array([y]).reshape(-1, 1))[0]
#
# y = 2010
# while prognoza(y) < 12:
#     y += 1
#
# plt.scatter(lata, bezrobocie, color='green', label='Bezrobocie w danym roku')
# plt.plot(lata, reg.predict(lata), color='blue', label='Regresja liniowa')
# plt.xlabel('Rok')
# plt.ylabel('Procent bezrobotnych')
# plt.legend()
# plt.show()
#
# wynik=prognoza(2025)
# print("Wynik modelu regresji liniowej dla roku 2025: "+str(round(wynik,3)))
# print("Procent bezrobotnych przekroczy 12% w roku:"+str(y))
#

# drugi tydzień


# def step_function(x):
#     return np.where(x>=0, 1, 0)
#
# def perceptron_learn(inputs, outputs, learning_rate, num_iterations):
#
#     weights = np.random.rand(inputs.shape[1])
#
#     for iteration in range(num_iterations):
#         weighted_sum = np.dot(inputs, weights)
#
#         activated_output = step_function(weighted_sum)
#
#         error = outputs - activated_output
#
#         weights += learning_rate * np.dot(inputs.T, error)
#
#     return weights
#
# inputs_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# outputs_and = np.array([0, 0, 0, 1])
# weights_and = perceptron_learn(inputs_and, outputs_and, 0.1, 100)
#
# inputs_not = np.array([[0], [1]])
# outputs_not = np.array([1, 0])
# weights_not = perceptron_learn(inputs_not, outputs_not, 0.1, 100)
#
# print("Wagi dla funkcji AND:", weights_and)
# print("Wagi dla funkcji NOT:", weights_not)


