# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:32:45 2024

@author: Informatica
"""

import random
import time

prob = 0.5

contdog=0
contnodog=0
n=0 

while n<1:
    # time.sleep(0.01)
    varal=random.random()
    if varal < prob:
        print('dog')
        contdog=contdog+1
    else:
        print('no dog')
        contnodog=contnodog+1
        
    n=n+1
print("ha entrado: ", contdog)
print("no ha entrado: ", contnodog)
    
    
   
    