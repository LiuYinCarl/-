# !/usr/bin/env python
# -*- codeing: utf-8 -*-

"""
GUI 模块， 整个系统的核心，在这个模块中调用 dLink 模块和 connect_mysql模块
参考资料：
    https://www.cnblogs.com/shemingli/p/6354073.html
    entry https://blog.csdn.net/liuxu0703/article/details/60781107
    Tkinter 15种控件简介  https://blog.csdn.net/qq_25600055/article/details/46941895
    Grid布局管理器详解 https://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html
    Listbox https://blog.csdn.net/m0_37264397/article/details/79079259
            https://blog.csdn.net/aa1049372051/article/details/51878578
            https://blog.csdn.net/jcodeer/article/details/1811310
    messagebox  http://www.17python.com/blog/25

"""
__author__ = 'bearcarl'
__version__= '1.0'

from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # 导入提示窗口包
from connect_mysql import Mysql_conn
from dLink import DouLink, Node


# 设置窗口大小
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


class GUI:
    """给每个组件都命名是为了以后迭代方便"""

    def __init__(self, root):
        # 创建双向链表
        self.dl = DouLink()
        root.title('学员信息管理系统  http://www.bearcarl.top')
        # 设置窗口大小
        center_window(root, 800, 600)
        root.maxsize(1200, 800)
        root.minsize(300, 240)
        root.iconbitmap('1.ico')

        # 添加学员
        upload_label_1 = ttk.Label(root, text='姓名').grid(row=0, column=1)
        upload_label_2 = ttk.Label(root, text='年龄').grid(row=1, column=1)
        upload_label_3 = ttk.Label(root, text='电话号码').grid(row=2, column=1)
        upload_label_4 = ttk.Label(root, text='入学日期').grid(row=3, column=1)
        upload_label_5 = ttk.Label(root, text='邮箱').grid(row=4, column=1)

        upload_entry_1 = ttk.Entry(root)
        upload_entry_2 = ttk.Entry(root)
        upload_entry_3 = ttk.Entry(root)
        upload_entry_4 = ttk.Entry(root)
        upload_entry_5 = ttk.Entry(root)

        upload_entry_1.grid(row=0, column=2)
        upload_entry_2.grid(row=1, column=2)
        upload_entry_3.grid(row=2, column=2)
        upload_entry_4.grid(row=3, column=2)
        upload_entry_5.grid(row=4, column=2)

        upload_button_1 = ttk.Button(root, text="提交信息", command=lambda: upload_event()).grid(row=6, column=2)

        # 修改信息
        update_label_1 = ttk.Label(root, text='需更新学号').grid(row=0, column=3)
        update_label_2 = ttk.Label(root, text='姓名').grid(row=1, column=3)
        update_label_3 = ttk.Label(root, text='年龄').grid(row=2, column=3)
        update_label_4 = ttk.Label(root, text='电话号码').grid(row=3, column=3)
        update_label_5 = ttk.Label(root, text='入学日期').grid(row=4, column=3)
        update_label_6 = ttk.Label(root, text='邮箱').grid(row=5, column=3)

        update_entry_1 = ttk.Entry(root)
        update_entry_2 = ttk.Entry(root)
        update_entry_3 = ttk.Entry(root)
        update_entry_4 = ttk.Entry(root)
        update_entry_5 = ttk.Entry(root)
        update_entry_6 = ttk.Entry(root)

        update_entry_1.grid(row=0, column=4)
        update_entry_2.grid(row=1, column=4)
        update_entry_3.grid(row=2, column=4)
        update_entry_4.grid(row=3, column=4)
        update_entry_5.grid(row=4, column=4)
        update_entry_6.grid(row=5, column=4)

        update_button = ttk.Button(root, text='更新信息',command=lambda: update_event()).grid(row=6, column=4)

        # 查找学员
        search_listbox = Listbox(root, height=3)
        for item in ['按学号查找', '按姓名查找', '按年龄查找']:
            search_listbox.insert(END, item)
        search_listbox.grid(row=0, column=6, rowspan=3)

        search_label = ttk.Label(root, text='查找参数').grid(row=3, column=5)

        search_entry = ttk.Entry(root)
        search_entry.grid(row=3, column=6)

        search_button = ttk.Button(root, text='查找', command=lambda: search_event()).grid(row=5, column=6)
        delete_button = ttk.Button(root, text='删除该学员', command=lambda: delete_event()).grid(row=6, column=6)

        # 排序
        sort_button_1 = ttk.Button(root, text='按学号排序', command=lambda: sort_event(1)).grid(row=1, column=7)
        sort_button_1 = ttk.Button(root, text='按姓名排序', command=lambda: sort_event(2)).grid(row=2, column=7)
        sort_button_1 = ttk.Button(root, text='按年龄排序', command=lambda: sort_event(3)).grid(row=3, column=7)

        # 信息提示框
        info_label = ttk.Label(root, text="信息展示窗口", background='#66ccff', width=100, anchor='center') \
            .grid(row=7, column=0, columnspan=8)

        # 信息展示
        Listbox(root, height=8, width=110).grid(row=8, column=0, columnspan=10)

        # 选择函数， 直接用SQL进行排序
        def sort_event(n):
            # 连接数据库
            conn_1 = Mysql_conn()
            if n == 1:
                # 构造查询SQL
                sw = 'SELECT * FROM STUDENT ORDER BY ID'
                stu_info = conn_1.select(sw)
                show_listbox = Listbox(root, height=8, width=110)
                for row in stu_info:
                    show_listbox.insert(END, row)
                show_listbox.grid(row=8, column=0, columnspan=10)
                messagebox.showinfo("排序", "已将学员按学号排序！")
            elif n == 2:
                # 构造查询SQL
                sw = 'SELECT * FROM STUDENT ORDER BY NAME'
                stu_info = conn_1.select(sw)
                show_listbox = Listbox(root, height=8, width=110)
                for row in stu_info:
                    show_listbox.insert(END, row)
                show_listbox.grid(row=8, column=0, columnspan=10)
                messagebox.showinfo("排序", "已将学员按姓名排序！")
            elif n == 3:
                # 构造查询SQL
                sw = 'SELECT * FROM STUDENT ORDER BY AGE'
                stu_info = conn_1.select(sw)
                show_listbox = Listbox(root, height=8, width=110)
                for row in stu_info:
                    show_listbox.insert(END, row)
                show_listbox.grid(row=8, column=0, columnspan=10)
                messagebox.showinfo("排序", "已将学员按年龄排序！")
            # 关闭数据库连接
            conn_1.close_conn()

        # 提交学员信息
        def upload_event():
            i = []
            # 连接数据库
            conn_1 = Mysql_conn()
            # root.update()
            i.append(upload_entry_1.get())
            i.append(upload_entry_2.get())
            i.append(upload_entry_3.get())
            i.append(upload_entry_4.get())
            i.append(upload_entry_5.get())
            # 清除输入框中的数据
            upload_entry_1.delete(0, END)
            upload_entry_2.delete(0, END)
            upload_entry_3.delete(0, END)
            upload_entry_4.delete(0, END)
            upload_entry_5.delete(0, END)
            # 构造SQL语句
            uw = "INSERT INTO STUDENT (NAME, AGE, TEL_NUMBER, DATE, EMAIL)" \
                 "VALUES('%s', '%s', '%s', '%s', '%s')" %(i[0], i[1], i[2], i[3], i[4])
            conn_1.insert(uw)
            messagebox.showinfo("保存提示", "已保存学员信息！")
            # 刷新信息区
            sw = 'SELECT * FROM STUDENT ORDER BY ID'
            stu_info = conn_1.select(sw)
            show_listbox = Listbox(root, height=8, width=110)
            for row in stu_info:
                show_listbox.insert(END, row)
            show_listbox.grid(row=8, column=0, columnspan=10)
            # 关闭数据库连接
            conn_1.close_conn()

        # 更新学员信息
        def update_event():
            i = []
            # 连接数据库
            conn_1 = Mysql_conn()
            i.append(update_entry_1.get())
            i.append(update_entry_2.get())
            i.append(update_entry_3.get())
            i.append(update_entry_4.get())
            i.append(update_entry_5.get())
            i.append(update_entry_6.get())
            # 清除输入框中的数据
            update_entry_1.delete(0, END)
            update_entry_2.delete(0, END)
            update_entry_3.delete(0, END)
            update_entry_4.delete(0, END)
            update_entry_5.delete(0, END)
            update_entry_6.delete(0, END)
            # 构造SQL语句
            uw = "UPDATE STUDENT SET NAME = '%s', AGE = '%s', TEL_NUMBER = '%s', DATE = '%s', EMAIL = '%s' WHERE " \
                 "ID = '%s'"% (i[1], i[2], i[3], i[4], i[5], i[0])
            conn_1.update(uw)
            messagebox.showinfo("更新提示", "已更新学员信息！")
            # 刷新信息区
            sw = 'SELECT * FROM STUDENT ORDER BY ID'
            stu_info = conn_1.select(sw)
            show_listbox = Listbox(root, height=8, width=110)
            for row in stu_info:
                show_listbox.insert(END, row)
            show_listbox.grid(row=8, column=0, columnspan=10)
            # 关闭数据库连接
            conn_1.close_conn()

        # 保存当前首位符合条件的学员的ID
        cur_search_id = None

        def search_event():
            # 连接数据库
            conn_1 = Mysql_conn()
            # 构造SQL语句
            sw = 'SELECT * FROM STUDENT ORDER BY ID'
            stu_info = conn_1.select(sw)
            # 保存当前首位符合条件的学员的ID
            global cur_search_id
            cur_search_id = stu_info[0][0]
            for items in stu_info:
                node = []
                node.append(items[0])
                node.append(items[1])
                node.append(items[2])
                node.append(items[3])
                node.append(items[4])
                node.append(items[5])
                self.dl.add(node)
            key = search_listbox.curselection()
            value = search_entry.get()
            # 删除搜索框中数据
            search_entry.delete(0, END)
            results = self.dl.find(value, key[0])
            if len(results) == 0:
                messagebox.showinfo("查找提示", "未找到该学员！")
            show_listbox = Listbox(root, height=8, width=110)
            for row in results:
                show_listbox.insert(END, row)
            show_listbox.grid(row=8, column=0, columnspan=10)
            # 清空链表
            self.dl.release()
            # 关闭数据库连接
            conn_1.close_conn()

        def delete_event():
            # 连接数据库
            conn_1 = Mysql_conn()
            global cur_search_id
            messagebox.showinfo("删除提示", "该学员信息已删除！")
            # 从数据库中删除该学员，以保持同步
            rw = "DELETE FROM STUDENT WHERE ID = '%d'" % (cur_search_id)
            conn_1.delete(rw)
            # 将cur_search_id 置为 None，防止误删
            cur_search_id = None
            # 断开数据库
            conn_1.close_conn()
            # 刷新数据显示
            Listbox(root, height=8, width=110).grid(row=8, column=0, columnspan=10)


if __name__ == '__main__':
    root = Tk()
    test = GUI(root)
    root.mainloop()
