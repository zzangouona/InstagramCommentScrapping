# coding=utf-8
"""
    Created by JungYunAh Hello!
    ProjectName : InstagramCommentProject
    Date        : 2020/12/01 3:38 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
    Description :
"""
import copy
import random
import re
from collections import Counter

import numpy as np

from securityFolder.src.constant import COMMENT_HEADER, RANK_LIST, RANDOM_COMMENT_HEADER, MAX_COMMENT_HEADER, \
    MAX_COMMENT_RANK
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

    # 이벤트 대상자 선별
    event_targets_data = getting_data(scrapping_data, pay_student_name, pay_student_num)
    temp_targets_data = copy.deepcopy(event_targets_data)

    # 이벤트 댓글 중 학번데이터 따로 추출(최빈값을 위해 필요)
    event_number_data = get_list_index(temp_targets_data, 1)
    # todo 이벤트 대상자 중 최다 댓글 작성 n순
    # 이벤트 대상자 중 댓글 작성 학생 n 순위 선별(랭킹)
    event_targets_mode = getting_mode_data(event_number_data, MAX_COMMENT_RANK, pay_student_name, pay_student_num)
    # todo 이벤트 대상자 랜덤 뽑기 n 순위 n 명 선별
    # 이벤트 대상자 랜덤 뽑기 n 순위 n명 선별
    event_targets_rank = get_random_rank_data(temp_targets_data, RANK_LIST)
    print(event_targets_data)


    # 엑셀 내보내기 전 헤더 값 추가하기
    # 이벤트 대상자 엑셀 내보내기
    event_targets_data.insert(0, COMMENT_HEADER)
    excel_export.start_init(event_targets_data, "event_comments.xlsx",)
    # 이벤트 대상자 중 랜덤 추첨 엑셀 내보내기
    event_targets_rank.insert(0, RANDOM_COMMENT_HEADER)
    excel_export.start_init(event_targets_rank, "rank_comments.xlsx", )
    # 이벤트대상자 중 최다 댓글 작성자 엑셀 내보내기
    event_targets_mode.insert(0, MAX_COMMENT_HEADER)
    excel_export.start_init(event_targets_mode, "max_comments.xlsx")


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
        # todo index(string) 를 사용해서 코드 개
        try:
            # 댓글에 나와있는 학번보다 정확한 csv 데이터를 넣기위해 index 값을 가져온다.
            stu_inx = pay_student_num.index(get_stu_num[0])
        except ValueError:  # index 값을 찾을 수 없을때
            continue

        # 위에 조건이 모두 true 일때 list에 데이터를 추가한다
        userid = cdata[1]
        comment_count += 1
        all_data.append([str(comment_count), pay_student_num[stu_inx], pay_student_name[stu_inx], userid, comment])

    return all_data


def get_random_rank_data(get_data, rank_list):
    """
        n 순위별 n명 추첨 함수 (중복 x)
    :param get_data: 이벤트 대상자 댓글
    :type get_data: list
    :param rank_list: 랭크 별 n명 추첨 리스트
    :type rank_list: list
    :return: 추첨 결과 => [[등수, 학번, 이름, 아이디, 댓글]]
    :rtype: list
    """
    rank_data = []
    for i, list_data in enumerate(rank_list):
        random_data = getting_random_data(get_data, list_data, i)  # 댓글 중 중복 없이 추첨
        get_data = overlap_random(get_data, random_data).tolist()  # 추첨된 데이터의 학번과 중복된 댓글 제rj
        rank_data = rank_data+random_data
    return rank_data


# 데이터 중 n개 추가
def getting_random_data(get_data, num, rank):
    """
        n 순위의 n명을 추첨해주는 함수(중복 x)
    :param get_data: 이벤트 대상자 데이터
    :type get_data: list
    :param num: n 명
    :type num: int
    :param rank: n 순위
    :type rank: int
    :return: 추첨된 데이터 [[n등, 학번, 이름, 아이디, 댓글]]
    :rtype: list
    """
    rank_text = str(rank+1)+"등"
    temp_random = random.sample(get_data, num)
    for r_data in temp_random:
        r_data[0] = rank_text  # 기본 번호 란에 등수 추가
    return temp_random


# 추첨된 학생 정보와 중복된 데이터 삭제 함수
def overlap_random(get_data, random_data):
    """
        추첨된 데이터와 중복된 학생 데이터를 가진 댓글 삭제
    :param get_data: 이벤트 대상자 댓글
    :type get_data: list
    :param random_data: 추첨된 데이터
    :type random_data: list
    :return: 중복제거된 데이터
    :rtype: list
    """
    temp_overlap = np.array(get_data)
    for o_data in random_data:
        overlap_data = temp_overlap[~(temp_overlap[:, 1] == o_data[1]), :]  # 학번이 다른 데이터만 저장터(중복 제거)
        temp_overlap = overlap_data
    return overlap_data


# todo 2D 데이터 n 번째 인덱스 값만 return 함수
# 2D 데이터 인수 안에서 index 인수 데이터 return
def get_list_index(get_data, num):
    """
        2차원배열에서 n행 번째 값만 return 해주는 함수
    :param get_data: 2차원배열
    :type get_data: list
    :param num: return 할 n 번째 값
    :type num: int
    :return: 2차원배열에서 n행 번째 값 numpy.array
    :rtype: numpy.array
    """
    temp_np = np.array(get_data)
    return temp_np[:, num]


# todo 댓글 중 최빈값 n 순위로 가져오기
def getting_mode_data(max_list, rank_num, pay_student_name, pay_student_num):
    """
        댓글 중 최다 댓글 작성자 n 순위 데이터
    :param max_list: 이벤트 대상자 데이터(학번만 있음)
    :type max_list: list
    :param rank_num: n 순위
    :type rank_num: int
    :param pay_student_name: 학생 이름 데이터
    :type pay_student_name: list
    :param pay_student_num: 학번 데이터
    :type pay_student_num: list
    :return: [[ n 등, 학번, 이름, 댓글 횟수]]
    :rtype: list
    """
    get_mode = Counter(max_list).most_common(rank_num)
    mode_data = []
    for i, m_data in enumerate(get_mode):
        m_inx = pay_student_num.index(m_data[0])
        mode_data.append([str(i+1)+"등", pay_student_name[m_inx], pay_student_num[m_inx], str(m_data[1])])
    return mode_data
