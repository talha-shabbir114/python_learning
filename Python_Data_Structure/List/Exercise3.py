# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 03:58:16 2022

@author: Talha Khokhar
"""

# Using the append() method to append an item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# Insert an item as the second position
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Add the elements of tropical to thislist
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)