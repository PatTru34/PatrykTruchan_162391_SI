import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(1)
weights_hidden = np.random.uniform(size=(2, 4))
bias_hidden = np.random.uniform(size=(1, 4))
weights_output = np.random.uniform(size=(4, 1))
bias_output = np.random.uniform(size=(1, 1))

learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    hidden_layer_activation = np.dot(X, weights_hidden)
    hidden_layer_activation += bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_activation)

    output_layer_activation = np.dot(hidden_layer_output, weights_output)
    output_layer_activation += bias_output
    predicted_output = sigmoid(output_layer_activation)
    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden = d_predicted_output.dot(weights_output.T)
    d_hidden_output = error_hidden * sigmoid_derivative(hidden_layer_output)

    weights_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    weights_hidden += X.T.dot(d_hidden_output) * learning_rate
    bias_hidden += np.sum(d_hidden_output, axis=0, keepdims=True) * learning_rate

hidden_layer_activation = np.dot(X, weights_hidden)
hidden_layer_activation += bias_hidden
hidden_layer_output = sigmoid(hidden_layer_activation)

output_layer_activation = np.dot(hidden_layer_output, weights_output)
output_layer_activation += bias_output
predicted_output = sigmoid(output_layer_activation)
print(predicted_output)
