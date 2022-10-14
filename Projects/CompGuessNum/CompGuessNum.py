#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:36:52 2020

@author: mohamadghadieh
"""

# https://www.youtube.com/watch?v=8ext9G7xspg

import random

check = False
n = 0

def guessNumber(guess, gen):
	if (guess == gen):
		return True
	return False

computerNumber = random.randint(1,10)
print("computerNumber: ", computerNumber)

guess = input("Guess the number: ")

while (not check):
    print (not check)
    check = guessNumber(guess,computerNumber)
    n += 1
    if (n!=0):
        guess = input("Try again: ")

print("Good job guessing ", computerNumber)
