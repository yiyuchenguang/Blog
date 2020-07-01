# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'html_to_doors.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from lxml import etree
import re
import sys


class HtmlToDoors(object):

    def __init__(self):
        self.fname = ""
        self.base_text = '''G_TST_TestStepAddPurpose("tempStr1");'''
        self.capl_text_output = ""
        self.doors_text_output = ""



    def test_purpose(self,input_text):
        self.text_spilt = input_text.split('\n')
        self.out_text = r'\n'.join(self.text_spilt)
        self.text_output = self.base_text.replace("tempStr1", self.out_text)
        return self.text_output

    def start_thansform(self,html):

        if html:
            # html = etree.parse(self.fname, etree.HTMLParser())
            # print(type(html))
            # result = etree.tostring(html)
            # print(result.decode("utf-8"))
            # print(html.xpath('string(.)'))//获取html全部内容
            test_cases_name = html.xpath('.//body/table[not(@class)]') #
            # print(test_cases_name)
            for case in test_cases_name:
                Action = []
                Expected = []
                single_case_message = ""
                """ find test cse num like : ST_1001"""
                casenum_str = case.xpath('.//big//a//text()')
                # print(casenum_str)
                if casenum_str:
                    casenum = re.findall(r"(ST_\d+):",casenum_str[0], re.IGNORECASE)
                    if casenum:
                        print(casenum[0])
                        # single_case_message = single_case_message + casenum[0] + "--------"
                        self.doors_text_output = self.doors_text_output +  casenum[0] + "\n"

                """ find test cse purpose descrition like : Purpose: Verify the SnaphotID for the DTC_PROG_EXE."""
                purpose_raw = case.xpath('./following-sibling::div[1]/p/text()')[0]
                # print(purpose_raw + '\n')
                single_case_message = single_case_message + purpose_raw + "\n"
                self.doors_text_output = self.doors_text_output + purpose_raw + "\n"

                """ find test streps."""
                table_rows = case.xpath('./following-sibling::div[1]/div[3]/table/tbody/tr')  # table rows,tbody can' be searched
                if not table_rows:
                    table_rows = case.xpath(
                        './following-sibling::div[1]/div[3]/table/tr')  # table rows,tbody can' be searched
                # print(table_rows)
                for table_row in table_rows[1:]:
                    test_step = table_row.xpath('./td[2]/text()')#test step column
                    if test_step: # 步骤没内容的跳过
                        description = table_row.xpath('./td[3]/text()')[0] # test step column
                        Action_macthFlag = re.match(r"(\d+).Action", test_step[0], re.IGNORECASE)
                        Expected_macthFlag = re.match(r"(\d+).Expected", test_step[0], re.IGNORECASE)

                        if Action_macthFlag:
                            Action_stepNum = Action_macthFlag.group(1)
                            description_1 = re.sub(r"TS\d+:", "", description, re.IGNORECASE)
                            description_2 = r"TS%s:%s" % (Action_stepNum, description_1)
                            Action.append(description_2)

                        if Expected_macthFlag:
                            Expected_stepNum = Expected_macthFlag.group(1)
                            description_1 = re.sub(r"TS\d+:", "", description, re.IGNORECASE)
                            description_2 = r"TS%s:%s" % (Action_stepNum, description_1)
                            Expected.append(description_2)

                single_case_message = single_case_message + "Action:\n"
                self.doors_text_output = self.doors_text_output +"Action:\n"
                for i in  Action:
                    # print(i)
                    single_case_message = single_case_message + i + "\n"
                    self.doors_text_output = self.doors_text_output + i + "\n"

                single_case_message = single_case_message + "Expected:\n"
                self.doors_text_output = self.doors_text_output + "Expected:\n"
                for i in Expected:
                    single_case_message = single_case_message + i + "\n"
                    self.doors_text_output = self.doors_text_output + i + "\n"
                # print("*"*160)
                self.doors_text_output = self.doors_text_output + "*"*160 + "\n"
                # print(self.test_purpose(single_case_message))
                self.capl_text_output =  self.capl_text_output + casenum[0] + "--------" + self.test_purpose(single_case_message)  + "\n" + "*"*160 + "\n"
            # print(capl_text_output)
        #     self.capl_text.setPlainText(capl_text_output)
        #     self.doors_text.setPlainText(doors_text_output)
        # else:
        #     self.doors_text.setPlainText("no file choosed!")
