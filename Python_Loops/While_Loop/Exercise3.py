# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:36:03 2022

@author: Talha Khokhar
"""

raining = False
while not raining:
    print("It's not raining.")
    if input("Is it raining? (y/n) ") == 'y':
        raining = True
print("It's raining!")

