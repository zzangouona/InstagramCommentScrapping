# coding=utf-8
"""
    Created by JungYunAh Hello!
    ProjectName : InstagramCommentProject
    Date        : 2020/12/01 3:38 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
    Description :
"""
import re
from src import excel_export


def start_init(scrapping_data, pay_student_name, pay_student_num):
    print("processing_data.py")
    """
        이벤트 대상자 데이터 반환 하기 위해 getting_data 호출 후 데이터 저장
        이벤트 대상자 데이터를 엑셀로 내보내기 위해 excel_export.start_init 호출

    :param scrapping_data: 스크래핑해서 가져온 데이터 댓글, 아이디
    :type scrapping_data: list
    :param pay_student_name: 학생이름
    :type pay_student_name: list(string)
    :param pay_student_num: 학번
    :type pay_student_num: list(string)
    :return noting: 
    """

    event_targets_data = getting_data(scrapping_data, pay_student_name, pay_student_num)
    excel_export.start_init(event_targets_data)


def getting_data(scrapping_data, pay_student_name, pay_student_num):
    """
        이벤트 대상자의 댓글들과 그 다른 정보들을 반환하는 함수이다.
        스크래핑한 데이터에서 csv 파일 안에 학번과 동일한 댓글이 있을 경우 list에 해당 댓글 순서, 학생의 이름, 학번, 인스타 아이디, 댓글이 추가하여 데이터를 반환한다.
    :param scrapping_data: 스크래핑해서 가져온 데이터 댓글, 아이디
    :type scrapping_data: list
    :param pay_student_name: 학생이름
    :type pay_student_name: list(string)
    :param pay_student_num: 학번
    :type pay_student_num: list(string)
    :return: [[번호, 학번, 이름, 인스타아이디, 댓글]]
    :rtype: list
    """

    all_data = []
    comment_count = 0  # 총 댓글 수 카운팅
    for cdata in scrapping_data:
        comment = cdata[0]  # 댓글

        # todo 2020.12.01 댓글에서 학번데이터만 추출
        num_pattern = re.compile(r"\d{8}")  # 댓글에서 학번 데이터을 추출 할 정규식
        get_stu_num = re.findall(num_pattern, comment.replace("-", ""))  # 학번 추출

        # todo 2020.12.01 csv 데이터 안에 있는 학번인지 check
        if not get_stu_num:  # get_stu_num == null
            continue
        stu_num = get_stu_num[0]  # 코드 가독성을 위해 변수에 저장
        check_student_num = stu_num in pay_student_num  # csv 데이터 학생 데이터에 있는 학번인지 check
        if not check_student_num:
            continue

        # 위에 조건이 모두 true 일때 list에 데이터를 추가한다
        userid = cdata[1]
        # 댓글에 나와있는 학번보다 정확한 csv 데이터를 넣기위해 index 값을 가져온다.
        stu_inx = pay_student_num.index(stu_num)
        comment_count += 1
        all_data.append([str(comment_count), pay_student_num[stu_inx], pay_student_name[stu_inx], userid, comment])

    return all_data
