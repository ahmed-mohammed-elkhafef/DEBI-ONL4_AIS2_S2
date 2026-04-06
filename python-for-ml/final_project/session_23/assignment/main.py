from activations import Activations
from chain_rule import ChainRule
from gradients import Gradients
from net import net
from update import update
from visualization import plot_error


# Activation
activation = Activations.sigmoid
activation_derivative = Activations.sigmoid_derivative


# Data
X1, X2 = 0.05, 0.10
t1, t2 = 0.01, 0.99

# weights
W1, W2, W3, W4 = 0.15, 0.20, 0.25, 0.30
W5, W6, W7, W8 = 0.40, 0.45, 0.50, 0.55

# bias
B1, B2 = 0.35, 0.60

lr = 0.5
epochs = 10000

errors = []

print("Start Training...\n")

for epoch in range(epochs):

    # ========= Forward =========
    net_h1 = net([X1, X2], [W1, W2], B1)
    h1 = activation(net_h1)

    net_h2 = net([X1, X2], [W3, W4], B1)
    h2 = activation(net_h2)

    net_o1 = net([h1, h2], [W5, W6], B2)
    o1 = activation(net_o1)

    net_o2 = net([h1, h2], [W7, W8], B2)
    o2 = activation(net_o2)

    # ========= Error =========
    E = 0.5 * (t1 - o1)**2 + 0.5 * (t2 - o2)**2
    errors.append(E)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch} | Error: {E:.6f}")

    # ========= Backward =========
    pE_o1 = ChainRule.p_E_p_out(t1, o1)
    pE_o2 = ChainRule.p_E_p_out(t2, o2)

    pO_o1 = ChainRule.p_out_p_net(activation_derivative, o1)
    pO_o2 = ChainRule.p_out_p_net(activation_derivative, o2)

    # output weights
    pW5 = Gradients.output_weight(pE_o1, pO_o1, h1)
    pW6 = Gradients.output_weight(pE_o1, pO_o1, h2)

    pW7 = Gradients.output_weight(pE_o2, pO_o2, h1)
    pW8 = Gradients.output_weight(pE_o2, pO_o2, h2)

    # hidden error
    pE_h1 = Gradients.hidden_error([pE_o1, pE_o2], [pO_o1, pO_o2], [W5, W7])
    pE_h2 = Gradients.hidden_error([pE_o1, pE_o2], [pO_o1, pO_o2], [W6, W8])

    pO_h1 = ChainRule.p_out_p_net(activation_derivative, h1)
    pO_h2 = ChainRule.p_out_p_net(activation_derivative, h2)

    # hidden weights
    pW1 = Gradients.hidden_weight(pE_h1, pO_h1, X1)
    pW2 = Gradients.hidden_weight(pE_h1, pO_h1, X2)

    pW3 = Gradients.hidden_weight(pE_h2, pO_h2, X1)
    pW4 = Gradients.hidden_weight(pE_h2, pO_h2, X2)

    # ========= Bias =========
    pB2 = Gradients.bias(pE_o1, pO_o1) + Gradients.bias(pE_o2, pO_o2)
    pB1 = Gradients.bias(pE_h1, pO_h1) + Gradients.bias(pE_h2, pO_h2)

    # ========= Update =========
    W1, W2, W3, W4 = update([W1, W2, W3, W4],
                            [pW1, pW2, pW3, pW4], lr)

    W5, W6, W7, W8 = update([W5, W6, W7, W8],
                            [pW5, pW6, pW7, pW8], lr)

    B1 -= lr * pB1
    B2 -= lr * pB2


# =========================
# Final Results
# =========================
E_final = errors[-1]

print("\n" + "="*50)
print("Final Results")
print("="*50)

print(f"o1 = {o1:.6f} | target = {t1}")
print(f"o2 = {o2:.6f} | target = {t2}")

print(f"\nFinal Error = {E_final:.10f}")
print(f"Error % ≈ {E_final * 100:.6f}")

print("\nFinal Weights:")
print(f"W1={W1:.6f}, W2={W2:.6f}")
print(f"W3={W3:.6f}, W4={W4:.6f}")
print(f"W5={W5:.6f}, W6={W6:.6f}")
print(f"W7={W7:.6f}, W8={W8:.6f}")

print("\nFinal Bias:")
print(f"B1={B1:.6f}, B2={B2:.6f}")

# ========= Plot =========
plot_error(errors)