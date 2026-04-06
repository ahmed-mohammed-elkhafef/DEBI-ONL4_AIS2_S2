import math

class Activations:

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    @staticmethod
    def sigmoid_derivative(out):
        return out * (1 - out)

    @staticmethod
    def tanh(x):
        return math.tanh(x)

    @staticmethod
    def tanh_derivative(out):
        return 1 - out**2

    @staticmethod
    def relu(x):
        return max(0, x)

    @staticmethod
    def relu_derivative(out):
        return 1 if out > 0 else 0

    @staticmethod
    def leaky_relu(x, alpha=0.01):
        return x if x > 0 else alpha * x

    @staticmethod
    def leaky_relu_derivative(out, alpha=0.01):
        return 1 if out > 0 else alpha

    @staticmethod
    def linear(x):
        return x

    @staticmethod
    def linear_derivative(out):
        return 1