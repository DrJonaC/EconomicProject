import policy
import nash_equilibrium_calculation
import mixed_strategy_calculation
import utils
import random
import sys
import copy
from sympy import *
import json

gamma = 0.5
r_matrix = policy.get_R_matrix()
q_matrix = copy.deepcopy(r_matrix)  # set q0 to reward matrix for initialization
p_matrix = policy.get_P_matrix()
v_matrix = policy.get_v_matrix()
possibility = policy.get_init_possibility()
payoff_type = {}
state_list = ["S1", "S2", "S3"]

# save history to show trend
possibility_history = [copy.deepcopy(possibility)]
q_matrix_history = [copy.deepcopy(q_matrix)]
v_matrix_history = []

# init v_matrix
for state in state_list:
    pure_payoff = nash_equilibrium_calculation.is_pure_strategy_equilibrium(q_matrix[state])

    if pure_payoff == []:
        # mixed strategy:
        payoff_type[state] = "mixed"
        p1, p2, p3, q1, q2, q3 = mixed_strategy_calculation.get_mixed_strategy_equilibrium(q_matrix[state])
    else:
        # pure strategy:
        payoff_type[state] = "pure"
        row, column = pure_payoff
        if row == 0:
            p1, p2, p3 = 1, 0, 0
        if row == 1:
            p1, p2, p3 = 0, 1, 0
        if row == 2:
            p1, p2, p3 = 0, 0, 1
        if column == 0:
            q1, q2, q3 = 1, 0, 0
        if column == 1:
            q1, q2, q3 = 0, 1, 0
        if column == 2:
            q1, q2, q3 = 0, 0, 1

    # calculate expected payoff v1 of player1 and v2 of player2
    v_matrix[state] = nash_equilibrium_calculation.calculate_v(p1, p2, p3, q1, q2, q3, q_matrix[state])

v_matrix_history.append(copy.deepcopy(v_matrix))

# count to check if convergence
count_if_convergence = 0


# the main training loop
for episode in range(1001):
    # randomly select a state
    state = state_list[random.randint(0, len(state_list) - 1)]

    # print(state, q_matrix[state])
    pure_payoff = nash_equilibrium_calculation.is_pure_strategy_equilibrium(q_matrix[state])

    if pure_payoff == []:
        # mixed strategy:
        payoff_type[state] = "mixed"
        p1, p2, p3, q1, q2, q3 = mixed_strategy_calculation.get_mixed_strategy_equilibrium(q_matrix[state])
    else:
        # pure strategy:
        payoff_type[state] = "pure"
        row, column = pure_payoff
        if row == 0:
            p1, p2, p3 = 1, 0, 0
        if row == 1:
            p1, p2, p3 = 0, 1, 0
        if row == 2:
            p1, p2, p3 = 0, 0, 1
        if column == 0:
            q1, q2, q3 = 1, 0, 0
        if column == 1:
            q1, q2, q3 = 0, 1, 0
        if column == 2:
            q1, q2, q3 = 0, 0, 1

    # calculate expected payoff v1 of player1 and v2 of player2
    v_matrix[state] = nash_equilibrium_calculation.calculate_v(p1, p2, p3, q1, q2, q3, q_matrix[state])

    # update equilibrium possibility history
    possibility[state]["p1"] = round(p1, 5)
    possibility[state]["p2"] = round(p2, 5)
    possibility[state]["p3"] = round(p3, 5)
    possibility[state]["q1"] = round(q1, 5)
    possibility[state]["q2"] = round(q2, 5)
    possibility[state]["q3"] = round(q3, 5)
    possibility_history.append(copy.deepcopy(possibility))

    # update v_matrix_history
    v_matrix_history.append(copy.deepcopy(v_matrix))

    # update q matrix
    for action1 in range(len(r_matrix["S1"])):
        for action2 in range(len(r_matrix["S1"][0])):
            for player in range(len(v_matrix["S1"])):
                previous_estimation = v_matrix["S1"][player] * p_matrix[state][action1][action2]["S1"] + v_matrix["S2"][
                    player] * p_matrix[state][action1][action2]["S2"] + v_matrix["S3"][player] * \
                                      p_matrix[state][action1][action2]["S3"]
                q_matrix[state][action1][action2][player] = round(
                    r_matrix[state][action1][action2][player] + gamma * previous_estimation, 5)

    q_matrix_history.append(copy.deepcopy(q_matrix))

    # check if convergence
    if v_matrix == v_matrix_history[-2]:  # same as the one before the latest one
        count_if_convergence += 1
    else:
        count_if_convergence = 0

    # choose the next state
    # rate = [p_matrix[state][action1][action2]["S1"], p_matrix[state][action1][action2]["S2"],
    #         p_matrix[state][action1][action2]["S3"]]
    # state = state_list[utils.random_index(rate)]

    # Display training progress
    if episode % 20 == 0:
        print("\nTraining episode: %d" % episode)
        print("Q matrix:\t", q_matrix)
        print("V_matrix:\t", v_matrix)
        print("Possibility:\t", possibility)
        print("Payoff type:\t", payoff_type)
        print("------------------------------------------------------------------------------------------------")

    if count_if_convergence == 10:
        print("\n================================================================================================")
        print("The V_matrix is converged at round:\t", episode - 10)
        # for item in q_matrix_history:
        #     print(item)
        break

print("Payoff type:\t", payoff_type)
if count_if_convergence < 10:
    raise ("Error: Q matrix didn't converge.")

# save
backup = {}
backup["possibility_history"] = possibility_history
backup["q_matrix_history"] = q_matrix_history
backup["v_matrix_history"] = v_matrix_history

jsObj = json.dumps(backup)

fileObject = open('backup_{}_{}.json'.format(gamma, "test"), 'w')
fileObject.write(jsObj)
fileObject.close()
