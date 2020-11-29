"""
    Created by JungYunAh Hello!
    ProjectName  : InstagramCommentScrapping
    DATE        : 2020/11/30 4:29 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
"""
import os
import pandas as pd

from securityFolder.constant import STUDENT_NUMBER_PATH

# csv 경로 찾기 성공!
csv_folder_path = STUDENT_NUMBER_PATH
csv_path = os.path.join(os.getcwd(), csv_folder_path)

# 해당 경로에 파일이 있을 시
if os.path.isfile(csv_path):
    csv_file = pd.read_csv(open(csv_path), names=["name", "number"], dtype=str)  # csv 오픈 시 string 데이터로 가져오기
    pay_student_name = csv_file["name"].to_list()  # 이름 데이터  dict -> list
    pay_student_num = csv_file["number"].to_list()  # 학번 데이터 dict - list
    print(pay_student_name)
