# !/usr/bin/env python
# -*- codeing: utf-8 -*-

"""
双链表模块，没啥用，直接用SQL操作更好
"""
__author__ = 'bearcarl'
__version__= '1.0'

"""结点类"""


class Node(object):
    def __init__(self, data = []):
        self.data = data
        self.pre = None
        self.next = None


class DouLink(object):
    """初始化双向链表"""

    def __init__(self):
        self.head = Node('head')
        self.length = 1

    def add(self, value):
        p = self.head
        new = Node(value)
        while p.next:
            p = p.next
        p.next = new
        new.pre = p
        self.length += 1

    def remove(self, ID):
        p = self.head
        while p.next:
            if p.data[0] == ID:
                temp = p.pre
                ans = p.next
                temp.next = ans
                ans.pre = temp
                return p
                self.length -= 1
            else:
                p = p.next
        raise AttributeError(u"can't find this element")

    def release(self):
        self.head = Node('head')
        self.length = 1

    def find(self, value, key):
        results = []
        p = self.head
        while p.next:
            # 检测下类型, 有时候会 int 和 str 比较看不出来
            # print(type(key))
            # print(type(value))
            # print(type(p.data[2]))
            if key == 0 and str(p.data[0]) == value:
                results.append(p.data)
            elif key == 1 and p.data[1] == value:
                results.append(p.data)
            elif key == 2 and str(p.data[2]) == value:
                results.append(p.data)
            p = p.next
        return results
        # raise AttributeError(u"can't find this element")
