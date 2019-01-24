""" 
@author: zoutai
@file: getLoundestSection.py 
@time: 2018/11/13 
@description: 用于截断最大的语音部分
"""

import sys
import wave

import numpy as np
import os

desire_len = 16000
oldPath = "G:\\语音数据集\\唤醒\\King-ASR-M-005"
newPath = "G:\\语音数据集\\唤醒\\King-ASR-M-005-16000"


def modify_filename(path):
    for childfiles in os.listdir(path):
        childfilenames = os.path.join(path, childfiles)
        if os.path.isdir(childfilenames):
            modify_filename(childfilenames)
        elif childfilenames.endswith('.wav')==False:
            continue
        else:
            wav = wave.open(childfilenames)
            # print('channel:', wav.getnchannels())
            # channel = wav.getnchannels()
            # sampwidth = wav.getsampwidth()
            # framerate = wav.getframerate()
            #
            # if channel != 1 or sampwidth != 2 or framerate != 8000:
            #     print('channel:', channel, 'sampwidth:', sampwidth, 'rate:', framerate)
            # print('only mono 16k/samples 16bits suported')
            # print('frames:', wav.getnframes())
            frames_data = wav.readframes(wav.getnframes())
            # print (frames_data[10000:10100])
            data = np.fromstring(frames_data, dtype=np.int16)
            # print(data[6000:8000])
            start, end = get_loudest_section(data, desire_len)
            # print(start, end)

            childfilenames = childfilenames.replace(oldPath,newPath)
            if len(sys.argv) > 2:
                out_file_name = sys.argv[2]
            else:
                out_file_name = childfilenames[:-4] + '_fixed_16000.wav'

            # create parent dir
            parentDir = os.path.dirname(out_file_name)
            if not os.path.exists(parentDir):
                os.makedirs(parentDir)

            wav_out = wave.open(out_file_name, 'wb')
            wav_out.setnchannels(1)
            wav_out.setsampwidth(2)
            wav_out.setframerate(8000)
            # wav_out.setnframes(16000)
            wav_out.writeframes(data[start:end])
            wav_out.close()


def main():
    # input_file = sys.argv[1]
    path = "G:\\语音数据集\\唤醒\\King-ASR-M-005"
    modify_filename(path)


def get_loudest_section(data, desire_len):
    '''
    原理相当于取固定长度中，累积和最大的那一段
    :param data:
    :param desire_len:
    :return:
    '''
    if len(data) < desire_len:
        return (0, len(data))

    start, end, max_sec_sum, max_start, max_end = 0, 0, 0, 0, 0

    sec_sum = np.int32(data[start])

    while end + 1 < len(data):
        end = end + 1
        if (end - start) >= desire_len:
            sec_sum -= abs(data[start])
            start = start + 1

        sec_sum += abs(data[end])
        if max_sec_sum < sec_sum:
            # print(sec_sum)
            max_sec_sum, max_start, max_end = sec_sum, start, end

    return (max_start, max_end)


if __name__ == '__main__':
    main()