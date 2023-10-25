import random

c_avg=[7,4,10,5]
c_dev=[3,10,6,2]
e =10

def exploitOnly():
    e = 10
    return e

def exploreOnly():
    e = 10
    return e


def eGreedy(e) -> float:
    LC1 = []
    LC2 = []
    LC3 = []
    LC4 = []

    VC1 = random.normalvariate(c_avg[0],c_dev[0])
    LC1.append(VC1)
    AC1 = sum(LC1)/len(LC1)

    VC2 = random.normalvariate(c_avg[1],c_dev[1])
    LC2.append(VC2)
    AC2 = sum(LC2) / len(LC2)

    VC3 = random.normalvariate(c_avg[2],c_dev[2])
    LC3.append(VC3)
    AC3 = sum(LC3) / len(LC3)

    VC4 = random.normalvariate(c_avg[3],c_dev[3])
    LC4.append(VC4)
    AC4 = sum(LC4) / len(LC4)

    current_highest_average = max(AC1,AC2,AC3,AC4)
    LA = [AC1,AC2,AC3,AC4]

    for i in range(196):
        r = random.random()
        if r < e/100:
            i = random.randint(1,4)
            if i == 1:
                VC1 = random.normalvariate(c_avg[0],c_dev[0])
                LC1.append(VC1)
                AC1 = sum(LC1) / len(LC1)
            elif i == 2:
                VC2 = random.normalvariate(c_avg[1],c_dev[1])
                LC2.append(VC2)
                AC2 = sum(LC2)/len(LC2)
            elif i == 3:
                VC3 = random.normalvariate(c_avg[2],c_dev[2])
                LC3.append(VC3)
                AC3 = sum(LC3)/len(LC3)
            else:
                VC4 = random.normalvariate(c_avg[3],c_dev[3])
                LC4.append(VC4)
                AC4 = sum(LC4)/len(LC4)
            current_highest_average = max(AC1, AC2, AC3, AC4)
            LA = [AC1, AC2, AC3, AC4]

        else:
            i = LA.index(max(LA))
            if i == 0:
                VC1 = random.normalvariate(c_avg[0],c_dev[0])
                LC1.append(VC1)
                AC1 = sum(LC1) / len(LC1)
            elif i == 1:
                VC2 = random.normalvariate(c_avg[1],c_dev[1])
                LC2.append(VC2)
                AC2 = sum(LC2) / len(LC2)
            elif i == 2:
                VC3 = random.normalvariate(c_avg[2],c_dev[2])
                LC3.append(VC3)
                AC3 = sum(LC3) / len(LC3)
            else:
                VC4 = random.normalvariate(c_avg[3],c_dev[3])
                LC4.append(VC4)
                AC4 = sum(LC4) / len(LC4)
            current_highest_average = max(AC1, AC2, AC3, AC4)
            LA = [AC1, AC2, AC3, AC4]

        current_highest_average = max(AC1, AC2, AC3, AC4)
        total_happiness = sum(LC1) + sum(LC2) + sum(LC3) + sum(LC4)
        return total_happiness
