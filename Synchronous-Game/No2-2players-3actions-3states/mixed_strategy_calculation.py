import policy

from sympy import *


#       L     R      C

#   T   00    01     02       p1

#   B   10    11     12       p2

#   F   20    21     22       1-p1 -p2

#       q1    q2    1-q1-q2

def get_mixed_strategy_equilibrium(Q_matrix):
    ans_p = calculate_p(Q_matrix)
    if "p1" in ans_p.keys():
        p1 = ans_p["p1"]
        p2 = ans_p["p2"]
    else:
        p1 = Symbol('p1')
        p2 = Symbol('p2')
        p1 = ans_p[p1]
        p2 = ans_p[p2]
    p3 = 1 - p1 - p2
    ans_q = calculate_q(Q_matrix)
    if "q1" in ans_q.keys():
        q1 = ans_q["q1"]
        q2 = ans_q["q2"]
    else:
        q1 = Symbol('q1')
        q2 = Symbol('q2')
        q1 = ans_q[q1]
        q2 = ans_q[q2]
    q3 = 1 - q1 - q2
    return float(p1), float(p2), float(p3), float(q1), float(q2), float(q3)


def calculate_p(Q_matrix):
    # 1. calculate p1 p2 p3
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve([(Q_matrix[0][0][1] * p1 + Q_matrix[1][0][1] * p2 + Q_matrix[2][0][1] * (1 - p1 - p2)) - (
                Q_matrix[0][1][1] * p1 + Q_matrix[1][1][1] * p2 + Q_matrix[2][1][1] * (1 - p1 - p2)),
                       (Q_matrix[0][0][1] * p1 + Q_matrix[1][0][1] * p2 + Q_matrix[2][0][1] * (1 - p1 - p2)) - (
                               Q_matrix[0][2][1] * p1 + Q_matrix[1][2][1] * p2 + Q_matrix[2][2][1] * (1 - p1 - p2))],
                      [p1, p2])
        p1 = ans_p[p1]
        p2 = ans_p[p2]
        if p1 >= 0 and p2 >= 0 and p1 + p2 <= 1:
            return ans_p
    except Exception:
        pass

    # set p1 = 0 and equation 1-2, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve([(Q_matrix[0][0][1] * 0 + Q_matrix[1][0][1] * p2 + Q_matrix[2][0][1] * (1 - 0 - p2)) - (
                Q_matrix[0][1][1] * 0 + Q_matrix[1][1][1] * p2 + Q_matrix[2][1][1] * (1 - 0 - p2))], [p2])
        p2_value = ans_p[0]
        if 0 <= p2_value <= 1:
            return {"p1": 1 - p2_value, "p2": p2_value}
    except Exception:
        pass

    # set p2 = 0 and equation 1-2, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve((Q_matrix[0][0][1] * p1 + Q_matrix[1][0][1] * 0 + Q_matrix[2][0][1] * (1 - p1 - 0)) - (
                Q_matrix[0][1][1] * p1 + Q_matrix[1][1][1] * 0 + Q_matrix[2][1][1] * (1 - p1 - 0)), p1)
        p1_value = ans_p[0]
        if 0 <= p1_value <= 1:
            return {"p1": p1_value, "p2": 1 - p1_value}
    except Exception:
        pass

    # set p3 = 0 and equation 1-2, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve((Q_matrix[0][0][1] * p1 + Q_matrix[1][0][1] * (1 - p1 - 0) + Q_matrix[2][0][1] * 0) - (
                Q_matrix[0][1][1] * p1 + Q_matrix[1][1][1] * (1 - p1 - 0) + Q_matrix[2][1][1] * 0), p1)
        p1_value = ans_p[0]
        if 0 <= p1_value <= 1:
            return {"p1": p1_value, "p2": 1 - p1_value}
    except Exception:
        pass

    # set p1 = 0 and equation 1-3, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve([(Q_matrix[0][0][1] * 0 + Q_matrix[1][0][1] * p2 + Q_matrix[2][0][1] * (1 - 0 - p2)) - (
                Q_matrix[0][2][1] * 0 + Q_matrix[1][2][1] * p2 + Q_matrix[2][2][1] * (1 - 0 - p2))], [p2])
        p2_value = ans_p[0]
        if 0 <= p2_value <= 1:
            return {"p1": 1 - p2_value, "p2": p2_value}
    except Exception:
        pass

    # set p2 = 0 and equation 1-3, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve((Q_matrix[0][0][1] * p1 + Q_matrix[1][0][1] * 0 + Q_matrix[2][0][1] * (1 - p1 - 0)) - (
                Q_matrix[0][2][1] * p1 + Q_matrix[1][2][1] * 0 + Q_matrix[2][2][1] * (1 - p1 - 0)), p1)
        p1_value = ans_p[0]
        if 0 <= p1_value <= 1:
            return {"p1": p1_value, "p2": 1 - p1_value}
    except Exception:
        pass

    # set p3 = 0 and equation 1-3, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve((Q_matrix[0][0][1] * p1 + Q_matrix[1][0][1] * (1 - p1 - 0) + Q_matrix[2][0][1] * 0) - (
                Q_matrix[0][2][1] * p1 + Q_matrix[1][2][1] * (1 - p1 - 0) + Q_matrix[2][2][1] * 0), p1)
        p1_value = ans_p[0]
        if 0 <= p1_value <= 1:
            return {"p1": p1_value, "p2": 1 - p1_value}
    except Exception:
        pass

    # set p1 = 0 and equation 2-3, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve([(Q_matrix[0][1][1] * 0 + Q_matrix[1][1][1] * p2 + Q_matrix[2][1][1] * (1 - 0 - p2)) - (
                Q_matrix[0][2][1] * 0 + Q_matrix[1][2][1] * p2 + Q_matrix[2][2][1] * (1 - 0 - p2))], [p2])
        p2_value = ans_p[0]
        if 0 <= p2_value <= 1:
            return {"p1": 1 - p2_value, "p2": p2_value}
    except Exception:
        pass

    # set p2 = 0 and equation 2-3, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve((Q_matrix[0][1][1] * p1 + Q_matrix[1][1][1] * 0 + Q_matrix[2][1][1] * (1 - p1 - 0)) - (
                Q_matrix[0][2][1] * p1 + Q_matrix[1][2][1] * 0 + Q_matrix[2][2][1] * (1 - p1 - 0)), p1)
        p1_value = ans_p[0]
        if 0 <= p1_value <= 1:
            return {"p1": p1_value, "p2": 1 - p1_value}
    except Exception:
        pass

    # set p3 = 0 and equation 2-3, try to get all positive value
    p1 = Symbol('p1')
    p2 = Symbol('p2')
    try:
        ans_p = solve((Q_matrix[0][1][1] * p1 + Q_matrix[1][1][1] * (1 - p1 - 0) + Q_matrix[2][1][1] * 0) - (
                Q_matrix[0][2][1] * p1 + Q_matrix[1][2][1] * (1 - p1 - 0) + Q_matrix[2][2][1] * 0), p1)
        p1_value = ans_p[0]
        if 0 <= p1_value <= 1:
            return {"p1": p1_value, "p2": 1 - p1_value}
    except Exception:
        # all cases cannot meet all-positive requirement
        print(Q_matrix)
        print(ans_p)
        print("all cases cannot meet all-positive requirement for p")
        raise


