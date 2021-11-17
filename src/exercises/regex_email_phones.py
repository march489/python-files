#!/usr/bin/env python3.9
""" regex_exmail_phones.py
This script takes text from the clipboard,
runs it through regexes to extract every phone number
and email address, and then returns the extracted 
phone numbers and emails to the clipboard. """

import re, pyperclip3

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # exchange
    (\s|-|\.)?                      # separator
    (\d{4})                         # last four digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # at-sign
    [a-zA-Z0-9.-]+               # domain
    (\.[a-zA-z]{2,4})                         # dot-something
)''', re.VERBOSE)

text = str(pyperclip3.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[7]:
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

if matches:
    pyperclip3.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')