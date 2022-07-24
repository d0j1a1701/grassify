# Grassify - 自动生草系统

## 功能

随机替换文本中的文字达到生草效果。

## 用法

`pip install -r requirements.txt` 安装所有依赖

`py grassify.py <input_file> <output_file> <probability>`

    * input_file: 输入文件
    * output_file: 输出文件
    * probability: 每个词被替换的概率(%)，0-100之间的整数

## 样例

```
# in.txt

我是一个蒟蒻，我喜欢吃苹果。

```

`py grassify.py in.txt out.txt 70`

```
# out.txt

我是一个蒟蒻，我抽象观察苹果。

```

大样例请见仓库。

## 实现

将给定句子分词并划分词性，再用词库中同词性的词替换。

具体可见代码。

## 自定义词库

仓库中默认的词库文件是2020年北京全科高考试卷及其答案。

1. 将你的词库样本以`docx`格式放入`/data/raw/`中，其中的非文本元素将会被自动忽略，具体可见仓库。

2. 执行 `py split.py` 以生成词库文件(`words.json`)。