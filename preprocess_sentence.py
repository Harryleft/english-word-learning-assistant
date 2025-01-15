# -*- coding: utf-8 -*-
import os
import re

def preprocess_text(text):
    """
    预处理文本，将不必要的换行符替换为空格。

    Args:
        text: 要处理的文本。

    Returns:
        处理后的文本。
    """
    # 将所有类型的换行符统一为 \n
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # 使用正则表达式匹配并去除句子中间的换行
    # 解释：
    # (?<=[^.!?])  : 肯定反向查找，表示匹配到的位置前面不是 .!? 之一
    # \n           : 匹配换行符
    # (?=\S)       : 肯定正向查找，表示匹配到的位置后面是一个非空白字符
    text = re.sub(r"(?<=[^.!?])\n(?=\S)", " ", text)
    return text

def process_book(filepath):
    """
    处理单个哈利波特 Markdown 文档，进行预处理。

    Args:
        filepath: Markdown 文档的路径。

    Returns:
        处理后的文本。
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        processed_text = preprocess_text(text)
        return processed_text
    except FileNotFoundError:
        print(f"文件未找到: {filepath}")
        return ""

def save_processed_book(filepath, text):
    """
    将处理后的文本保存到新的 Markdown 文件中。

    Args:
        filepath: 原始文件的路径。
        text: 要保存的文本。
    """
    new_filepath = filepath.replace(".md", "_processed.md")
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"已保存处理后的文件: {new_filepath}")

def main():
    """
    主函数，用于获取用户输入的哈利波特书籍目录，并对每个文件进行预处理。
    """
    book_dir = input("请输入哈利波特系列 Markdown 文档所在的目录: ")

    for filename in os.listdir(book_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(book_dir, filename)
            processed_text = process_book(filepath)
            if processed_text:
                save_processed_book(filepath, processed_text)

if __name__ == "__main__":
    main()
