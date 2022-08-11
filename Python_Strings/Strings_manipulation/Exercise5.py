# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 22:57:15 2022

@author: Talha Khokhar
"""

# Exercise 5
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
string1 = string1.lower()
# (string2 will pass unmodified)
string3 = string3.lower()
string4 = string4.strip().lower()

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))
