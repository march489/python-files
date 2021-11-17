#!/usr/bin/env python3.9
""" bullet_point_adder.py -- 
Adds Wikipedia bullet points to the start of each line
of text on the clipboard.  """

import pyperclip3

text = str(pyperclip3.paste()).strip('b\'').split('\\n')
for index, item in enumerate(text):
    text[index] = '* ' + item
pyperclip3.copy('\n'.join(text))

