import matplotlib.pyplot as plt

def plot_error(errors):
    plt.plot(errors)
    plt.title("Error Curve")
    plt.xlabel("Epoch")
    plt.ylabel("Error")
    plt.show()