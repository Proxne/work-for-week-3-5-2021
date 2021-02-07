# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:15:15 2021

@author: lordb
"""

import numpy as np
from matplotlib import pyplot as plt
 
def rektangelmetoden(a, t):
    N = len(a)
    v = [0]
    A = 0
    for i in range(N-1):
        h = t[i+1] - t[i]
        A += a[i] * h
        v.append(A)
 
    return(v)
 
def liten_fallskjerm():
    f = open("D:\\Python.brageprojekt\liten fallskjerm.txt", "r")
 
    data = f.read()
     
    a_maling = [float(val) for val in data.split("[")[1].split("]")[0].split(", ")]
    t_maling = [float(val) for val in data.split("[")[2].split("]")[0].split(", ")]
 
 
    f.close()
  
    v_maling = rektangelmetoden(a_maling, t_maling)

    g = 9.81
    m = 0.37
    k = 0.045 
    t_0 = t_maling[0]
    t_s = t_maling[-1]
    
    N = 500
 
    v = np.zeros(N)
    t = np.linspace(t_0, t_s, N)
    
    for i in range(N-1):
        h = t[i+1] - t[i]
        v[i+1] = v[i] + (h *(g - k * v[i]**2 / m) )

    plt.plot(t,v)
    plt.grid()
    plt.plot(t_maling, v_maling)
    
def middels_fallskjerm():
    f = open("D:\\Python.brageprojekt\middels fallskjerm.txt", "r")
 
    data = f.read()
    
    a_maling = [float(val) for val in data.split("[")[1].split("]")[0].split(", ")]
    t_maling = [float(val) for val in data.split("[")[2].split("]")[0].split(", ")]
    
    
    f.close()
    
    v_maling = rektangelmetoden(a_maling, t_maling)
    
    g = 9.81
    m = 0.37
    k = 0.21
    t_0 = t_maling[0]
    t_s = t_maling[-1]
    
    N = 500
    
    v = np.zeros(N)
    t = np.linspace(t_0, t_s, N)
    
    for i in range(N-1):
        h = t[i+1] - t[i]
        v[i+1] = v[i] + (h *(g - k * v[i]**2 / m) )
        
    plt.plot(t,v)
    plt.grid()
    plt.plot(t_maling, v_maling)

def stor_fallskjerm():
    f = open("D:\\Python.brageprojekt\stor fallskjerm.txt", "r")
 
    data = f.read()

    a_maling = [float(val) for val in data.split("[")[1].split("]")[0].split(", ")]
    t_maling = [float(val) for val in data.split("[")[2].split("]")[0].split(", ")]
 
 
    f.close()
  
    v_maling = rektangelmetoden(a_maling, t_maling)

    g = 9.81
    m = 0.37
    k = 0.875
    t_0 = t_maling[0]
    t_s = t_maling[-1]
    
    N = 500
    
    v = np.zeros(N)
    t = np.linspace(t_0, t_s, N)
    
    for i in range(N-1):
        h = t[i+1] - t[i]
        v[i+1] = v[i] + (h *(g - k * v[i]**2 / m) )
        
    plt.plot(t,v)
    plt.grid()
    plt.plot(t_maling, v_maling)
    
stor_fallskjerm()
middels_fallskjerm()
liten_fallskjerm()