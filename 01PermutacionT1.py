# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:32:45 2024

@author: Informatica
"""

import copy

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

co2 = 0.020

smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations (route,ports):
    
    lista=portnames
    
    inicio=[[1,2],[2,1]]
    siguiente=copy.deepcopy(inicio)
    aux=[]
    
    puertos=len(lista)
    
    h=3
    while h<puertos:
    
        n=h
        b=h
        while b>0:
            
            CSigui=0
            siguiente=copy.deepcopy(inicio)
            for a in inicio:
                siguiente[CSigui].insert(b-1,n)
                var=siguiente[CSigui]
                aux.append(var)
                CSigui=CSigui+1
            b=b-1
        
        inicio=copy.deepcopy(aux)
        siguiente=inicio[:]
        
        aux=[]
        
        h=h+1
    
    for a in inicio:
        print(lista[0]+" "+' '.join([lista[i] for i in a]))
    
    return None
                
permutations([0], list(range(1, len(portnames))))