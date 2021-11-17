#!/usr/bin/env python3.9
""" myclip.py -- A multi clipboard program

This program takes single word command-line 
arguments and then adds a pre-written message to
the clipboard. This can then be pasted as needed 
into an email. """
import sys
import pyperclip3

TEXT = {
    'agree': 'Yes, I agree. That sounds great.',
    'busy': 'Sorry, can we do later this week or next week?'
}

if len(sys.argv) < 2:
    print('Usage: python myclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip3.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

    