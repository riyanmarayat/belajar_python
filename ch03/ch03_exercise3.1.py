# -*- coding: utf-8 -*-
# ch03_exercise3.1
"""
Created on Mon Apr  4 15:41:52 2022
Validating User Input
@author: Riyan Martin Hidayat
"""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    while result != 1 and result != 2:
        result = int(input('Incorrect. Please enter result (1=pass, 2=fail): '))
    
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')

