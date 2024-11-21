# 柱状图
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import json


def converge_round_plot():
    # 折线图
    fig, ax = plt.subplots(figsize=(8, 6))

    # plt.figure(figsize=(8, 6))

    x = [0.2, 0.5, 0.8]  # 点的横坐标
    pure_pure = [28, 52, 169]  # 线1的纵坐标
    pure_mixed = [29, 65, 179]
    mixed_mixed = [35, 78, 195]
    # print(len(x))
    # print(len(FEL))
    # print(len(FedCS_5))
    # print(len(DSA_5))
    plt.plot(x, pure_pure, 's-', color='r', label="Case 1")  # s-:方形
    plt.plot(x, pure_mixed, 'o-', color='g', label="Case 2")  # o-:圆形
    plt.plot(x, mixed_mixed, '*-', color='b', label="Case 3")
    plt.xlabel("Discount rate", fontsize=30)  # 横坐标名字
    plt.ylabel("Convergent rounds", fontsize=30)  # 纵坐标名字
    # plt.xticks(label, label, fontsize=25)
    plt.xticks([0.2, 0.5, 0.8], fontsize=25)
    plt.yticks(fontsize=25)
    plt.legend(loc="best", fontsize=25)  # 图例
    # plt.title("$\mathregular{T^{wait}}$ = 5 min",fontsize = 15)
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%1.1f'))
    plt.tight_layout()

    # plt.show()
    fig.savefig("converge_round.pdf", format="pdf")


def converge_round_bar():
    # 柱状图
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.arange(3)  # 柱状图在横坐标上的位置
    # 列出你要显示的数据，数据的列表长度与x长度相同
    pure_pure = [28, 52, 169]  # 线1的纵坐标
    pure_mixed = [29, 65, 179]
    mixed_mixed = [35, 78, 195]

    gamma_0_2 = [28, 29, 35]
    gamma_0_5 = [52, 65, 78]
    gamma_0_8 = [169, 179, 195]

    bar_width = 0.3  # 设置柱状图的宽度
    # name_list = ["0.2", "0.5", "0.8"]
    name_list = ["Case 1", "Case 2", "Case 3"]

    # 绘制并列柱状图
    # plt.bar(x, pure_pure, bar_width, label='Case 1')
    # plt.bar(x + bar_width, pure_mixed, bar_width, label='Case 2')
    # plt.bar(x + 2 * bar_width, mixed_mixed, bar_width, label='Case 3')

    plt.bar(x, gamma_0_2, bar_width, label='$\gamma = 0.2$')
    plt.bar(x + bar_width, gamma_0_5, bar_width, label='$\gamma = 0.5$')
    plt.bar(x + 2 * bar_width, gamma_0_8, bar_width, label='$\gamma = 0.8$')

    plt.legend(loc="center left", fontsize=25)  # 图例
    plt.xlabel("Cases", fontsize=30)  # 横坐标名字
    plt.ylabel("Convergent rounds", fontsize=30)  # 纵坐标名字
    plt.xticks(x + bar_width, name_list, fontsize=25)  # 显示x坐标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
    plt.yticks(fontsize=25)
    plt.tight_layout()

    # plt.show()
    fig.savefig("converge_round_bar.pdf", format="pdf")


def p_trend(p1_line, p2_line, q1_line, q2_line, state):
    # 折线图
    fig, ax = plt.subplots(figsize=(8, 6))

    # plt.figure(figsize=(8, 6))

    x = [i for i in range(len(p1_line))]  # 点的横坐标

    if state == "S1":
        # s1是对的
        plt.plot(x, p1_line, 'o-', color='r', label="${p_{11}}$")  # s-:方形
        plt.plot(x, q2_line, 'o-', color='b', label="${q_{22}}$")  # o-:圆形
        plt.plot(x, p2_line, '*-', color='r', label="${p_{12}}$")
        plt.plot(x, q1_line, '*-', color='b', label="${q_{21}}$")
    if state == "S2":
        # s2是对的(正常）
        plt.plot(x, p1_line, 'o-', color='r', label="${p_{11}}$")  # s-:方形
        plt.plot(x, q1_line, 'o-', color='b', label="${q_{21}}$")
        plt.plot(x, p2_line, '*-', color='r', label="${p_{12}}$")
        plt.plot(x, q2_line, '*-', color='b', label="${q_{22}}$")  # o-:圆形
    plt.xlabel("Number of rounds", fontsize=30)  # 横坐标名字
    plt.ylabel("Probabilities", fontsize=30)  # 纵坐标名字
    # plt.xticks(label, label, fontsize=25)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.legend(loc="right", fontsize=25)  # 图例
    # plt.title("$\mathregular{T^{wait}}$ = 5 min",fontsize = 15)
    # plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%1.1f'))
    plt.tight_layout()

    # plt.show()
    fig.savefig("p_trend_{}.pdf".format(state), format="pdf")


