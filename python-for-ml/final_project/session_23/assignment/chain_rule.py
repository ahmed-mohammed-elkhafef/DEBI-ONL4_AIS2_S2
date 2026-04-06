class ChainRule:

    @staticmethod
    def p_E_p_out(target, out):
        return -(target - out)

    @staticmethod
    def p_out_p_net(activation_derivative, out):
        return activation_derivative(out)

    @staticmethod
    def p_net_p_w(input_val):
        return input_val

    @staticmethod
    def p_net_p_prev(weight):
        return weight

    @staticmethod
    def p_net_p_b():
        return 1