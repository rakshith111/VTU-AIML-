
import matplotlib.pyplot as plt

from math import ceil
import numpy as np
from scipy import linalg


def lowess(x, y, f, iterations):
    '''
    x: an array of independent variables
    y: an array of dependent variables
    f: the smoothing span, which is a value between 0 and 1 that determines the amount of smoothing to apply. A larger value of f will result in a smoother curve. 
    iter: the number of robustifying iterations to perform. The function will run faster with a smaller number of iterations, but may be less robust to outliers. 
    h is a list of values that represent the bandwidths (smoothing distances) used at each point in the independent variable x. Specifically, h[i] is the bandwidth used when fitting the linear regression model at x[i].
    r is a variable that represents the smoothing distance used at each point in the independent variable x. 
    w is a matrix that represents the weights used in the linear regression model at each point in the independent variable x. Specifically, w[i, j] is the weight used when fitting the linear regression model at x[i] using the jth point in the independent variable x.
    yest is a list of values that represent the fitted values of the dependent variable y. Specifically, yest[i] is the fitted value of y at x[i].
    delta is a list of values that represent the robustifying weights used at each point in the independent variable x. Specifically, delta[i] is the robustifying weight used when fitting the linear regression model at x[i].
    A is a 2x2 matrix that is constructed from the weights w[:, i] at each point x[i], and b is a vector of length 2 that is constructed from the weighted sums of y and y * x
    beta  is a vector of regression coefficients that is being solved for, and A and b are the matrices and vectors of known quantities. 
    '''
    n = len(x)
    r = int(ceil(f * n))
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)]
    w = np.clip(np.abs((x[:, None] - x[None, :]) / h), 0.0, 1.0)
    w = (1 - w ** 3) ** 3
    yest = np.zeros(n)
    delta = np.ones(n)
    for iteration in range(iterations):
        for i in range(n):
            weights = delta * w[:, i]
            b = np.array([np.sum(weights * y), np.sum(weights * y * x)])
            A = np.array([[np.sum(weights), np.sum(weights * x)],
                         [np.sum(weights * x), np.sum(weights * x * x)]])
            beta = linalg.solve(A, b)
            yest[i] = beta[0] + beta[1] * x[i]

        residuals = y - yest
        s = np.median(np.abs(residuals))
        delta = np.clip(residuals / (6.0 * s), -1, 1)
        delta = (1 - delta ** 2) ** 2

    return yest


n = 100
x = np.linspace(0, 10, n)
y = np.sin(x) + 0.3 * np.random.randn(n)
f = 0.25
iterations = 3
yest = lowess(x, y, f, iterations)


plt.plot(x, y, "r.")

plt.plot(x, yest, "b-")

plt.show()
