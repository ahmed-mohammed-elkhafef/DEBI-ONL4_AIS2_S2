import numpy as np
import matplotlib.pyplot as plt

class LinearRegression_Ahmed:
    """
    Linear Regression model using Gradient Descent.

    Methods:
    fit(x, y) : trains the model and updates weights and bias
    Pred_y(x_new) : predicts target values for new inputs
    score(x_test, y_test) : computes R² score on test data
    visual() : visualizes SSE over iterations and regression line
    poly_features: to adjust polynomial regression  

    Attributes:
    w : float or numpy array = weight(s) of the model
    b : float = bias of the model
    alpha : float = learning rate
    num_iteration : int = number of iterations
    degree : int = polynomial degree
    regularization : str = None, 'ridge', or 'lasso'
    lambda_param : float = regularization strength
    sse_values : list = stores SSE for each iteration
    x_orig : numpy array = original input features used in training
    x : numpy array = processed features (polynomial)
    y : numpy array = target values used in training
    """
    
    def __init__(self, alpha, num_iteration, w=0, b=0, degree=1, regularization=None, lambda_param=0):
        """
        param1 : learning rate
        type   : float
        param2 : number of iterations
        type   : int
        param3 : initial weight
        type   : float
        param4 : initial bias
        type   : float
        param5 : polynomial degree
        type   : int
        param6 : regularization type ('ridge', 'lasso', or None)
        type   : str
        param7 : regularization strength
        type   : float
        return : None
        """
        self.w = w
        self.b = b
        self.alpha = alpha
        self.num_iteration = num_iteration
        self.degree = degree
        self.regularization = regularization
        self.lambda_param = lambda_param

    def _poly_features(self, x):
        """
        param1 : input features
        type   : list or numpy array
        return : polynomial features up to self.degree
        rtype  : numpy array
        """
        x = np.array(x)
        return np.vstack([x**i for i in range(1, self.degree+1)]).T

    def fit(self, x, y):
        """
        param1 : input features
        type   : list or numpy array
        param2 : target values
        type   : list or numpy array
        return : trained weight(s) and bias
        rtype  : tuple (w, b)
        """
        self.sse_values = []
        self.x_orig = np.array(x)
        self.y = np.array(y)
        self.x = self._poly_features(self.x_orig)
        n, m = self.x.shape

        if np.isscalar(self.w):
            self.w = np.zeros(m)

        for i in range(self.num_iteration):
            y_hat = self.x.dot(self.w) + self.b

            D_w = 2/n * self.x.T.dot(y_hat - self.y)
            D_b = 2/n * np.sum(y_hat - self.y)

            if self.regularization == 'ridge':
                D_w += 2 * self.lambda_param * self.w
            elif self.regularization == 'lasso':
                D_w += self.lambda_param * np.sign(self.w)

            self.w -= self.alpha * D_w
            self.b -= self.alpha * D_b

            y_hat = self.x.dot(self.w) + self.b
            sse = np.sum((y_hat - self.y)**2)
            self.sse_values.append(sse)
        
        return self.w, self.b
    
    def Pred_y(self, x_new):
        """
        param1 : new input features
        type   : float or numpy array
        return : predicted values
        rtype  : float or numpy array
        """
        x_new = np.array(x_new)
        x_poly = self._poly_features(x_new)
        return x_poly.dot(self.w) + self.b
    
    def score(self, x_test, y_test):
        """
        param1 : test features
        type   : list or numpy array
        param2 : test target values
        type   : list or numpy array
        return : R2 score
        rtype  : float
        """
        y_test = np.array(y_test)
        y_pred = self.Pred_y(x_test)
        ss_res = np.sum((y_test - y_pred)**2)
        ss_tot = np.sum((y_test - np.mean(y_test))**2)
        return 1 - (ss_res / ss_tot)
    
    def visual(self):
        """
        param : None
        return : None
        Visualizes:
        - SSE over iterations
        - Regression line with dynamic labeling (Linear/Polynomial + Ridge/Lasso)
        """
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(range(len(self.sse_values)), self.sse_values, label='SSE')
        plt.xlabel("iteration")
        plt.ylabel("SSE")
        plt.title("SSE over Iteration")
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.scatter(self.x_orig, self.y, color='blue', label='Data points')

        x_sorted = np.linspace(min(self.x_orig), max(self.x_orig), 200)
        y_sorted = self.Pred_y(x_sorted)

        label = ""
        if self.degree == 1:
            label += "Linear"
        else:
            label += f"Polynomial (deg={self.degree})"
        if self.regularization == 'ridge':
            label += " + Ridge"
        elif self.regularization == 'lasso':
            label += " + Lasso"

        plt.plot(x_sorted, y_sorted, color='red', label=label)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Regression Fit")
        plt.legend()
        plt.show()