# def q_trend(p1_line, p2_line, q1_line, q2_line, state):
# plan A 一开始时的那种画图 两两相加
# fig, ax = plt.subplots(figsize=(8, 6))
#
# # plt.figure(figsize=(8, 6))
#
# x = [i for i in range(len(p1_line))]  # 点的横坐标
# plt.plot(x, p1_line, 'o-', color='r', label="p1")  # s-:方形
# plt.plot(x, q1_line, 'o-', color='b', label="q1")
# plt.plot(x, p2_line, '*-', color='r', label="p2")  # o-:圆形
# plt.plot(x, q2_line, '*-', color='b', label="q2")
# plt.xlabel("Number of rounds", fontsize=30)  # 横坐标名字
# plt.ylabel("Q values", fontsize=30)  # 纵坐标名字
# # plt.xticks(label, label, fontsize=25)
# plt.xticks(fontsize=25)
# plt.yticks(fontsize=25)
# plt.legend(loc="best", fontsize=25)  # 图例
# # plt.title("$\mathregular{T^{wait}}$ = 5 min",fontsize = 15)
# # plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%1.1f'))
# plt.tight_layout()
#
# # plt.show()
# fig.savefig("q_trend_{}.pdf".format(state), format="pdf")


def q_trend(a11_a21_player1, a11_a22_player1, a12_a21_player1, a12_a22_player1, state, player):
    # plan B
    fig, ax = plt.subplots(figsize=(8, 6))
    # plt.figure(figsize=(8, 6))

    if state == "S1":
        state_formatted = "${s_1}$"
    if state == "S2":
        state_formatted = "${s_2}$"

    x = [i for i in range(len(p1_line))]  # 点的横坐标
    # plt.plot(x, a11_a21_player1, 'o-', color='r', label="Q(${a_11}$,{})".format(state))  # s-:方形 ,${a_{21}}$
    plt.plot(x, a11_a21_player1, 'o-', color='r', label="$Q({a_{11}},{a_{21}},$" + state_formatted + "$)$")  # s-:方形
    plt.plot(x, a11_a22_player1, 'o-', color='b', label="$Q({a_{11}},{a_{22}},$" + state_formatted + "$)$")
    plt.plot(x, a12_a21_player1, '*-', color='r', label="$Q({a_{12}},{a_{21}},$" + state_formatted + "$)$")  # o-:圆形
    plt.plot(x, a12_a22_player1, '*-', color='b', label="$Q({a_{12}},{a_{22}},$" + state_formatted + "$)$")
    plt.xlabel("Number of rounds", fontsize=30)  # 横坐标名字
    plt.ylabel("Q values", fontsize=30)  # 纵坐标名字
    # plt.xticks(label, label, fontsize=25)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.legend(loc="lower right", fontsize=25)  # 图例
    # plt.title("$\mathregular{T^{wait}}$ = 5 min",fontsize = 15)
    # plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%1.1f'))
    plt.tight_layout()

    # plt.show()
    fig.savefig("q_trend_{}_{}.pdf".format(state, player), format="pdf")


def v_trend(p1_line, q1_line, state):
    # 折线图
    fig, ax = plt.subplots(figsize=(8, 6))

    # plt.figure(figsize=(8, 6))

    x = [i for i in range(len(p1_line))]  # 点的横坐标
    plt.plot(x, p1_line, 'o-', color='r', label="${v_{1}}$")  # s-:方形
    plt.plot(x, q1_line, '*-', color='b', label="${v_{2}}$")
    plt.xlabel("Number of rounds", fontsize=30)  # 横坐标名字
    plt.ylabel("v values", fontsize=30)  # 纵坐标名字
    # plt.xticks(label, label, fontsize=25)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.legend(loc="best", fontsize=25)  # 图例
    # plt.title("$\mathregular{T^{wait}}$ = 5 min",fontsize = 15)
    # plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%1.1f'))
    plt.tight_layout()

    # plt.show()
    fig.savefig("v_trend_{}.pdf".format(state), format="pdf")


if __name__ == '__main__':
    converge_round_bar()
    input()
    with open('backup_pure_pure.json', 'r') as f:
        backup = json.load(f)

    state_list = ["S1", "S2"]

    possibility_history = backup["possibility_history"]
    q_matrix_history = backup["q_matrix_history"]
    v_matrix_history = backup["v_matrix_history"]

    # draw results
    for state in state_list:
        # possibility
        p1_line = []
        p2_line = []
        q1_line = []
        q2_line = []
        for i in possibility_history:
            p1_line.append(i[state]["p1"])
            p2_line.append(i[state]["p2"])
            q1_line.append(i[state]["q1"])
            q2_line.append(i[state]["q2"])
        p_trend(p1_line, p2_line, q1_line, q2_line, state)

        # V matrix
        p1_line = []
        p2_line = []
        q1_line = []
        q2_line = []
        for i in v_matrix_history:
            p1_line.append(i[state][0])
            q1_line.append(i[state][1])
        v_trend(p1_line, q1_line, state)

    for state in state_list:
        # Q matrix
        a11_a21_player1 = []
        a11_a21_player2 = []
        a11_a22_player1 = []
        a11_a22_player2 = []

        a12_a21_player1 = []
        a12_a21_player2 = []
        a12_a22_player1 = []
        a12_a22_player2 = []
        for i in q_matrix_history:
            a11_a21_player1.append(i[state][0][0][0])
            a11_a21_player2.append(i[state][0][0][1])
            a11_a22_player1.append(i[state][0][1][0])
            a11_a22_player2.append(i[state][0][1][1])

            a12_a21_player1.append(i[state][1][0][0])
            a12_a21_player2.append(i[state][1][0][1])
            a12_a22_player1.append(i[state][1][1][0])
            a12_a22_player2.append(i[state][1][1][1])

        q_trend(a11_a21_player1, a11_a22_player1, a12_a21_player1, a12_a22_player1, state, 'player1')
        q_trend(a11_a21_player2, a11_a22_player2, a12_a21_player2, a12_a22_player2, state, 'player2')
