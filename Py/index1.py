#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 创建时间 ：2018/2/2 - 10:25
"""
**** python 是强定义语言 数据类型必须手动变成才能转化
本期学习内容
    一、 用户输入
    二、学习占位符（做数据类型检测使用-类正则）
        1. %s  表示 字符串 类型
        2. %d  表示 整数数值 类型
        3. %f  表示 浮点数值 类型
    三、检测数据类型
        type() 函数 - 不会认为子类是一种父类类型
        isinstance() 函数 - 会认为子类是一种父类类型
        print(type(数据))
        print(isinstance(数据))
    四、数据类型转化函数
        1. int()  转化为 长整型数值 类型
        2. str()  转化为 字符串 类型
    五、引入标准库，使用 import
        1. getpass 密文可不见库 - 密码框
    六、流程控制语句
        1. if elif else
    七、循环
        1.while 循环 支持 while else
        2.for 循环
            ①如果遍历数字序列 for i in range(参数1,参数2,参数3) 参数1 -> 开始位置 参数2 -> 循环长度 参数3 -> 步进量
            ②如果循环数组序列 for i,j in enumerate(参数1) 参数1 循环的数据  i -> 下标 j-> 下标对应的值
            ③如果循环对象序列 for i,j in enumerate(参数1) 参数1 循环的数据  i -> 下标 j-> 下标对应的对象，对象只能采用 j['key'] 进行取值操作
"""

# 1.用户输入 - 在控制台中等待用户输入 - 异步
# userName = input("UserName:")
# userPassword = input("UserPassword:")
# print(userName,userPassword)

# 2.格式化输出字符串
#  ①使用原始的 字符串拼接方法 **效率低下，浪费内存

# info = """
#         ------------info """+userName+"""-----------
#         userName:"""+userName+"""
#         userPassword:"""+userPassword
# print(info)

#  ②使用python的占位符 参数一一对应，不少不多 **顺序不能错乱

# info2 = """
#         ------------info %s-----------
#         userName:%s
#         userPassword:%s
# """ % (userName,userName,userPassword)
# print(info2)

# 做数据类型转化 int() 只能输入 int 长整数 类型的
# userAge = int(input("UserAge:"))
# 做数据类型转化 str() 只能输入 str 字符串 类型的
# userInfo = str(input("Info:"))

#  ③使用{ } 变量赋值形式 .format() 进行内部赋值 同值，可赋值一次 ***优先推荐，可顺序错乱

# info3 = """
#         ------------info {_name}-----------
#         userName:{_name}
#         userPassword:{_UaerPassword}
#         userAge:{_userAge}
#         userInfo:{_userInfo}
# """.format(_name = userName,
#            _UaerPassword = userPassword,
#            _userAge = userAge,
#            _userInfo = userInfo)
# print(info3)

# 用户输入 密码 密文 等不可见的类型时  需要引入 getpass 标准库

# 1. getpass 密文不可见输入 Pycharm 没有反应， 可切换至系统shell交互器中
# import getpass
#
# newUserPassword = getpass.getpass("NewUserPassword:")
# print(newUserPassword)

# 流程控制语句 if else  elif

# _userName = 'cheng'
# _userPassword = '123456'
# userName = input('userName:')
# userPassword = input("UserPassword:")
#
# if _userName == userName and _userPassword == userPassword:
#     print('登录成功！{name}'.format(name=userName))
# else:
#     print('验证失败！')

# 3.循环控制语句
# ①while 循环条件语句  支持 while else
# count = 0
# while count < 3:
#     age = int(input('age:'))
#     if age == 12:
#         print('cg')
#         break
#     else:
#         print('sb')
#     count += 1
# else:
#     print('输入次数过多！')

# ②for in 循环语句 range(参数1,参数2,参数3) 参数1 -> 开始位置 参数2 -> 循环长度 参数3 -> 步进量

# for i in range(3):
#     age = int(input('age:'))
#     if age == 12:
#         print('cg')
#         break
#     else:
#         print('sb')

# 关于列表的循环取值
# arr = ['a','b','c','d','e']
# for i, j in enumerate(arr):
#     print(i, j)

# 关于对象的循环取值 j['name'] 不能使用 . 只能使用
# obj = [{
#     'name': 'cheng',
#     'age': 21
# }, {
#     'name': 'zhang',
#     'age': 22
# }, {
#     'name': 'li',
#     'age': 23
# }]
# for i, j in enumerate(obj):
#     print(i, j['name'])
