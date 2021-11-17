import re

phone_number_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_number_regex.search('My phone number is 415-555-4242.')
print('mo.group(1): ', mo.group(1))
print('mo.group(2): ', mo.group(2))
print('mo.group(0): ', mo.group(0))
print('mo.group(): ', mo.group())
print('mo.groups(): ', mo.groups())