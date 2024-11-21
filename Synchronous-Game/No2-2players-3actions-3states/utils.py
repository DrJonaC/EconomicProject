import random


def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    rand_num = random.random()

    for index, scope in enumerate(rate):
        start += scope
        if rand_num <= start:
            break
    return index
