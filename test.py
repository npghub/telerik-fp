#!/usr/bin/python3
from art import text2art


def outputtext():
    '''Outputs some text'''
    custom_text = text2art("TELERIK ACADEMY", font='block', chr_ignore=True)
    print('Content-Type: text/plain')
    print('')
    print('This is a successful test!')
    print(custom_text)


outputtext()
