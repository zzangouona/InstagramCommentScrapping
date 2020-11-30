# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from securityFolder.src.constant import INST_LOGIN_ADDRESS, INSTA_ID, INSTA_PW, INST_ADDRESS
from src import processing_data

"""
    Created by JungYunAh Hello!
    ProjectName : InstagramCommentScrapping
    DATE        : 2020/11/30 6:32 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
    Description :
"""


# todo 2020.11.30 인스타그램 스크래핑 시작
def start_int(pay_student_name, pay_student_num):
    print("scrapping_comments.py")
    """
        인스타그램 로그임 함수 호출
        인스타그램 스크래핑 함수 호출 후 데이터를 받음
        processing_data.start_init 함수 호출
    :param pay_student_name: 학생 이름
    :type pay_student_name: list(string) 
    :param pay_student_num: 학번
    :type pay_student_num: list(string)
    :return noting:  
    """
    print("def start_int")
    driver = webdriver.Chrome()
    # 인스타그램 로그인
    instagram_signup(driver)

    # 인스타댓글 크롤링해서 가져온다.
    scrapping_data = scrapping_inst_comment(driver)
    processing_data.start_init(scrapping_data, pay_student_name, pay_student_num)


# todo 2020.11.30 인스타그램 로그인 크롤링 함수 구현
def instagram_signup(driver):
    print("def instagram_signup")
    """
    인스타 로그인 크롤링 함수
    :param driver: chrome web driver
    :type driver:
    :return noting:
    """

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
    driver.find_element_by_class_name('sqdOP').send_keys(Keys.RETURN)
    time.sleep(1.5)

    # 알림설정 안함 클릭
    driver.find_element_by_class_name('HoLwm').send_keys(Keys.RETURN)
    time.sleep(1.5)


# todo 2020.11.30 인스타그램 댓글, 유저 아이디 정보 스크래핑 함수 구현
def scrapping_inst_comment(driver):
    print("def scrapping_inst_comment")
    """
    인스타 댓글 Element를 scrapping 하여 인스타 댓글과 사용자 아이디 데이터 list 를 가져온다.
    :param driver: chrome web driver
    :type driver:
    :return [[comment, userid]]: 인스타 그램 댓글과 사용자 아이디 데이터
    :rtype list :
    """

    # 댓글 스크래핑 주소 접속
    driver.get(INST_ADDRESS)
    time.sleep(3)

    # 댓글 더보기 버튼 클릭
    # todo 2020.11.30 댓글 더보기 기능 코드 정리
    # 조건 : 더보기 버튼이 있을 경우(클래스로 판단) selenium.send_keys를 사용해서 자동 클릭
    while True:
        try:
            driver.find_element_by_class_name('afkep').send_keys(Keys.RETURN)
            time.sleep(1.5)
        except Exception as e:
            print(e)
            break

    scrapping_data = []  # 인스타 아이디, 인스타 댓글 보내짐
    comment_element = driver.find_elements_by_class_name('gElp9 ')  # 댓글 element
    for el in comment_element:
        container = el.find_element_by_class_name('C4VMK')
        # 인스타 아이디
        userid = container.find_element_by_class_name('_6lAjh').text
        # 인스타 댓글
        content = el.find_element_by_css_selector('.C4VMK > span').text
        content = content.replace('\n', ' ').strip().rstrip().encode('utf-8')
        scrapping_data.append([content, userid])
    return scrapping_data


