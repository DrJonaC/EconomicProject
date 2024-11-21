# four example
pure_1 = [
    [[5, 0], [1, 1]],
    [[2, 2], [6, 5]]
]

pure_2 = [
    [[2, 3], [5, 4]],
    [[3, 1], [1, 3]]
]

pure_3 = [
    [[5, 0], [1, 1]],
    [[2, 2], [10, 5]]
]

mixed_1 = [
    [[6, 2], [4, 7]],
    [[1, 4], [5, 3]]
]

mixed_2 = [
    [[1, 2], [0, 4]],
    [[0, 5], [3, 2]]
]

mixed_3 = [
    [[1, 2], [0, 4]],
    [[0, 5], [3, 2]]
]


def get_R_matrix():
    # R["S1"][0][1][0]   means  P["to state S1"][action of player1][action of player2][reward of player1]
    R = {
        "S1": mixed_1,
        "S2": mixed_2
    }

    return R


def get_P_matrix():
    # P["S1"][0][1]["S2"]   means    P["from state S1"][action of player1][action of player2][to state "S2"]
    P = {
        "S1": [
            [{"S1": 0.4, "S2": 0.6}, {"S1": 0.3, "S2": 0.7}],
            [{"S1": 0.5, "S2": 0.5}, {"S1": 0.8, "S2": 0.2}]
        ],
        "S2": [
            [{"S1": 0.7, "S2": 0.3}, {"S1": 0.4, "S2": 0.6}],
            [{"S1": 0.4, "S2": 0.6}, {"S1": 0.5, "S2": 0.5}]
        ]
    }
    return P


def get_init_possibility():
    possibility = {
        "S1": {"p1": 0.5, "p2": 0.5, "q1": 0.5, "q2": 0.5},
        "S2": {"p1": 0.5, "p2": 0.5, "q1": 0.5, "q2": 0.5}
    }
    return possibility


def get_v_matrix():
    v_matrix = {
        "S1": [],
        "S2": [],
    }
    return v_matrix


if __name__ == '__main__':
    R = get_R_matrix()
    print("R['S2']: ", R["S2"])
    print("mixed_3: ", mixed_3)
    print('R["S2"] == mixed_3', R["S2"] == mixed_3)
