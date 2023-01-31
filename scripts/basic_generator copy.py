from typing import *
import urllib
import os
from datetime import datetime

def get_list_of_problem_folders_raw():
    return [f for f in os.listdir('00_발표')]


def get_list_of_presentation_folders_raw():
    return [f for f in os.listdir('01_문제')]

def folder_format(raw_folder):
    result = ''

    for c in raw_folder:
        try:
            c = int(c)
        except:
            result += c
    result.lstrip('_')
    result.replace('_',", ")

    return result


def parse_directory_path(folder):
    my_url = urllib.parse.quote(folder)
    return f'https://github.com/Maker-H/GroupStudy_Algo_Log/tree/master/{my_url}'


def date_format():
    my_year = datetime.today().year
    my_month = datetime.today().month
    my_day = datetime.today().day

    return f'{my_year}-{my_month}-{my_day}'


def get_column_number(f):
    num = 0

    flag = True
    while flag:
        one_line = list(f.readline())
        print(one_line)
        if one_line[-1] == '|':
            tmp = 0
            for c in list(f.readline()):
                if c == ' ':
                    tmp += 1
                if tmp == 10:
                    break

        cnt = 0
        
        for idx in range(len(one_line)):
            if one_line[idx] == '|':
                cnt += 1
            if cnt == 3:
                num = one_line[idx-1: idx]
                my_str = "".join(num)
                print(num)
                num = int(my_str)
                flag = False
                break
    
    if num < 9:
        return f'0{num}'
    else:
        return num



# 날짜, 순번, 주제(url), 문제(url)
def make_table_row(raw_presentation_new_folder, raw_problem_new_folder, column_number):
    return f'|{date_format}|{column_number}|[{folder_format(raw_presentation_new_folder)}]({parse_directory_path(raw_presentation_new_folder)})|[바로가기]({parse_directory_path(raw_problem_new_folder)})|'
    



if __name__ == "__main__":
    # readme.md 파일을 생성한다.
    f = open('scripts/readme_table.md', "r", encoding='utf-8')
    column_number = get_column_number(f)
    table_row = make_table_row(get_list_of_presentation_folders_raw()[-1], get_list_of_problem_folders_raw()[-1],column_number)
    f = open('scripts/readme_table.md', "w", encoding='utf-8')
    f.writelines(table_row)

    f = open('README1.md', "w", encoding='utf-8')
    f.writelines(table_row)
    f.writelines()
    n = open('scripts/template.md', "w", encoding='utf-8')
    f.writelines(n.read())
    
    n.close()
    f.close()