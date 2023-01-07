"""Build an Artificial Neural Network by implementing the Backpropagation algorithm and test the same using
appropriate data sets """

import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

# Scale units
X = X / np.amax(X, axis=0)
y = y / 100


# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid Function
def derivative_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


epoch = 17000
lr = 0.1
ip_layer = 2
hidn_layer = 3
weight = np.random.uniform(size=(ip_layer, hidn_layer))
bias = np.random.uniform(size=(1, hidn_layer))

for iterations in range(epoch):
    inp = X
    weighted_sum = np.dot(inp, weight)+bias
    final_output = sigmoid(weighted_sum)

    error = final_output-y
    second_der = derivative_sigmoid(final_output)
    derivative = error*second_der

    t_inp = inp.T  # transpose of input
    final_d = np.dot(inp.T, derivative)
    weight = weight-lr*final_d

    for updates in derivative:
        bias = bias-lr*updates
op_layer = np.mean(final_output, axis=1)
print("Input: \n" + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n", op_layer)
print("Error: \n" + str(np.mean(np.square(y - op_layer[0]))))

# CUSTOM INPUT
pred = np.array([0.66666667, 1.])
# pred = pred/np.amax(X, axis=0)
result = np.dot(pred, weight)+bias
result = sigmoid(result)
print("Predicted result for [2,9] is: ", result[0][0])
