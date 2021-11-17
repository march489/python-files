import re

def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-': 
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

msg = 'Call me at 415-555-1911 tomorrow. 415-555-9999 is my office.'
for i in range (len(msg)):
    chunk = msg[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found: ', chunk)
print('Done')