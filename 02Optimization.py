# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:32:45 2024

@author: Informatica
"""

import math
import time
# import matplotlib.pyplot as plt
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [random.random()/3, random.random()/3, random.random()/3]
# print(w)
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]
# h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-1.3+x/9.)*w[1]+math.sin(-3.2+x/30.)*w[2] for x in range(100)]



def climb(x, h):
    # keep climbing until we've found a summit
    summit = False
    mov="centro"
    # Index=[]
    # contIndex=0
    print("el valor inicial de la lista es: ",x)
   
    

    # edit here
    
    while not summit:
        #summit = True         # stop unless there's a way up
        time.sleep(1)
        if x>=5 and x<=94: #revisa que no me pase de los rangos del vector
            #print("paila")
            vecH=h[x-5:x+6]#escogo la mitad del posible vector con 5 pasos a izquierda o derecha
        elif x<5:
            vecH=h[:11]
        elif x>94:
            vecH=h[89:]
        
        # print(vecH)
        
        
        
        maxVec=max(vecH)#encuentro el valor máximo del rango de 11 datos
        if vecH.index(maxVec)==5: #si los números coinciden, el punto máximo está en la mitad, para el algoritmo
            # print("el punto maximo coincide con la mitad")
            # print("el valor máximo de la lista h es: ", max(h), " el valor máximo en este rango es: ",maxVec)
            summit=True
            # plt.close()
            # plt.plot(h)
            
        else:
                        
            # print("el valor del indice es: ",vecH.index(maxVec))
            x=x+vecH.index(max(vecH))-5#vuelvo a poner el centro en el punto mas algo e inicio el algoritmo. 
            # print(x)
    
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)
