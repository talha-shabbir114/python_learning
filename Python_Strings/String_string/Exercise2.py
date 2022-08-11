# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 23:06:40 2022

@author: Talha Khokhar
"""

# Exercise 2
# Replace every occurrence of the character `"s"`
# with the character `"x"`
phrase = "Somebody said something to Samantha."
phrase = phrase.replace("s", "x")
print(phrase)
# NOTE: This leaves the capital "S" unchanged, so the
# output will be "Somebody xaid xomething to Samantha."