# coding=utf-8
"""
    Created by JungYunAh Hello!
    ProjectName : InstagramCommentProject
    Date        : 2020/12/01 4:56 오전
    Notion      : https://www.notion.so/a68b9e1475634c1389447ef8f34111b4?v=de124104486840189d382bb67efcffb4
    Github      : http://github.com/zzanunada
    Description :
"""


import xlsxwriter

from securityFolder.src.constant import EXCEL_SAVE_PATH


def start_init(excel_data, file_name):
    """
        엑셀 파일로 내보내기 위해 excel_export 호출
    :param excel_data: 엑셀데이터
    :type excel_data: list
    :param file_name: 파일명
    :type file_name: string
    :return nothing:
    """
    print("excel_export.py")
    excel_export(excel_data, file_name)


# todo 데이터를 엑셀로 내보낸다.
def excel_export(excel_list, file_name):
    """
        데이터를 엑셀파일로 내보낸다.
    :param excel_list: 엑셀에 들어갈 데이터
    :type excel_list: list
    :param file_name: 파일명
    :type file_name: string
    :return nothing:
    """
    workbook = xlsxwriter.Workbook(EXCEL_SAVE_PATH + file_name)
    worksheet = workbook.add_worksheet("comment")

    # 엑셀 header 스타일
    cell_header = workbook.add_format()
    cell_header.set_bg_color('#CECECE')
    cell_header.set_border(3)
    cell_header.set_bold()
    cell_header.set_align("vcenter")
    cell_header.set_align("center")
    cell_header.set_font_size(14)

    # 공통 스타일
    cell_common = workbook.add_format()
    cell_common.set_align("center")
    cell_common.set_align("vcenter")

    cell_common.set_font_size(12)

    # 엑셀 데이터 삽입
    for row, data in enumerate(excel_list):
        for column, token in enumerate(data):
            worksheet.write_string(row, column, token)  # 한글 utf-8 디코더

    worksheet.set_column('A:A', 8, cell_common)
    worksheet.set_column('B:D', 15, cell_common)
    worksheet.set_column('E:E', 50, cell_common)

    # 헤더 적용
    worksheet.set_row(0, 30, cell_header)

    workbook.close()
