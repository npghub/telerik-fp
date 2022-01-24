#!/usr/bin/python3
"""Outputs some text"""
from art import text2art


def outputtext():
    """Does the actual output"""
    custom_text = text2art("TELERIK", font='block', chr_ignore=True)
    print('Content-Type: text/plain')
    print('')
    print('This is a successful test!')
    print(custom_text)


outputtext()
