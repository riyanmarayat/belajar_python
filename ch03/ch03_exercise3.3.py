# -*- coding: utf-8 -*-
#ch03_exercise3.3
"""
What Does This Code Do?
Created on Mon Apr  4 16:40:24 2022

@author: Riyan Martin Hidayat
"""
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
    
