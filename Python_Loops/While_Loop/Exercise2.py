# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:25:02 2022

@author: Talha Khokhar
"""

its_raining = True
while its_raining:
    print("It's raining!")
    answer = input("Or is it? (y=yes, n=no) ")
    if answer == 'y':
        print("Oh well...")
    elif answer == 'n':
        its_raining = False # end the while loop
    else:
        print("Enter y or n next time.")
print("It's not raining anymore.")