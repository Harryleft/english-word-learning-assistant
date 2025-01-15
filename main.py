# -*- coding: utf-8 -*-
import os
from find_sentence_with_word import find_sentences_with_lemmatization, save_sentences_to_markdown
from english_pronounce_audio_download import download_audio
from ai_explain import analyze_word_usage, save_analysis

def get_word_input():
    """获取用户输入的单词"""
    while True:
        words = input("请输入要处理的单词 (多个单词请用空格分隔): ").strip()
        if not words:
            print("输入不能为空，请重新输入")
            continue
            
        # 分割并过滤空字符串
        word_list = [w.strip() for w in words.split() if w.strip()]
        
        if not word_list:
            print("请输入有效的单词")
            continue
            
        # 验证输入是否包含无效字符
        invalid_chars = set('\\/:*?"<>|')  # Windows文件系统不允许的字符
        has_invalid = False
        for word in word_list:
            if any(char in invalid_chars for char in word):
                print(f"单词 '{word}' 包含无效字符，请重新输入")
                has_invalid = True
                break
        
        if has_invalid:
            continue
            
        return word_list

def process_words_sentences(words, book_dir):
    """处理单词查找句子的功能"""
    results = []  # 记录成功找到例句的单词
    for word in words:
        all_sentences = []
        for filename in os.listdir(book_dir):
            if filename.endswith(".md"):
                filepath = os.path.join(book_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        text = f.read()
                    sentences = find_sentences_with_lemmatization(word, text)
                    all_sentences.extend(sentences)
                except FileNotFoundError:
                    print(f"文件未找到: {filepath}")
                    continue

        if all_sentences:
            save_sentences_to_markdown(word, all_sentences)
            print(f"\n包含单词 '{word}' 的句子已保存至 'output/{word}/{word}.md'")
            results.append(word)
        else:
            print(f"没有找到包含单词 '{word}' 的句子")
    
    return results

def process_words_audio(words):
    """处理单词音频下载的功能"""
    output_dir = "audio_downloads"
    os.makedirs(output_dir, exist_ok=True)
    for word in words:
        download_audio(word, output_dir)

def process_words_analysis(words):
    """处理单词分析的功能"""
    for word in words:
        markdown_file = os.path.join("output", word, f"{word}.md")
        if not os.path.exists(markdown_file):
            print(f"未找到 {word} 的例句文件，跳过分析")
            continue
            
        print(f"正在分析单词 {word} ...")
        
        # 读取例句并进行分析
        with open(markdown_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()[2:]  # 跳过表头
            sentences_data = []
            for line in lines:
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        sentences_data.append({
                            'word': parts[1].strip(),
                            'sentence': parts[2].strip()
                        })
        
        if sentences_data:
            analysis = analyze_word_usage(word, sentences_data)
            save_analysis(word, sentences_data, analysis)
            print(f"分析结果已更新到 output/{word}/{word}.md")
        else:
            print(f"未找到 {word} 的有效例句，跳过分析")

def show_menu():
    """显示功能菜单"""
    print("\n=== Harry Potter Series | 英语学习小助手 ===")
    print("1. 查找单词在文本中的例句")
    print("2. 下载单词发音")
    print("3. 分析单词用法")
    print("4. 执行完整学习流程（查找例句+下载发音+分析用法）")
    print("0. 退出程序")
    return input("请选择功能 (0-4): ").strip()

def main():
    """主函数"""
    book_dir = r"S:\PythonProject\english-word-audio-download\data"  # 可以根据实际情况修改路径
    
    while True:
        choice = show_menu()
        
        if choice == "0":
            print("感谢使用！再见！")
            break
            
        if choice not in ["1", "2", "3", "4"]:
            print("无效的选择，请重试")
            continue
            
        words = get_word_input()
        
        if choice == "1":
            process_words_sentences(words, book_dir)
        elif choice == "2":
            process_words_audio(words)
        elif choice == "3":
            process_words_analysis(words)
        elif choice == "4":
            # 执行完整流程
            found_words = process_words_sentences(words, book_dir)
            if found_words:  # 只处理成功找到例句的单词
                process_words_analysis(found_words)
                process_words_audio(found_words)

if __name__ == "__main__":
    main()
