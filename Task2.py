import random

c_avg = [7, 4, 10, 5]
c_dev = [3, 10, 6, 2]


def exploreOnly() -> float:
    c1_hap = 0
    c2_hap = 0
    c3_hap = 0
    c4_hap = 0
    # getting sum of happiness for C1
    for i in range(50):
        a = random.normalvariate(c_avg[0], c_dev[0])
        c1_hap += a
    # getting sum of happiness for C2
    for i in range(50):
        a = random.normalvariate(c_avg[1], c_dev[1])
        c2_hap += a
    # getting sum of happiness for C3
    for i in range(50):
        a = random.normalvariate(c_avg[2], c_dev[2])
        c3_hap += a
    # getting sum of happiness for C4
    for i in range(50):
        a = random.normalvariate(c_avg[3], c_dev[3])
        c4_hap += a
    # formats the code and turns the string into float
    return float(format(c1_hap + c2_hap + c3_hap + c4_hap, ".2f"))
