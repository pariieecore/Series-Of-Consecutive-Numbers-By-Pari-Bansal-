# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 14:53:22 2025

@author: Pari
"""
# To print series of digit from given number

n = int(input("Enter the number: "))
seq = ""
for i in range(1,n+1):
    seq += str(i)
d = int(input("Enter the digit till you want the series to be printed: "))
print("The required seq is: ",seq[:d])



#Reverse task
# To find the number at a given digit

position = int(input("Enter the digit position: "))
sequence = ""
for i in range(1, d):
    sequence += str(i)
    if len(sequence) >= position:
        print("Number at digit", position, "is:", i)
        break
