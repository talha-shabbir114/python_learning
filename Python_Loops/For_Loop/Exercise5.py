# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:53:58 2022

@author: Talha Khokhar
"""

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'

for index, letterpair in enumerate(zip(uppercase, lowercase), start=1):
    upper, lower = letterpair
    print(index, upper, lower)
