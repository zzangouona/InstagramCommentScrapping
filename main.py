"""
    Created by JungYunAh Hello!
    ProjectName  : InstagramCommentScrapping
    DATE        : 2020/11/30 4:29 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
"""
import os

from securityFolder.constant import STUDENT_NUMBER_PATH

# csv 경로 찾기 성공!
csv_folder_path = STUDENT_NUMBER_PATH
csv_path = os.path.join(os.getcwd(), csv_folder_path)