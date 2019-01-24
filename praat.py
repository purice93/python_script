"""
@author: ZouTai
@file: praat.py
@time: 2019/1/24.py
@description: praat便捷标注脚本
"""


'''
编码说明：
1.首先待读取的文本文件需要提前转换为utf-8格式
2.encoding='UTF-8',设置编码读取格式
'''
import os

path = "E:\\下载临时\\WeChat Files\\ZT530337704\\Files\\record_keyword_volume_2\\file"  # 文件夹目录
new_path = "E:\\下载临时\\WeChat Files\\ZT530337704\\Files\\record_keyword_volume_2_new\\file"  # 文件夹目录
files = os.listdir(path)  # 得到文件夹下的所有文件名称
s = []


def modify(filepath, new_filepath):
    print(filepath)
    lines = open(filepath, 'r', encoding='UTF-8').readlines()  # 打开文件，读入每一行
    fp = open(new_filepath, 'w')
    for i in range(0, len(lines)):
        if (i - 17) % 4 == 0 and i >= 17:
            if lines[i].find('""') < 0:
                print("切分格式错误，未找到""！！可能是少切分了")
        if i == 17 or i == 37 or i == 57:
            line = lines[i]
            text = line.replace('""', '"sli"')
            fp.write(text)
        elif i == 21:
            fp.write(lines[i].replace('""', '"增"'))
        elif i == 25:
            fp.write(lines[i].replace('""', '"大"'))
        elif i == 29 or i == 49:
            fp.write(lines[i].replace('""', '"音"'))
        elif i == 33 or i == 53:
            fp.write(lines[i].replace('""', '"量"'))
        elif i == 41:
            fp.write(lines[i].replace('""', '"减"'))
        elif i == 45:
            fp.write(lines[i].replace('""', '"小"'))
        elif lines[i].find('""') >= 0:
            print("切分格式错误，多切了！！")
        else:
            fp.write(lines[i])
    fp.close()  # 关闭文件


if not os.path.exists(new_path):
    os.mkdir(new_path)
for file in files:  # 遍历文件夹
    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
        if file.endswith('.TextGrid'):
            new_filepath = os.path.join(new_path, file)
            filepath = os.path.join(path, file)
            modify(filepath, new_filepath)
