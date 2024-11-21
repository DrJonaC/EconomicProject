import policy


#       L     R      

#   T   00    01      p

#   B   10    11      1-p

#       q     1-q 


def get_mixed_strategy_equilibrium(Q_matrix):
    equ_player2 = "{} * p + {} * (1 - p) = {} * p + {} * (1 - p)".format(Q_matrix[0][0][1], Q_matrix[1][0][1],
                                                                         Q_matrix[0][1][1], Q_matrix[1][1][1])
    # print("{} * p + {} * (1 - p) = {} * p + {} * (1 - p)".format(Q_matrix[0][0][1], Q_matrix[1][0][1], Q_matrix[0][1][1], Q_matrix[1][1][1]))
    p = solve(equ_player2, var="p")
    equ_player1 = "{} * q + {} * (1 - q) = {} * q + {} * (1 - q)".format(Q_matrix[0][0][0], Q_matrix[0][1][0],
                                                                         Q_matrix[1][0][0], Q_matrix[1][1][0])
    # print("{} * q + {} * (1 - q) = {} * q + {} * (1 - q)".format(Q_matrix[0][0][0], Q_matrix[0][1][0], Q_matrix[1][0][0], Q_matrix[1][1][0]))
    q = solve(equ_player1, var="q")
    # print("mixed_strategy:\tp = {}, q = {}".format(p, q))

    return p, 1 - p, q, 1 - q


def solve(equation, var='X'):
    equation = equation.replace("=", "-(") + ")"
    result = eval(equation, {var: 1j})
    return -result.real / result.imag


# def calculate_v(Q_matrix):
#     p, q = get_equilibrium(Q_matrix)
#     # v1 is the expected payoff of player1
#     v1 = Q_matrix[0][0][0] * p * q + Q_matrix[1][0][0] * (1 - p) * q + Q_matrix[0][1][0] * p * (1 - q) + Q_matrix[1][1][0] * (1 - p) * (1 - q)
#     # v2 is the expected payoff of player2
#     v2 = Q_matrix[0][0][1] * p * q + Q_matrix[1][0][1] * (1 - p) * q + Q_matrix[0][1][1] * p * (1 - q) + Q_matrix[1][1][1] * (1 - p) * (1 - q)
#     return v1, v2, p, q

# def get_equilibrium(Q_matrix):
#     p = -1
#     q = -1
#     # check if pure strategy
#     if Q_matrix[0][0][0] >= Q_matrix[1][0][0] and Q_matrix[0][1][0] >= Q_matrix[1][1][0]:
#         p = 1
#     if Q_matrix[0][0][0] <= Q_matrix[1][0][0] and Q_matrix[0][1][0] <= Q_matrix[1][1][0]:
#         p = 0
#     if Q_matrix[0][0][0] == Q_matrix[1][0][0] and Q_matrix[0][1][0] == Q_matrix[1][1][0]:
#         p = 0.5
#     if Q_matrix[0][0][1] >= Q_matrix[0][1][1] and Q_matrix[1][0][1] >= Q_matrix[1][1][1]:
#         q = 1
#     if Q_matrix[0][0][1] <= Q_matrix[0][1][1] and Q_matrix[1][0][1] <= Q_matrix[1][1][1]:
#         q = 0
#     if Q_matrix[0][0][1] == Q_matrix[0][1][1] and Q_matrix[1][0][1] == Q_matrix[1][1][1]:
#         q = 0.5
#     if p != -1 and q != -1:
#         # print("pure strategy:\tdefault\tp = {}, q = {}".format(p, q))
#         return p, q
#     if p == -1 and q == -1:
#         # print("mixed strategy")
#         return get_mixed_strategy_equilibrium(Q_matrix)
#     if (p == -1 and q == 0.5) or (p == 0.5 and q == -1):
#         # print("pure strategy\t2")
#         return 0.5, 0.5
#     if p == -1 and q == 1: # player2 -> L
#         p = 1 if Q_matrix[0][0][0] > Q_matrix[1][0][0] else 0
#         # print("pure strategy:\tplayer2 -> L\tp = {}, q = {}".format(p, q))
#         return p, q
#     if p == -1 and q == 0: # player2 -> R
#         p = 1 if Q_matrix[0][1][0] > Q_matrix[1][1][0] else 0
#         # print("pure strategy:\tplayer2 -> R\tp = {}, q = {}".format(p, q))
#         return p, q
#     if p == 1 and q == -1: # player1 -> T
#         q = 1 if Q_matrix[0][0][1] > Q_matrix[0][1][1] else 0
#         # print("pure strategy:\tplayer1 -> T\tp = {}, q = {}".format(p, q))
#         return p, q
#     if p == 0 and q == -1: # player1 -> B
#         q = 1 if Q_matrix[1][0][1] > Q_matrix[1][1][1] else 0
#         # print("pure strategy:\tplayer1 -> B\tp = {}, q = {}".format(p, q))
#         return p, q
#     raise "false:\tp = {}, q = {}".format(p, q)


if __name__ == '__main__':
    sample_matrix = {}
    # a sample matrix of mixed strategy
    sample_matrix["S1"] = [
        [[1, 2], [0, 4]],
        [[0, 5], [3, 2]]
    ]
    # print("Example matrix of sample matrix:")
    # p, q = get_equilibrium("S1", draft_matrix)
    # print(p, q)
    # print("Example matrix of main func:")
    # p, q  = get_equilibrium("S1", R_matrix.get_R_matrix())
    # print(p, q)
