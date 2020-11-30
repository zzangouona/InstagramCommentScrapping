# coding=utf-8
"""
    Created by JungYunAh Hello!
    ProjectName : InstagramCommentScrapping
    DATE        : 2020/11/30 4:29 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
    Description : 해당 파일은 cvs 파일의 데이터를 가져온다.
"""

import os

import pandas as pd

import src.scrapping_comments
from securityFolder.src.constant import STUDENT_NUMBER_PATH
from src import scrapping_comments


def get_csv_file():
    """
    csv를 찾아서 데이터를 불러오는 함
    :return get_csv: csv에서 불러온 데이터(안에 데이터는 string)
    :rtype: dict
    """
    # csv 경로 찾기 성공!
    csv_folder_path = STUDENT_NUMBER_PATH
    csv_path = os.path.join(os.getcwd(), csv_folder_path)

    # 해당 경로에 파일이 있을 시
    if os.path.isfile(csv_path):
        get_csv = pd.read_csv(open(csv_path), names=["name", "number"], dtype=str)  # csv 오픈 시 string 데이터로 가져오기
        return get_csv


print("main.py")
# csv 데이터 가져오기
csv_data = get_csv_file()
pay_student_name = csv_data["name"].to_list()  # 이름 데이터  dict -> list
pay_student_num = csv_data["number"].to_list()  # 학번 데이터 dict - list

# 인스타그램 댓글 스크래핑 시작
src.scrapping_comments.start_int(pay_student_name, pay_student_num)
