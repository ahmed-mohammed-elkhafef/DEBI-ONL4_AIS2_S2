from chain_rule import ChainRule

class Gradients:

    @staticmethod
    def output_weight(pE, pO, input_val):
        return pE * pO * ChainRule.p_net_p_w(input_val)

    @staticmethod
    def hidden_error(pE_list, pO_list, weights):
        total = 0
        for i in range(len(pE_list)):
            total += pE_list[i] * pO_list[i] * ChainRule.p_net_p_prev(weights[i])
        return total

    @staticmethod
    def hidden_weight(pE, pO, input_val):
        return pE * pO * ChainRule.p_net_p_w(input_val)

    @staticmethod
    def bias(pE, pO):
        return pE * pO * ChainRule.p_net_p_b()