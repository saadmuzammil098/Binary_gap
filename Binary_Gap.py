# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:04:59 2022

@author: SaadMuzammil
"""

class Final:
    def binary_gap(self, N):
        return len(max(format(N, 'b').strip('0').split('1'))) 



ob = Final()
x = [2, 22, 34]
for i in x:
    print(ob.binary_gap(i))   #Like 22 has binary value 10110









