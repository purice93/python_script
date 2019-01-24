""" 
@author: zoutai
@file: organizeFiles.py 
@time: 2018/11/13 
@description: 将语音文件按内容组装
即将 说话人-说话内容 转换为：说话内容-说话人
"""
import os
import wave
import numpy as np

speakers = 10
oldPath = "G:\\语音数据集\\唤醒\\King-ASR-M-005"
newPath = "G:\\语音数据集\\唤醒\\King-ASR-M-005-new"


def copyFile(path):
    for childfiles in os.listdir(path):
        # childfiles=speaker001
        childfilenames = os.path.join(path, childfiles)
        if not os.path.isdir(childfilenames):
            continue
        for wave in os.listdir(childfilenames):
            # wave=00011_fixed_16000.wav
            wordName = wave[:wave.find('_')] # 00011
            wavename = os.path.join(childfilenames, wave)
            newDirPath = os.path.join(newPath, wordName)
            if not os.path.exists(newDirPath):
                os.makedirs(newDirPath)
            newWavename = os.path.join(newDirPath,wave.replace(wordName,childfiles))
            open(newWavename, "wb").write(open(wavename, "rb").read())


def main():
    path = "G:\\语音数据集\\唤醒\\King-ASR-M-005-16000"
    copyFile(path)


if __name__ == '__main__':
    main()