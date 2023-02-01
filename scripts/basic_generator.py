from typing import *
from urllib import parse
import os

def get_list_of_presentation_folders_raw():
    my_url = os.path.abspath('.\\00_발표')

    folders = [f for f in os.listdir(my_url)]
    folders.remove('README.md')
    
    return folders



def get_list_of_problem_folders_raw():
    my_url = os.path.abspath('.\\01_문제')
    
    folders = [f for f in os.listdir(my_url)]

    return folders

# TODO: 작성자 추가 
def folder_format(raw_folder):
    # 발표자 찾기
    presentation_folder = get_list_of_presentation_folders_raw()
    last_presentation_folder = presentation_folder[-1]
    readme_path = f'./00_발표/{last_presentation_folder}/README.md'
    
    f = open(readme_path, "r", encoding='utf-8')

    is_not_presenter = True
    that_row = ''
    while is_not_presenter:
        tmp = f.readline()
        for idx in range(len(tmp)):
            if tmp[idx:idx+3] == '발표자':
                that_row = tmp
                is_not_presenter = False
                break
    
    # 발표자 포메팅
    that_row = that_row.replace('발표자', '')
    that_row = that_row.replace(':', '')
    that_row = that_row.replace('-', '')
    that_row = that_row.replace('📌', '')
    presentor = that_row.strip()


    # 폴더 포메팅
    convert_folder_name = ''
    for c in raw_folder:
        try:
            c = int(c)
        except:
            convert_folder_name += c
    convert_folder_name = convert_folder_name.strip('_')
    convert_folder_name = convert_folder_name.replace('_',", ")

    return f'{convert_folder_name} - {presentor}'


def parse_presentation_directory_path(target_folder):
    
    parent_folder = parse.quote('00_발표')
    child_folder = parse.quote(target_folder)

    return f'https://github.com/Maker-H/GroupStudy_Algo_Log/tree/master/{parent_folder}/{child_folder}'

def parse_problem_directory_path(target_folder):
    
    parent_folder = parse.quote('01_문제')
    child_folder = parse.quote(target_folder)

    return f'https://github.com/Maker-H/GroupStudy_Algo_Log/tree/master/{parent_folder}/{child_folder}'


def date_format(folder):
    date = int("".join(folder[-6:]))
    my_year = date // 10000
    my_month = (date % 10000) // 100
    my_date = date % 100

    if my_month < 10:
        my_month = f'0{str(my_month)}'
    if my_date < 10:
        my_date = f'0{str(my_date)}'

    date = f'20{my_year}-{my_month}-{my_date}'

    return date


def get_next_column_number(f):
    num = 0
    row = []
    prev = None
    tmp = f.readline()
    while True:
        if not tmp and prev != None:
            row = list(prev)
            break    
        prev = tmp
        tmp = f.readline()
        
    cnt = 0
    for idx in range(len(row)):
        if row[idx] == '|':
            cnt += 1
        if cnt == 3:
            num = row[idx-1: idx]

            my_str = "".join(num)
            num = int(my_str)
            break
    num +=1
    if num < 9:
        return f'0{num}'
    else:
        return num



# 날짜, 순번, 주제(url), 문제(url)
def make_table_row(raw_presentation_new_folder, raw_problem_new_folder, column_number):
    return f'|{date_format(raw_presentation_new_folder)}|{column_number}|[{folder_format(raw_presentation_new_folder)}]({parse_presentation_directory_path(raw_presentation_new_folder)})|[바로가기]({parse_problem_directory_path(raw_problem_new_folder)})|\n'
    



if __name__ == "__main__":
    # 갱신되는 테이블을 만든다.
    f = open('scripts/readme_table.md', "r", encoding='utf-8')
    folder_len = len(get_list_of_presentation_folders_raw())
    
    table_len = 0
    table_template = 9
    table_row_not_in_presentation_folder = 1
    while True:
        new_f = f.readline()
        table_len += 1
        if not new_f:
            break
    table_len = table_len - table_template 
    folder_len += table_row_not_in_presentation_folder

    f.close()
    # 만약 폴더 개수가 더이상 리드미를 갱신할 필요가 없다면
    if table_len >= folder_len:
        pass

    elif table_len < folder_len: 
        f = open('scripts/readme_table.md', "r", encoding='utf-8')
        # 한 줄 만들기
        column_number = get_next_column_number(f)
        table_row = make_table_row(get_list_of_presentation_folders_raw()[-1], get_list_of_problem_folders_raw()[-1],column_number)
        f = open('scripts/readme_table.md', "a", encoding='utf-8')
        f.writelines(table_row)
        f.close()
    

        # 리드미 작성
        f = open('README.md', "w", encoding='utf-8')
        n = open('scripts/readme_table.md', "r", encoding='utf-8')
        t = open('scripts/template.md', "r", encoding='utf-8')
        
        while True:
            new_n = n.readline()
            f.writelines(new_n)
            if not new_n:
                break

        while True:
            t_line = t.readline()
            f.writelines(t_line)
            if not t_line:
                break
        t.close()
        n.close()
        f.close()
    