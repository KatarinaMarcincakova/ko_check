from difflib import Differ
  
with open('files/file1.txt') as file_1, open('files/file2.txt') as file_2:
    differ = Differ()
    
    f1, f2 = file_1.readlines(), file_2.readlines()
    differ_result_array = list(differ.compare(f1, f2))
    
    sum_of_lines = len(f1) + len(f2)
    sum_of_same_lines = 0

    for r in differ_result_array:
        if r[0] == '-': sum_of_same_lines += 2
    
    print(f'[SUM Of ALL LINES]: {sum_of_lines}')
    print(f'[SUM Of SAME LINES]: {sum_of_same_lines}')
    print(f'[MATCH %]: {(sum_of_same_lines / sum_of_lines) * 100}%')