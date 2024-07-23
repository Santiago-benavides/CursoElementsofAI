# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:32:45 2024

@author: Informatica
"""

import random
import math

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing

    prob=math.exp(-(S_old-S_new)/T)
    if S_new > S_old:
        return 1.0
    else:
        return prob



# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    randval=random.random()
    print(randval)
    if randval < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)


accept(150 ,100, 200)