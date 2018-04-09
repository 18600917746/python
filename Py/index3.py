#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 创建时间 ：2018/2/5 - 11:07
"""
**** 所有的自定义模块都可以放在 /lib/site-packages/ 下变成全系统公用
本期学习内容
    一、

"""
import calendar

#
# number_list = []
# while True:
#     number = input('循环输入:')
#     if number == 'q':
#         print('退出循环', number_list)
#         exit()
#     else:
#         number_list.append(number)

# 字符串操作
# name = 'ch\teng'
# print(name.capitalize());
#
# print(name.center(50, '-'))
#
# print(name.endswith('g'))  # 是否以指定字符结尾
#
# print(name.expandtabs(tabsize=30))
#
# print(name.find('g')) # 查找下标
#
# print(name.index('g')) # 查找下标

str = '这是一段{str}的{neirong}'
str1='12345郑'
# print(str.format(str='替换',neirong='内容'))
print(str.format_map({'str':'替换','neirong':'内容'}))
print(len(str1))
isalnum ='12w'
print(isalnum.isalnum())# 只能包含 数字 加 字母
isalpha ='tyuiw'
print(isalpha.isalpha())# 只能包含  字母
