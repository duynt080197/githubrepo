"""Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:
Ví dụ với user pymivn, sử dụng dữ liệu ở JSON format tại
https://api.github.com/users/pymivn/repos
Câu lệnh của chương trình có dạng:
python3 githubrepos.py username"""

import requests
import sys
import json
import log

logger = log.get_logger(__name__)


def githubrepos(input_data):
    """Trả về `list` chứa tất cả các repository của user

    :param input_data: tên user

    Nếu tên user không đúng trả về None
    """

    url = "https://api.github.com/users/{}/repos".format(input_data)
    r = requests.get(url)
    if r.status_code == 200:
        result = [data["name"] for data in json.loads(r.text)]
    else:
        result = None
    return result


def solve(input_data):
    """:param input_data: tên user"""

    logger.debug("All repository'of %s:", input_data)
    result = githubrepos(input_data)
    return result


def main():
    input_data = sys.argv[1]
    repos = solve(input_data)
    for repo in repos:
        print(repo)


if __name__ == "__main__":
    main()
