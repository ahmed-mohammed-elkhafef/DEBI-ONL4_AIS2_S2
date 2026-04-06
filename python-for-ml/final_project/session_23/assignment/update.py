def update(weights, grads, lr):
    new_weights = []
    for i in range(len(weights)):
        new_weights.append(weights[i] - lr * grads[i])
    return new_weights