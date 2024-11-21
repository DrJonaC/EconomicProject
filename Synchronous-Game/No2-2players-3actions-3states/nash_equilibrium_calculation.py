import policy
import random

from sympy import *


#       L     R      C

#   T   00    01     02       p1

#   B   10    11     12       p2

#   F   20    21     22       1-p1 -p2

#       q1    q2    1-q1-q2

def is_pure_strategy_equilibrium(Q_matrix):
    count = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    equilibrium_list = []  # check if it is pure
    # player 1
    for colomn in range(len(Q_matrix[0])):
        colomn_list = []
        for row in range(len(Q_matrix)):
            colomn_list.append(Q_matrix[row][colomn][0])
        max_value = max(colomn_list)
        for row in range(len(Q_matrix)):
            if Q_matrix[row][colomn][0] == max_value:
                count[row][colomn] += 1
    # player 2
    for row in range(len(Q_matrix)):
        row_list = []
        for colomn in range(len(Q_matrix[0])):
            row_list.append(Q_matrix[row][colomn][1])
        max_value = max(row_list)
        for colomn in range(len(Q_matrix[0])):
            if Q_matrix[row][colomn][1] == max_value:
                count[row][colomn] += 1
                if count[row][colomn] == 2:  # means both two player can get equilibrium here
                    equilibrium_list.append([row, colomn])

    if equilibrium_list == []:
        # mixed strategy
        return []

    # else: randomly choose a equilibrium payoff to calculate v
    random_pure = random.randint(0, len(equilibrium_list) - 1)
    # print("random_pure", random_pure, equilibrium_list)
    return equilibrium_list[random_pure]


def calculate_v(p1, p2, p3, q1, q2, q3, Q_matrix):
    # v1 is the expected payoff of player1
    v1 = Q_matrix[0][0][0] * p1 * q1 + Q_matrix[1][0][0] * p2 * q1 + Q_matrix[2][0][0] * p3 * q1 + Q_matrix[0][1][
        0] * p1 * q2 + Q_matrix[1][1][0] * p2 * q2 + Q_matrix[2][1][0] * p3 * q2 + Q_matrix[0][2][0] * p1 * q3 + \
         Q_matrix[1][2][0] * p2 * q3 + Q_matrix[2][2][0] * p3 * q3
    # v2 is the expected payoff of player2
    v2 = Q_matrix[0][0][1] * p1 * q1 + Q_matrix[1][0][1] * p2 * q1 + Q_matrix[2][0][1] * p3 * q1 + Q_matrix[0][1][
        1] * p1 * q2 + Q_matrix[1][1][1] * p2 * q2 + Q_matrix[2][1][1] * p3 * q2 + Q_matrix[0][2][1] * p1 * q3 + \
         Q_matrix[1][2][1] * p2 * q3 + Q_matrix[2][2][1] * p3 * q3
    return [round(v1, 3), round(v2, 3)]  # the number of list is equal to the number of players


if __name__ == '__main__':
    sample_matrix = {}
    # a sample matrix of mixed strategy
    sample_matrix["S1"] = [
        [[3, 1], [4, 3], [5, 4]],
        [[4, 2], [3, 4], [2, 2]],
        [[2, 3], [4, 5], [3, 3]]
    ]
    # print("Example matrix of sample matrix:")
    pure_payoff = is_pure_strategy_equilibrium(sample_matrix["S1"])
    print(pure_payoff)