def calculate_q(Q_matrix):
    # 2. calculate q1 q2 q3
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve([(Q_matrix[0][0][0] * q1 + Q_matrix[1][0][0] * q2 + Q_matrix[2][0][0] * (1 - q1 - q2)) - (
                Q_matrix[0][1][0] * q1 + Q_matrix[1][1][0] * q2 + Q_matrix[2][1][0] * (1 - q1 - q2)),
                       (Q_matrix[0][0][0] * q1 + Q_matrix[1][0][0] * q2 + Q_matrix[2][0][0] * (1 - q1 - q2)) - (
                               Q_matrix[0][2][0] * q1 + Q_matrix[1][2][0] * q2 + Q_matrix[2][2][0] * (1 - q1 - q2))],
                      [q1, q2])
        q1 = ans_p[q1]
        q2 = ans_p[q2]
        if q1 >= 0 and q2 >= 0 and q1 + q2 <= 1:
            return ans_p
    except Exception:
        pass

    # set q1 = 0 and equation 1-2, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve([(Q_matrix[0][0][0] * 0 + Q_matrix[1][0][0] * q2 + Q_matrix[2][0][0] * (1 - 0 - q2)) - (
                Q_matrix[0][1][0] * 0 + Q_matrix[1][1][0] * q2 + Q_matrix[2][1][0] * (1 - 0 - q2))], [q2])
        q2_value = ans_p[0]
        if 0 <= q2_value <= 1:
            return {"q1": 1 - q2_value, "q2": q2_value}
    except Exception:
        pass

    # set q2 = 0 and equation 1-2, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve((Q_matrix[0][0][0] * q1 + Q_matrix[1][0][0] * 0 + Q_matrix[2][0][0] * (1 - q1 - 0)) - (
                Q_matrix[0][1][0] * q1 + Q_matrix[1][1][0] * 0 + Q_matrix[2][1][0] * (1 - q1 - 0)), q1)
        q1_value = ans_p[0]
        if 0 <= q1_value <= 1:
            return {"q1": q1_value, "q2": 1 - q1_value}
    except Exception:
        pass

    # set q3 = 0 and equation 1-2, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve((Q_matrix[0][0][0] * q1 + Q_matrix[1][0][0] * (1 - q1 - 0) + Q_matrix[2][0][0] * 0) - (
                Q_matrix[0][1][0] * q1 + Q_matrix[1][1][0] * (1 - q1 - 0) + Q_matrix[2][1][0] * 0), q1)
        q1_value = ans_p[0]
        if 0 <= q1_value <= 1:
            return {"q1": q1_value, "q2": 1 - q1_value}
    except Exception:
        pass

    # set q1 = 0 and equation 1-3, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve([(Q_matrix[0][0][0] * 0 + Q_matrix[1][0][0] * q2 + Q_matrix[2][0][0] * (1 - 0 - q2)) - (
                Q_matrix[0][2][0] * 0 + Q_matrix[1][2][0] * q2 + Q_matrix[2][2][0] * (1 - 0 - q2))], [q2])
        q2_value = ans_p[0]
        if 0 <= q2_value <= 1:
            return {"q1": 1 - q2_value, "q2": q2_value}
    except Exception:
        pass

    # set q2 = 0 and equation 1-3, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve((Q_matrix[0][0][0] * q1 + Q_matrix[1][0][0] * 0 + Q_matrix[2][0][0] * (1 - q1 - 0)) - (
                Q_matrix[0][2][0] * q1 + Q_matrix[1][2][0] * 0 + Q_matrix[2][2][0] * (1 - q1 - 0)), q1)
        q1_value = ans_p[0]
        if 0 <= q1_value <= 1:
            return {"q1": q1_value, "q2": 1 - q1_value}
    except Exception:
        pass

    # set q3 = 0 and equation 1-3, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve((Q_matrix[0][0][0] * q1 + Q_matrix[1][0][0] * (1 - q1 - 0) + Q_matrix[2][0][0] * 0) - (
                Q_matrix[0][1][0] * q1 + Q_matrix[1][1][0] * (1 - q1 - 0) + Q_matrix[2][1][0] * 0), q1)
        q1_value = ans_p[0]
        if 0 <= q1_value <= 1:
            return {"q1": q1_value, "q2": 1 - q1_value}
    except Exception:
        pass

    # set q1 = 0 and equation 2-3, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve([(Q_matrix[0][1][0] * 0 + Q_matrix[1][1][0] * q2 + Q_matrix[2][1][0] * (1 - 0 - q2)) - (
                Q_matrix[0][2][0] * 0 + Q_matrix[1][2][0] * q2 + Q_matrix[2][2][0] * (1 - 0 - q2))], [q2])
        q2_value = ans_p[0]
        if 0 <= q2_value <= 1:
            return {"q1": 1 - q2_value, "q2": q2_value}
    except Exception:
        pass

    # set q2 = 0 and equation 2-3, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve((Q_matrix[0][1][0] * q1 + Q_matrix[1][1][0] * 0 + Q_matrix[2][1][0] * (1 - q1 - 0)) - (
                Q_matrix[0][2][0] * q1 + Q_matrix[1][2][0] * 0 + Q_matrix[2][2][0] * (1 - q1 - 0)), q1)
        q1_value = ans_p[0]
        if 0 <= q1_value <= 1:
            return {"q1": q1_value, "q2": 1 - q1_value}
    except Exception:
        pass

    # set q3 = 0 and equation 2-3, try to get all positive value
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    try:
        ans_p = solve((Q_matrix[0][1][0] * q1 + Q_matrix[1][1][0] * (1 - q1 - 0) + Q_matrix[2][1][0] * 0) - (
                Q_matrix[0][2][0] * q1 + Q_matrix[1][2][0] * (1 - q1 - 0) + Q_matrix[2][2][0] * 0), q1)
        q1_value = ans_p[0]
        if 0 <= q1_value <= 1:
            return {"q1": q1_value, "q2": 1 - q1_value}
    except Exception:
        # all cases cannot meet all-positive requirement
        print(Q_matrix)
        print("All cases cannot meet all-positive requirement for q")
        raise


if __name__ == '__main__':
    sample_matrix = {}
    # a sample matrix of mixed strategy
    sample_matrix["S1"] = [
        [[20.0, -20.0], [15.0, -15.0], [15.0, -15.0]],
        [[5.0, -15.0], [62.58297, -61.46681], [62.58297, -61.46681]],
        [[5.0, -15.0], [62.58297, -61.46681], [62.58297, -61.46681]]
    ]
    # print("Example matrix of sample matrix:")
    p1, p2, p3, q1, q2, q3 = get_mixed_strategy_equilibrium(sample_matrix["S1"])
    print(p1, p2, p3, q1, q2, q3)
    # print("Example matrix of main func:")
    # p, q  = get_equilibrium("S1", R_matrix.get_R_matrix())
    # print(p, q)
    # v1, v2, p1, p2, p3, q1, q2, q3 = calculate_v(sample_matrix["S1"])
    # print(v1, v2, p1, p2, p3, q1, q2, q3)
