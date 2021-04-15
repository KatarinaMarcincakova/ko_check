from difflib import Differ

def index_of_line(file_array, file_line):
    i = 0
    file_line = file_line.replace('\n', '').replace('- ', '')
    for f in file_array:
        f = f.replace('\n', '')
        if f == file_line:
            #print(f'[F]: {f} [FILE_LINE]: {file_line}')
            return i + 1
        i += 1
    return i if i != 0 else 0

with open('files/file1.txt') as file_1, open('files/file2.txt') as file_2:
    differ = Differ()
    
    f1, f2 = file_1.readlines(), file_2.readlines()
    differ_result_array = list(differ.compare(f1, f2))
    
    sum_of_lines = len(f1) + len(f2)
    sum_of_same_lines = 0

    for l in differ_result_array:
        if l[0] == '-':
            sum_of_same_lines += 2
            print(f'[LINE]: {index_of_line(f1, l)}')
    
    print(f'[SUM Of ALL LINES]: {sum_of_lines}')
    print(f'[SUM Of SAME LINES]: {sum_of_same_lines}')
    print(f'[MATCH %]: {(sum_of_same_lines / sum_of_lines) * 100}')