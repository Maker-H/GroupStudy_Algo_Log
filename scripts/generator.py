from typing import *
import fnmatch
import yaml
import os

def get_list_of_folders(dir_name: str):
    solution_file = [f for f in os.listdir(dir_name)]

    fileList = os.listdir(dir_name)
    result = []
    for entry in fileList:
        full_path = os.path.join(dir_name, entry)
        if os.path.isdir(full_path):
            result = result + get_list_of_files(full_path)
        else:
            result.append(full_path)
    return result

def parse_yaml_headers(mdtext: str):
    result = {}
    try:
        start_index = mdtext.index("---")
        # --- 가 시작이 아니라면 올바른 포멧이 아님
        if start_index != 0:
            raise ValueError(f"파싱할 수 없습니다.")

        end_index = mdtext.index("---", start_index + 1)
        mdtext = mdtext[start_index: end_index]

        result = yaml.load(mdtext, Loader=yaml.FullLoader)
    except ValueError:
        raise ValueError
    except Exception as e:
        raise e

    return result


# yaml에 필요한 key 가 있는지 검사
def valid_yaml_headers(yaml_dict: dict):
    keys = ("file", "name", "src", "tags", "done")
    return set(keys).issubset(yaml_dict)


# 해당 디렉터리 하위 디렉터리 까지 전부 순회하여 파일을 탐색한 뒤
# table 생성할 데이터를 만듬
def make_list(path: str):
    # markdown 파일만 필터링
    file_list = fnmatch.filter(get_list_of_files(path), "*.md")

    result = []
    for file in file_list:
        try:
            dir = os.path.dirname(file)
            body = file_read_to_end(file)
            headers = parse_yaml_headers(body)

            if not valid_yaml_headers(headers):
                raise ValueError("필요한 키가 포함되어있지 않음")

            result.append({
                "file_name": headers["file"],
                "file": os.path.join(dir, headers["file"]).replace('\\', '/'),
                "name": headers["name"],
                "src": headers["src"],
                "tags": headers["tags"],
                "done": headers["done"],
            })
            print(dir)

        except Exception as e:
            raise e

    return result

def make_markdown_table(hlist: list[dict]):
    """
    흠..
    """
    result = []

    columns = [
        {"name": "#", "size": 5},
        {"name": "문제 이름", "size": 20},
        {"name": "유형", "size": 15},
        {"name": "풀이", "size": 10},
        {"name": "완료", "size": 6},
    ]
    result.append('|'.join([key["name"] for key in columns]))
    result.append('|'.join([key["size"]*'-' for key in columns]))

    for index, header in enumerate(hlist):
        done = '✔️' if header["done"] else '❌'
        result.append(
            f"{index+1}|[{header['name']}]({header['src']})|{', '.join(header['tags'])}|[{header['file_name']}]({header['file']})|{done}")
    result.append('')
    return '\n'.join(result)


if __name__ == "__main__":
    # 문제를 탐색할 디렉터리 이름
    target_path = "./baekjoon"
    # 인식한 알고리즘 문제 목록
    rows = make_list(target_path)
    # markdown 테이블 문자열
    md_table = make_markdown_table(rows)
    # 템플릿 파일을 불러온다
    template = file_read_to_end('template.md')

    # 템플릿 파일 내 특정 문자를 생성한 마크다운 테이블 코드로 치환한다.
    readme_text = template.replace("__file_table__", md_table)

    # radme.md 파일을 생성한다.
    f = open(os.path.join(BASE_DIR, 'README.md'), "w", encoding='utf-8')
    f.write(readme_text)
    f.close()