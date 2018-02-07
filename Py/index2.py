#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 创建时间 ：2018/2/2 - 17:12
"""
**** 所有的自定义模块都可以放在 /lib/site-packages/ 下变成全系统公用
本期学习内容
    一、模块学习
        1.标准库导入 import
        2.第三方库导入
    二、bytes 数据类型讲解 略
    三、字符串与二进制之间转化  decode('转码类型') 是二进制 转化 字符串  encode('转码类型') 是 字符串转化二进制 soket 进行数据传输时 必须进行数据转化  需要 *** 不指定编码类型 默认走系统编码类型
    四、列表
"""
# 一、模块

# 1.sys模块

# import sys
# sys.path -> Python 解释器自动查找所需模块的路径的列表
# sys.argv -> 当前文件所在的相对路径 （python 调用的补全了 绝对路径）

# print(sys.argv)

# 1.os模块

# import os
# os.system('dir') -> 执行打印当前文件目录内容
# cmd_res = os.system('dir') -> 只执行一次，不能进行变量存储结果
# cmd_res = os.popen('dir').read() -> 读取当前目录内容，可以变量存储，但是需要 read() 输出
# os.mkdir('文件名') 创建一个文件夹
# print(cmd_res)

# 三、编码转化

# 编码转化 字符串 转化 bytes（二进制）

# Str = '凄凄惨惨戚戚，冷冷清清'
# print(Str.encode(encoding='utf-8'))

# 编码转化 bytes（二进制） 转化 字符串

# print(Str.encode(encoding='utf-8').decode(encoding='utf-8'))

# 四、列表

# 1.声明 列表 -> 类数组 取值 也是通过 [下标]

List = ['Zhang', 'San', 'Li', 'Si', 'Wang', 'Wang', 'Wu', 'Wang', 'Zhao', 'Liu']

# 2.取值

# ①.对应取值 列表[下标]
# print(List[0], List[4])  # Zhang Wang
# ②.区间取值 列表[开始下标:结束下标]  取值区间为 ‘左闭右开’
# print(List[2:5])  # ['Li', 'Si', 'Wang']
# ③.取最后一个下标对应的值 -1
# print(List[-1])  # ['Liu']
# ④.取后三位  List[-4:] 冒号后面省略 默认取到最后一位  因为 ‘左闭右开’
# print(List[-2:])  # ['Zhao', 'Liu']
# ⑤.冒号前面省略 默认是从零开始
# print(List[:5]) # ['Zhang', 'San', 'Li', 'Si', 'Wang']
# ⑥.如果全部省略 则输出原列表
# print(List[:]) # ['Zhang', 'San', 'Li', 'Si', 'Wang', 'Wu', 'Zhao', 'Liu']

# 3.添加值

# ①列表尾部插值 -> 对应 js push()  append(值) 默认插入到最后一位
# List.append('Wu')
# ②列表前部插值 -> 对应 js unshift()   insert('指定插入的位置下标'，值)
# List.insert(0,'Zhou') # ['Zhou', 'Zhang', 'San', 'Li', 'Si', 'Wang', 'Wu', 'Zhao', 'Liu', 'Wu']

# 4.修改 同 js

# List[2] = 'He' # ['Zhou', 'Zhang', 'He', 'Li', 'Si', 'Wang', 'Wu', 'Zhao', 'Liu', 'Wu']

# 5.删除

# ①指定对应 key 删除
# List.remove('He') # ['Zhou', 'Zhang', 'Li', 'Si', 'Wang', 'Wu', 'Zhao', 'Liu', 'Wu']
# ②根据下标删除对应的值 可以 -1
# del List[2] # ['Zhou', 'Zhang', 'Si', 'Wang', 'Wu', 'Zhao', 'Liu', 'Wu']
# ③删除最后一个值 -> 对应 js 的 pop(下标) 如果 不传参 默认删除最后一个，参数可以传 负数
# List.pop()
# ④删除第一个值 -> 对应 js 的 unshift()

# 6.查找值对应的下标 -> 同 js 的indexOf()  不同 如果找不到会报错

# print(List.index('Cheng')) # 没有找到就会报错  ValueError:'Cheng' is not in list
# print(List.index('Li')) # 2

# 7.相同值的个数

# print(List.count('Wang')) # 3

# 8.清空一个列表

# ①使用 clear()
# List.clear() # 返回 []
# ②使用赋值操作 List = []
# List = []  # 返回 []

# 9.翻转列表 同 js 的 reverse()

# List.reverse() # ['Liu', 'Zhao', 'Wang', 'Wu', 'Wang', 'Wang', 'Si', 'Li', 'San', 'Zhang']

# 10.列表排序

# ①默认使用码进行排列 同 js 的 sort() 不同 不能传入 -1
# List.sort() # ['Li', 'Liu', 'San', 'Si', 'Wang', 'Wang', 'Wang', 'Wu', 'Zhang', 'Zhao'] 特殊符号 > 数字 > 大写字母 > 小写字母

# 11.列表的合并

# ①使用 extend() 同 js 的 concat()
List1 =['1','2','3','4']
List.extend(List1) #['Zhang', 'San', 'Li', 'Si', 'Wang', 'Wang', 'Wu', 'Wang', 'Zhao', 'Liu', '1', '2', '3', '4']




print(List)
