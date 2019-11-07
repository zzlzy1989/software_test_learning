# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/11/4 15:27
# @File     : file_operations.py
# @Software : software_test_learning


"""
    文件操作:
        有一个jsonline格式的文件file.txt大小约为10K
"""

def get_lines():
    with open('file.txt','rb') as f:
        return f.readlines()


"""
    现在要处理一个大小为10G的文件，但是内存只有4G，
    如果在只修改get_lines 函数而其他代码保持不变的情况下，
    应该如何实现？需要考虑的问题都有那些？
"""

def get_big_lines():
    with open('file.txt','rb') as f:
        for i in f:
            yield i





if __name__ == '__main__':
    for e in get_lines():
        print(e.strip())

    for e in get_big_lines():
        print(e.strip())