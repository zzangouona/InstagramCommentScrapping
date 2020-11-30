# coding=utf-8
import time

from selenium import webdriver
from securityFolder.src.constant import INST_LOGIN_ADDRESS, INSTA_ID, INSTA_PW

"""
    Created by JungYunAh Hello!
    ProjectName : InstagramCommentScrapping
    DATE        : 2020/11/30 6:32 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
    Description :
"""


def start_int(pay_student_name, pay_student_num):
    print("scrapping_comment.py")
    driver = webdriver.Chrome()
    # 인스타그램 로그인
    instagram_signup(driver)


# 인스타 로그인 스크래핑 함수
def instagram_signup(driver):
    driver.get(INST_LOGIN_ADDRESS)
    time.sleep(3)
    username = driver.find_element_by_name('username')  # 아이디 입력
    username.send_keys(INSTA_ID)
    password = driver.find_element_by_name('password')  # 비밀번호 입력
    password.send_keys(INSTA_PW)
    # 로그인
    submit = driver.find_element_by_tag_name('form')
    submit.submit()
    time.sleep(3)

    # 자동로그인 클릭
    driver.find_element_by_css_selector('.sqdOP').click()
    time.sleep(3)

    # 알림설정 안함 클릭
    driver.find_element_by_css_selector('.HoLwm').click()
    time.sleep(3)

