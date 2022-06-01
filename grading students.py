#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grades = []
    
    for num in range(len(grades)):
        next_multiple = grades[num]
        
        while True:
            next_multiple +=1
            if next_multiple % 5 == 0:
                break
        if grades[num] >= 38:
            if next_multiple - grades[num] < 3:
                grades[num] = next_multiple
                final_grades.append(grades[num])
            else:
                final_grades.append(grades[num])
        elif grades[num]<38:
            final_grades.append(grades[num])
    
    return final_grades
                
                
                
            

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
