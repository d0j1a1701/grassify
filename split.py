# 导入所需库
import jieba.posseg as pseg
from docx import Document
import json
import os

# 文件地址后的/不能省略
filePath = os.getcwd() + r"/data/raw/"
savePath = os.getcwd() + r"/"
os.chdir(filePath)

output = {}

for root, dirs, files in os.walk(r'%s' % (filePath), topdown=False):
    for file_name in files:
        # 打开word文档
        document = Document(root+file_name)

        # 获取所有段落
        all_paragraphs = document.paragraphs

        for paragraph in all_paragraphs:
            # 写入每一个段落的文字,'\n'分行
            # 自带文件关闭功能，不需要再写f.close()
            words = pseg.cut(paragraph.text)
            for text, flag in words:
                if flag in output:
                    output[flag].append(text)
                else:
                    output[flag] = [text]

# 将output中的所有value去重
for key in output:
    output[key] = list(set(output[key]))

js = json.dumps(output)

with open(savePath+"words.json", "w") as f:
    # 将output转为字符串形式输出到f
    f.write(js)
    f.close()
