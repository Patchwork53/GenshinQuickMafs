import random
import numpy as np
import matplotlib.pyplot as plt


def royal_longsword_sim(sim_num, crit_increase, max_stack)->None:

    y=[]
    x=[]
    for crit_rate in range (1,100):
        x.append(crit_rate)
        sum = 0
        
        for i in range(sim_num):
            count=0
            current_crit = crit_rate
            while (1>0):
                count+=1
                toss = random.randint(1,100)
                if toss<=current_crit:
                    break
                if count<=max_stack:
                    current_crit=current_crit+ crit_increase

            sum+=count

        
        y.append(sim_num*100/sum-crit_rate)


    xpoints = np.array(x)
    ypoints = np.array(y)


    plt.xlabel('Base Crit Rate')
    plt.ylabel('Crit Rate Increase')
    plt.title('Royal Longsword, Crit Buff +'+str(crit_increase))
    plt.scatter(xpoints, ypoints)
    plt.show()


if __name__ =="__main__":
    royal_longsword_sim(100000,16,4)