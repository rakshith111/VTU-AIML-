import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
Y = np.array(([92], [85], [89]), dtype=float)

# Normalize the inputs
X = X/np.amax(X, axis=0)
Y = Y / 100

# set number of layers
input_layer = 2
hidden_layer = 3
output_layer = 1

# iteratins and learning rate
epochs = 5000
learning_rate = 0.5

# weihts and bias
w1 = np.random.uniform(size=(input_layer, hidden_layer))
b1 = np.random.uniform(size=(1, hidden_layer))
w2 = np.random.uniform(size=(hidden_layer, output_layer))
b2 = np.random.uniform(size=(1, output_layer))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivative_sigmoid(x):
    return x * (1 - x)


# train the model
for i in range(epochs):
    # forward propagation
    # layer 1 to layer hidden
    hidden_out = np.dot(X, w1) + b1
    out1 = sigmoid(hidden_out)
    # Hidden layer to output layer
    final_out = np.dot(out1, w2) + b2
    out2 = sigmoid(final_out)

    # backpropagation
    # last layer to hidden layer
    error_output = Y - out2
    delta_last = derivative_sigmoid(out2) * error_output

    error_hidden = np.dot(delta_last, w2.T)
    delta_hidden = derivative_sigmoid(out1) * error_hidden

    w1 += np.dot(X.T, delta_hidden) * learning_rate
    w2 += np.dot(out1.T, delta_last) * learning_rate

print("Input: \n" + str(X))
print("Actual Output: \n" + str(Y))
print("Predcited Output: \n", out2)
