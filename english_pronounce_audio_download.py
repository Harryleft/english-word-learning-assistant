# -*- coding: utf-8 -*-
import os
import subprocess
import spacy

# 加载 spaCy 英文模型
nlp = spacy.load("en_core_web_sm")

def get_word_base_form(word):
    """获取单词的原形"""
    doc = nlp(word)
    return doc[0].lemma_

def download_audio(word, output_dir="."):
    """
    使用 yt-dlp 下载单词的音频文件。

    Args:
        word: 要下载发音的单词。
        output_dir: 音频文件的输出目录。
    """
    try:
        # 获取单词原形
        base_word = get_word_base_form(word)
        print(f"正在下载 {word} (原形: {base_word}) 的音频...")
        
        # 使用 yt-dlp 下载音频，并指定输出目录和文件名模板
        command = [
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            f"https://dictionary.cambridge.org/us/pronunciation/english/{base_word}",
            "-o", f"{output_dir}/{word}.%(ext)s",  # 保存时使用原始单词形式
        ]
        subprocess.run(command, check=True)
        print(f"已下载 {word} 的音频.")

    except subprocess.CalledProcessError as e:
        print(f"下载 {word} 的音频失败: {e}")
        # 如果原形下载失败，尝试使用原始形式
        try:
            command = [
                "yt-dlp",
                "-x",
                "--audio-format", "mp3",
                f"https://dictionary.cambridge.org/us/pronunciation/english/{word}",
                "-o", f"{output_dir}/{word}.%(ext)s",
            ]
            subprocess.run(command, check=True)
            print(f"已使用原始形式下载 {word} 的音频.")
        except subprocess.CalledProcessError as e:
            print(f"使用原始形式下载 {word} 的音频也失败了: {e}")

# def main():
#     """主函数，用于获取用户输入的单词列表并下载音频。"""
#     # 获取用户输入的单词列表
#     words = input("请输入要下载发音的单词，用空格分隔: ").split()

#     # 创建输出目录（如果不存在）
#     output_dir = "audio_downloads"
#     os.makedirs(output_dir, exist_ok=True)

#     # 循环下载每个单词的音频
#     for word in words:
#         download_audio(word, output_dir)

#     print("所有音频下载完成！")

# if __name__ == "__main__":
#     main()

