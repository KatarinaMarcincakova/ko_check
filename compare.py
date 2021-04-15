from difflib import Differ
  
with open('files/file1.txt') as file_1, open('files/file2.txt') as file_2:
    differ = Differ()
    
    f1, f2 = file_1.readlines(), file_2.readlines()
    differ_result_array = list(differ.compare(f1, f2))
    
    sum_of_lines = len(f1) + len(f2)
    print(sum_of_lines)
    for r in differ_result_array: print(f'# {r}')