# -*- encoding=utf-8 -*-
from flask import Flask, request
import jieba.posseg as pseg
import random
import json
import sys

replace_list = ['n', 'nr', 'ns', 'v', 'a', 'd']

probability = 50

word_list = {}

with open('./words.json', 'r', encoding='utf-8') as f:
    word_list = json.loads(f.read())


def grassify(inp, prob=probability):
    words = pseg.cut(inp)
    outp = ''
    for word, flag in words:
        if flag in replace_list and random.randint(0, 100) <= prob:
            word = word_list[flag][random.randint(0, len(word_list[flag]) - 1)]
        outp += word
    return outp


if len(sys.argv) != 4:
    print('Usage: %s <input_file> <output_file> <probability>' % sys.argv[0])
    exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
probability = int(sys.argv[3])

with open(input_file, 'r', encoding='utf-8') as f:
    with open(output_file, 'w', encoding='utf-8') as fout:
        for line in f:
            fout.write(grassify(line, probability) + '\n')
