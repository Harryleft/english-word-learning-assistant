<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stars][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<div align="center">
  
[English](./README_EN.md) | 简体中文

</div>

<!-- 项目介绍 -->
<div align="center">
  <h3 align="center">Harry Potter Series English Word Learning Assistant</h3>

  <p align="center">
    基于哈利波特系列英文原著的英语单词学习助手，帮助学习者通过原著进行英语单词学习。
    <br />
    <a href="https://github.com/Harryleft/english-word-learning-assistant"><strong>查看文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Harryleft/english-word-learning-assistant/issues/new?labels=bug">报告Bug</a>
    ·
    <a href="https://github.com/Harryleft/english-word-learning-assistant/issues/new?labels=enhancement">功能建议</a>
  </p>
</div>

<!-- 目录 -->
<details>
  <summary>目录</summary>
  <ol>
    <li><a href="#项目背景">项目背景</a></li>
    <li><a href="#功能特点">功能特点</a></li>
    <li><a href="#项目结构">项目结构</a></li>
    <li><a href="#安装方法">安装方法</a></li>
    <li><a href="#使用说明">使用说明</a></li>
    <li><a href="#致谢">致谢</a></li>
    <li><a href="#许可证">许可证</a></li>
  </ol>
</details>

## 项目背景

本项目旨在帮助英语学习者通过哈利波特系列英文原著进行英语单词学习。

通过提取原著中的例句、下载单词发音、AI图像化分析单词等功能，为学习者提供一个便捷的英语单词学习工具。

## 功能特点

- 📚 从哈利波特系列原著中提取例句
- 🔍 支持单词变体和词形变化识别
- 🎧 自动下载单词发音
- 🤖 AI 分析单词用法和助记
- ✨ 支持批量单词处理

## 项目结构

```
.
├── main.py                 # 主程序入口
├── find_sentence_with_word.py  # 例句提取模块
├── english_pronounce_audio_download.py  # 音频下载模块
├── ai_explain.py          # AI 分析模块
├── data/                  # 原著文本目录
├── output/               # 输出目录
└── audio_downloads/      # 音频文件目录
```

## 安装方法

1. 克隆项目
```bash
git clone https://github.com/Harryleft/english-word-learning-assistant.git
cd english-word-learning-assistant
```

2. 安装依赖
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

3. 配置环境变量
```bash
# 设置 OpenAI API Key（用于 AI 分析功能）
export OPENAI_API_KEY=your_api_key
```

## 使用说明

1. 运行主程序
```bash
python main.py
```

2. 选择功能
- 1: 查找单词在文本中的例句
- 2: 下载单词发音
- 3: 分析单词用法
- 4: 执行完整学习流程

3. 输入单词
- 支持输入多个单词（用空格分隔）
- 自动处理单词变体形式

## 致谢

- [spaCy](https://spacy.io/) - 自然语言处理库
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 音频下载工具
- [OpenAI API](https://openai.com/blog/openai-api) - AI 分析支持

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

<!-- 徽章链接 -->
[contributors-shield]: https://img.shields.io/github/contributors/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[contributors-url]: https://github.com/Harryleft/english-word-learning-assistant/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[forks-url]: https://github.com/Harryleft/english-word-learning-assistant/network/members
[stars-shield]: https://img.shields.io/github/stars/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[stars-url]: https://github.com/Harryleft/english-word-learning-assistant/stargazers
[issues-shield]: https://img.shields.io/github/issues/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[issues-url]: https://github.com/Harryleft/english-word-learning-assistant/issues
[license-shield]: https://img.shields.io/github/license/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[license-url]: https://github.com/Harryleft/english-word-learning-assistant/blob/master/LICENSE 