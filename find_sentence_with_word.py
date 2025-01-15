import os
import re
import spacy

# 加载 spaCy 英文模型
nlp = spacy.load("en_core_web_sm")

def find_sentences_with_lemmatization(word, text):
    """
    从文本中提取包含指定单词及其所有词形变体的句子。

    Args:
        word: 要查找的单词。
        text: 要搜索的文本。

    Returns:
        包含指定单词及其所有词形变体的句子列表。
    """
    doc = nlp(text)
    lemma = nlp(word)[0].lemma_  # 获取单词的词元

    sentences = []
    for sent in doc.sents:
        for token in sent:
            if token.lemma_ == lemma:
                sentences.append(sent.text)
                break  # 找到一个匹配的单词就跳到下一个句子

    return sentences

def process_book(filepath, word):
    """
    处理单个哈利波特 Markdown 文档，提取包含指定单词及其所有词形变体的句子。

    Args:
        filepath: Markdown 文档的路径。
        word: 要查找的单词。

    Returns:
        包含指定单词及其所有词形变体的句子列表。
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        # 这一步可以进行预处理
        # text = preprocess_text(text)
        sentences = find_sentences_with_lemmatization(word, text)
        return sentences
    except FileNotFoundError:
        print(f"文件未找到: {filepath}")
        return []

def save_sentences_to_markdown(word, sentences):
    """
    将包含指定单词及其所有词形变体的句子保存为 Markdown 表格格式。

    Args:
        word: 要查找的单词。
        sentences: 包含指定单词及其所有词形变体的句子列表。
    """
    output_dir = os.path.join("output", word)
    os.makedirs(output_dir, exist_ok=True)
    output_filepath = os.path.join(output_dir, f"{word}.md")
    
    # 获取单词的所有词形变体
    doc = nlp(word)
    lemma = doc[0].lemma_
    
    def highlight_word(sentence):
        """在句子中高亮显示目标单词及其变体"""
        words = sentence.split()
        for i, w in enumerate(words):
            # 清理单词（去除标点符号）
            clean_word = ''.join(c for c in w if c.isalnum())
            if clean_word:
                # 检查是否是目标单词的变体
                doc_w = nlp(clean_word)
                if doc_w[0].lemma_ == lemma:
                    # 保留原始标点符号
                    prefix = w[:w.index(clean_word)] if w.index(clean_word) > 0 else ''
                    suffix = w[w.index(clean_word) + len(clean_word):] if w.index(clean_word) + len(clean_word) < len(w) else ''
                    words[i] = f"{prefix}**{clean_word}**{suffix}"
        return ' '.join(words)

    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write("| Word | Sentence |\n")
        f.write("| --- | --- |\n")
        for sentence in sentences:
            # 清理句子中的换行符和多余的空格
            cleaned_sentence = ' '.join(sentence.strip().split())
            # 高亮显示目标单词
            highlighted_sentence = highlight_word(cleaned_sentence)
            f.write(f"| {word} | {highlighted_sentence} |\n")

def main():
    """
    主函数，用于获取用户输入的单词和哈利波特书籍目录，并输出包含该单词及其所有词形变体的句子。
    """
    word = input("请输入要查找的单词: ")
    book_dir = r"S:\PythonProject\english-word-audio-download\data"

    all_sentences = []
    for filename in os.listdir(book_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(book_dir, filename)
            sentences = process_book(filepath, word)
            all_sentences.extend(sentences)

    if all_sentences:
        save_sentences_to_markdown(word, all_sentences)
        print(
            f"\n包含单词 '{word}' 及其所有词形变体的句子已保存至 'output/{word}/{word}_sentences.md'。\n")
    else:
        print(
            f"在哈利波特系列中没有找到包含单词 '{word}' 及其所有词形变体的句子。")
