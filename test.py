#!/usr/bin/python3
from art import text2art

def outputtext():
    '''Takes in a number n, returns the square of n'''
    custom_text = text2art("УРА",font='block',chr_ignore=True)
    print('Content-Type: text/plain')
    print('')
    print('This is my test!')
    print(custom_text)

outputtext()
