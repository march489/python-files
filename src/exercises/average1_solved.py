#!/usr/bin/env python3

import sys

def get_number(msg):
    while True:
        try:
            number = input(msg)
            if number:
                return int(number)
            else:
                break
        except ValueError as err:
            print(err)


ls = []
while True:
    new_number = get_number('enter a number or Enter to finish: ')
    if not new_number:
        break
    ls.append(new_number)
    print(ls)


if ls:
    print('count = ', len(ls), ', sum = ', sum(ls), ', lowest = ', min(ls), ', highest = ', max(ls), ', mean = ', round(sum(ls) / len(ls), 2))