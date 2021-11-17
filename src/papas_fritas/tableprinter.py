#!/usr/bin/env python3
""" tableprinter.py
Given a list of lists, prints a table where each row 
corresponds the individual lists given as input."""

def print_table(table_data):
    col_widths = [0] * len(table_data[0])
    for index in range(len(tableData[0])):
        col_widths[index] = max([len(row[index]) for row in table_data])
    for row in table_data:
        printed_row = []
        for index, item in enumerate(row):
            printed_row.append(f'{item:>{col_widths[index]}} ')
        print(''.join(printed_row))
    

if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'Daivd'],
                 ['dogs', 'cats', 'moose', 'goose']]
    print_table(tableData)