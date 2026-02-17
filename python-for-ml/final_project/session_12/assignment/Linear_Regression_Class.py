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

    Attributes:
    w : float = weight of the model
    b : float = bias of the model
    alpha : float = learning rate
    num_iteration : int = number of iterations
    sse_values : list = stores SSE for each iteration
    x : numpy array = input features used in training
    y : numpy array = target values used in training
    """
    
    def __init__(self, alpha, num_iteration, w=0, b=0):
        """
        param1 : initial weight
        type   : float
        param2 : initial bias
        type   : float
        param3 : learning rate
        type   : float
        param4 : number of iterations
        type   : int
        return : None
        """
        self.w = w
        self.b = b
        self.alpha = alpha
        self.num_iteration = num_iteration
    
    def fit(self, x, y):
        """
        param1 : input features
        type   : list or numpy array
        param2 : target values
        type   : list or numpy array
        return : trained weight and bias
        rtype  : tuple (w, b)
        """
        self.sse_values = []
        self.x = np.array(x)
        self.y = np.array(y)
        n = len(self.x)
        
        for i in range(self.num_iteration):
            y_hat = self.w * self.x + self.b
            D_w = 2/n * np.sum((y_hat - self.y) * self.x)
            D_b = 2/n * np.sum(y_hat - self.y)
            
            self.w -= self.alpha * D_w
            self.b -= self.alpha * D_b
            
            y_hat = self.w * self.x + self.b
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
        return self.w * x_new + self.b
    
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
        """
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(range(len(self.sse_values)), self.sse_values, label='SSE')
        plt.xlabel("iteration")
        plt.ylabel("SSE")
        plt.title("SSE over Iteration")
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.scatter(self.x, self.y, color='blue', label='Data point')
        plt.plot(self.x, self.w * self.x + self.b, color='red', label='Regression Line')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Linear Regression fit line")
        plt.legend()
        plt.show()



