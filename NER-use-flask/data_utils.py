#!/usr/bin/python
# -*- coding: UTF-8 -*-
#微信公众号 AI壹号堂 欢迎关注
#Author bruce

import jieba
jieba.initialize()

def get_seg_features(words):
    """
    利用jieba分词
    采用类似bioes的编码，0表示单个字成词, 1表示一个词的开始， 2表示一个词的中间，3表示一个词的结尾
    :param words:
    :return:
    """
    seg_features = []

    word_list = list(jieba.cut(words))

    for word in word_list:
        if len(word) == 1:
            seg_features.append(0)
        else:
            temp = [2] * len(word)
            temp[0] = 1
            temp[-1] = 3
            seg_features.extend(temp)
    return seg_features

def input_from_line(line, word_to_id):
    """
    :param line:
    :param word_to_id:
    :return:
    """
    inputs = list()
    inputs.append([line])
    if line is None:
        raise Exception("错误的输入")
    line.replace(" ","$")
    inputs.append(
        [
            [word_to_id[word] if word in word_to_id else word_to_id["<UNK>"] for word in line]
        ]
    )
    inputs.append([get_seg_features(line)])
    inputs.append([[]])
    return inputs

