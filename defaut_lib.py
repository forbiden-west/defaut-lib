import os
import time
import random
def passwd():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(8):
        passwd0 = ''
        for i in range(8):
            passwd0 += random.choice(chars)
    return passwd0
def cls():os.system('clear')
def delay():input()