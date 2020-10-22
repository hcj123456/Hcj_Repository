#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:huangCijin
# datetime:2020/10/21 15:24
# software: PyCharm
import allure
import pytest


class Test_HCJ:
    @allure.step(title='第一次测试')
    def test_001(self):
        mkmk
        allure.attach("输出好帅","11111")
        print('hcj你好帅哦！')
    @allure.step(title='第二次测试')
    @pytest.allure.testcase("aaaaa")
    def test_002(self):
        print('njnjnjnjj')
    @allure.step(title='第三次测试')
    @allure.issue("ssssss","查看bug")
    def test_0003(self):
        print("艰苦艰苦艰苦看见就")