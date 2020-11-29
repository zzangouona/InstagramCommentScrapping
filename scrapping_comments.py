# coding=utf-8
from selenium import webdriver
"""
    Created by JungYunAh Hello!
    ProjectName : InstagramCommentScrapping
    DATE        : 2020/11/30 6:32 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
    Description :
"""


def start_int(pay_student_name, pay_student_num):
    print("scrapping_comment")
    driver = webdriver.Chrome()
    driver.get("https://github.com/zzanguna")
