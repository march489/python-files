#!/usr/bin/env python3
"""
grade_conversion.py
This script takes the .csv files pulled from JumpRope
and converts each kid's grade to the appropriate letter
based on their PI Score and outputs the appropriate CSV file. 

Currently, this only implements the version of the grading scale
for when there are 8 PIs or less. 
"""

import os

class Student:
    def __init__(self, line):
        """ 
        __init__ creates the student objects directly from the input.csv file
        The code in __init__ is written to handle the unusual formating 
        in the input.csv file

        Example inpout line: " -> Doe, Jane","3.4","2.61053","3.4","3"
                             " -> Last, First", "Score1", "Score2", "Score3, "Score4"
        """
        tmp = line.strip().split(',')        
        self.name = tmp[0][5:] +", " + tmp[1].split()[0].strip('\"')

        self.scores = []
        for num in tmp[2:]:
            if num.strip('"'):
                self.scores.append(round(float(num.strip('"'))))     

    def score_counter(self, target):
        return sum(map(lambda x: x == target, self.scores))

    def grade_conversion(self):
        minimum_score = min(self.scores)
        maximum_score = max(self.scores)
        if minimum_score >= 3:
            return "A"
        elif minimum_score == 2:
            if self.score_counter(2) > 2:
                return "C"
            else:
                return "B"
        else:
            if maximum_score == 1:
                return "F"
            elif self.score_counter(1) <= 1:
                return "C"
            else: 
                return "D"


class ScoreReport:
    def __init__(self, section_number, input_file):
        self.section = section_number
        self.roster = []

        with open(input_file, 'r') as f:
            for line in f.readlines()[2:]:
                self.roster.append(Student(line))
            f.close()
    
    def print_report(self, file = None):
        if file:
            with open(file, 'w') as f:
                for student in self.roster:
                    print(f'\"{student.name}\", \"{student.grade_conversion()}\"', file = f)
                    # print(f'\"{student.name}\", \"{student.scores}\"', file = f)
                f.close()

        else:
            for student in self.roster:
                print(f'\"{student.name}\", \"{student.grade_conversion()}\"')

class FileHandler:
    def __init__(self, directory):
        self.section_list = ['8', '4', 'A', 'C', 'D']
        self.file_counter = 0

        with os.scandir(directory) as gradebooks:
            for infile in gradebooks:
                current_section = self.section_list[self.file_counter]
                outfile = f'/home/marcello/Scripts/Python/outputs/converted_grades_section_{current_section}.csv'
                ScoreReport(current_section, infile).print_report(outfile)
                self.file_counter += 1

if __name__ == "__main__":
    FileHandler('/home/marcello/Scripts/Python/grade_inputs/')
