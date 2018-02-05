#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 创建时间 ：2018/2/2 - 17:12
"""
**** 所有的自定义模块都可以放在 /lib/site-packages/ 下变成全系统公用
本期学习内容
    一、模块学习
        1.标准库导入 import
        2.第三方库导入
        3.字符串与二进制之间转化  decode('转码类型') 是二进制 转化 字符串  encode('转码类型') 是 字符串转化二进制 soket 进行数据传输时 必须进行数据转化  需要 *** 不指定编码类型 默认走系统编码类型

"""

# 1.sys模块

# import sys
# sys.path -> Python 解释器自动查找所需模块的路径的列表
# sys.argv -> 当前文件所在的相对路径 （python 调用的补全了 绝对路径）

# print(sys.argv)

# 1.os模块

import os
# os.system('dir') -> 执行打印当前文件目录内容
# cmd_res = os.system('dir') -> 只执行一次，不能进行变量存储结果
# cmd_res = os.popen('dir').read() -> 读取当前目录内容，可以变量存储，但是需要 read() 输出
# os.mkdir('文件名') 创建一个文件夹
# print(cmd_res)
