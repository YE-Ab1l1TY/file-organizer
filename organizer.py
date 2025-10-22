# -*- coding: utf-8 -*-
# @Author: YE-AB1L1TY
# @Date: 2025/10/22
# @Description: 此文件用于...

# -*- coding: utf-8 -*-
# @Author: YE-AB1L1TY
# @Date: 2025/10/15
# @Description: 此文件用于...

import os
import shutil
import tkinter as tk
from tkinter import filedialog

FILE_FENLEI={
    "文档":[".pdf",".docx",".txt",".doc",".pptx",".xlsx"],
    "图片":['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    '代码': ['.py', '.java', '.cpp', '.c', '.html', '.css', '.js'],
    '压缩包': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '音频': ['.mp3', '.wav', '.flac', '.aac'],
    '视频': ['.mp4', '.avi', '.mov', '.mkv', '.wmv']
}

"""根据文件扩展名返回分类"""
def get_file_category(ext):
    for category,exts in FILE_FENLEI.items():
        if ext in exts:
            return category
    return "其他"

"""创建所有分类文件夹"""
def create_category_folders(target_folders):
    for category in FILE_FENLEI:
        category_path = os.path.join(target_folders, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"创建文件夹：{category}")

"""整理源文件夹中的文件"""
def orgnize_files(source_folder):
    print(f"开始整理文件夹：{source_folder}")

    create_category_folders(source_folder)

    try:
        items = os.listdir(source_folder)
        moved_files =0

        for item in items:
            item_path=os.path.join(source_folder, item)

            if os.path.isfile(item_path):
                _,ext=os.path.splitext(item)
                ext=ext.lower()

                category=get_file_category(ext)

                if category !="其他":

                    target_folder = os.path.join(source_folder, category)
                    target_path = os.path.join(target_folder, item)

                shutil.move(item_path,target_path)
                print(f"移动{item}-》{category}")
                moved_files += 1

            else:
                print(f"跳过{item},未知类型{ext}")

        print(f"整理完成，共移动{moved_files}个文件。")

    except Exception as e:
        print(f"出现错误：{e}")


def scan_folder(folder_path):
    print(f"扫描文件：{folder_path}")

    try:

        items=os.listdir(folder_path)

        for item in items:
            item_path=os.path.join(test_folder, item)
            if os.path.isfile(item_path):
                print(f"{item}是一个文件")
                _,ext=os.path.splitext(item)
                ext=ext.lower()

                print(f"文件:{item}|拓展名:{ext}")

            elif os.path.isdir(item_path):
                print(f"{item}是一个文件夹")
    except FileNotFoundError:
        print(f"Error，找不到文件{folder_path}")
    except PermissionError:
        print(f"Error：没有权限访问文件夹{folder_path}")

def select_and_organize():

    root=tk.Tk()         # 创建一个隐藏的主窗口
    root.withdraw()      # 隐藏GUI窗口

    selected_folder=filedialog.askdirectory(title="请选择需要整理的文件夹")

    if not selected_folder:
        print("未选择文件夹")
        return

    orgnize_files(selected_folder)

    print(f"整理完成！文件夹 '{selected_folder}' 已处理。")
    input("按回车键退出...")  # 暂停程序，防止窗口立刻关闭

if __name__ == '__main__':

    select_and_organize()
