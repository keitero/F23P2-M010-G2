import random

c_avg = [7, 4, 10, 5]
c_dev = [3, 10, 6, 2]


def simulation(t: int, e=10) -> None:
    # creation of all the local variables used in the function
    days = 200

    # storage of simulated values
    exploit_vals = []
    explore_vals = []
    greed_vals = []

    # optimum happiness calculation
    opt_hap = max(c_avg) * days

    # expected values
    # sorting the list from highest to lowest value
    l1 = sorted(c_avg, reverse=True)
    exploit_exp = 197 * l1[0] + l1[1] + l1[2] + l1[3]
    explore_exp = c_avg[0] * (days/4) + c_avg[1] * (days/4) + c_avg[2] * (days/4) + c_avg[3] * (days/4)
    # all my work to calculate greed_exp
    best_days = ((100-e)/100)*days
    sub_days = ((e/100)*days)/4
    greed_exp = l1[0] * best_days + l1[0] * sub_days + l1[1] * sub_days + l1[2] * sub_days + l1[3] * sub_days

    # setting the sim values
    exploit_sim = 0
    explore_sim = 0
    greed_sim = 0

    # doing the simulation t amount of times
    for i in range(0, t):
        # storing the values in the list each time
        exploit_vals.append(exploitOnly())
        explore_vals.append(exploreOnly())
        greed_vals.append(eGreedy(e))

    # get simulated happiness for exploreOnly() by finding the average
    for i in explore_vals:
        explore_sim += i
    # avg value
    explore_sim = explore_sim / t

    # get simulated happiness for exploitOnly() by finding the average
    for i in exploit_vals:
        exploit_sim += i
    # avg value
    exploit_sim = exploit_sim / t

    # get simulated happiness for eGreed() by finding the average
    for i in greed_vals:
        greed_sim += i
    # avg value
    greed_sim = greed_sim / t

    # getting regret values by subtracting from optimal happiness
    expReg_explore = format(opt_hap - explore_exp, ".2f")
    expReg_exploit = format(opt_hap - exploit_exp, ".2f")
    expReg_greed = format(opt_hap - greed_exp, ".2f")
    simReg_explore = format(opt_hap - explore_sim, ".2f")
    simReg_exploit = format(opt_hap - exploit_sim, ".2f")
    simReg_greed = format(opt_hap - greed_sim, ".2f")

    # turning the regrets into a string
    exploit_exp = format(exploit_exp, ".2f")
    explore_exp = format(explore_exp, ".2f")
    greed_exp = format(greed_exp, ".2f")

    # turning sims to string
    explore_sim = format(explore_sim, ".2f")
    exploit_sim = format(exploit_sim, ".2f")
    greed_sim = format(greed_sim, ".2f")

    # turning opt happiness into a string
    opt_hap = format(opt_hap, ".2f")

    # big print statement

    print("Optimum Happiness: " + opt_hap + "\n" +
          # this is the explore stuff
          "\nExplore Only:\nExpected Happiness: " + explore_exp +
          "\nExpected Regret: " + expReg_explore +
          "\nSimulated Happiness: " + explore_sim + "\nSimulated Regret: " +
          simReg_explore + "\n" +
          # this is the exploit stuff
          "\nExploit Only:\nExpected Happiness: " + exploit_exp +
          "\nExpected Regret: " + expReg_exploit +
          "\nSimulated Happiness: " + exploit_sim + "\nSimulated Regret: " +
          simReg_exploit + "\n" +
          # this is the greed stuff
          "\neGreedy:\nExpected Happiness: " + greed_exp +
          "\nExpected Regret: " + expReg_greed +
          "\nSimulated Happiness: " + greed_sim + "\nSimulated Regret: " +
          simReg_greed)


simulation(700, 29)
